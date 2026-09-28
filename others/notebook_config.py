
"""
MySQL Notebook Configuration
----------------------------
Works in:
1. VS Code Jupyter Notebook
2. CMD / VS Code terminal

Responsibilities:
- Load MySQL credentials from .env
- Validate required configuration
- Test MySQL connectivity
- Configure ipython-sql inside Jupyter
- Display clear success/error messages
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.exc import SQLAlchemyError


# --------------------------------------------------
# 1. Project configuration
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent
ENV_FILE = PROJECT_DIR / "../others/.env"

print("\n========== MySQL Configuration ==========")


def configure_mysql():

    try:
        # --------------------------------------------------
        # 2. Load environment variables
        # --------------------------------------------------

        if not ENV_FILE.exists():
            raise FileNotFoundError(
                f".env file not found: {ENV_FILE}"
            )

        load_dotenv(ENV_FILE, override=True)

        username = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        database = os.getenv("MYSQL_DATABASE")

        # --------------------------------------------------
        # 3. Validate credentials
        # --------------------------------------------------

        required_variables = {
            "MYSQL_USER": username,
            "MYSQL_PASSWORD": password,
            "MYSQL_HOST": host,
            "MYSQL_DATABASE": database,
        }

        missing = [
            key
            for key, value in required_variables.items()
            if not value
        ]

        if missing:
            raise ValueError(
                "Missing environment variables: "
                + ", ".join(missing)
            )

        print("[SUCCESS] Environment variables loaded.")

        # --------------------------------------------------
        # 4. Create MySQL connection URL
        # --------------------------------------------------

        connection_url = URL.create(
            drivername="mysql+pymysql",
            username=username,
            password=password,
            host=host,
            database=database,
        )

        # --------------------------------------------------
        # 5. Test MySQL database connection
        # --------------------------------------------------

        engine = create_engine(connection_url)

        try:
            with engine.connect() as connection:
                connection.exec_driver_sql("SELECT 1")

            print("[SUCCESS] MySQL database connection established.")

        finally:
            engine.dispose()

        # --------------------------------------------------
        # 6. Configure Jupyter SQL magic
        # --------------------------------------------------

        from IPython import get_ipython

        ip = get_ipython()

        if ip is None:
            print(
                "[INFO] Running outside Jupyter. "
                "Database connection verified, "
                "but SQL magic was not configured."
            )
            return True

        ip.run_line_magic("load_ext", "sql")

        ip.run_line_magic(
            "config",
            "SqlMagic.style = 'SINGLE_BORDER'"
        )

        # Reveal password only internally when passing
        # the connection URL to ipython-sql.
        sql_connection_string = (
            connection_url.render_as_string(
                hide_password=False
            )
        )

        ip.run_line_magic(
            "sql",
            sql_connection_string
        )

        print("[SUCCESS] SQL magic configured.")
        print("[SUCCESS] SQL output style: SINGLE_BORDER")
        print("[SUCCESS] MySQL notebook is ready.")

        return True

    except FileNotFoundError as error:
        print(f"[ERROR] {error}")

    except ValueError as error:
        print(f"[ERROR] {error}")

    except SQLAlchemyError as error:
        print("[DATABASE ERROR] MySQL connection failed.")
        print(f"Error type: {type(error).__name__}")
        print(f"Details: {error}")

    except Exception as error:
        print("[CONFIGURATION ERROR] Unexpected error occurred.")
        print(f"Error type: {type(error).__name__}")
        print(f"Details: {error}")

    return False


# --------------------------------------------------
# 7. Execute configuration
# --------------------------------------------------

configure_mysql()