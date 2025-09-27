import os
import sys
import sqlite3
import pandas as pd
from utils_logger import logger

def execute_sql_file(conn, file_path):
    """Read and execute an SQL script file using the provided sqlite3 connection.

    Logs failures and re-raises exceptions so callers can decide how to handle them.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        conn.executescript(sql_script)
        logger.info(f"Executed SQL file: {file_path}")
    except (sqlite3.DatabaseError, sqlite3.Error) as e:
        logger.exception(f"SQLite error executing '{file_path}': {e}")
        raise
    except OSError as e:
        logger.exception(f"Failed to read SQL file '{file_path}': {e}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error executing '{file_path}': {e}")
        raise

def show_table(conn, table_names):
    """Log the row counts for the specified tables."""
    try:
        for table in table_names:
            query = f"SELECT * FROM {table};"
            df = pd.read_sql_query(query, conn)            
            logger.info(f"Table '{table}'")
            logger.info(f"\n {df}")
    except Exception as e:
        logger.exception(f"Error retrieving table: {e}")
        raise

if __name__ == "__main__":
    sqlite_db = "data/books.db"
    conn = None

    try:
        # Ensure directory exists for the sqlite file
        db_dir = os.path.dirname(sqlite_db)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

        conn = sqlite3.connect(sqlite_db)
        logger.info(f"Connected to SQLite database at {sqlite_db}")

        execute_sql_file(conn, "sql_create/01_drop_tables.sql")
        logger.info("Executed drop tables script")
        
        execute_sql_file(conn, "sql_create/02_create_tables.sql")
        logger.info("Executed create tables script")
        print(show_table(conn, ["authors", "books"]))

        execute_sql_file(conn, "sql_create/03_insert_records.sql")
        logger.info("Executed insert records script")
        print(show_table(conn, ["authors", "books"]))

        conn.commit()
        logger.info("Database setup completed successfully.")
    except Exception:
        # Detailed exceptions are already logged in execute_sql_file; rollback and exit
        if conn:
            try:
                conn.rollback()
                logger.info("Rolled back open transaction(s)")
            except Exception:
                logger.exception("Failed to rollback the database connection")
        logger.exception("Database setup failed. Exiting with error.")
        sys.exit(1)
    finally:
        if conn:
            try:
                conn.close()
                logger.info("Database connection closed")
            except Exception:
                logger.exception("Failed to close the database connection")