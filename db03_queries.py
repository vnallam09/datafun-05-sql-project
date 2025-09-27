import os
import sys
import sqlite3
import pandas as pd
from utils_logger import logger

def execute_sql_file_show(conn, file_path):
    """Read and execute an SQL script file using the provided sqlite3 connection.

    Logs failures and re-raises exceptions so callers can decide how to handle them.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        df = pd.read_sql_query(sql_script, conn) 
        logger.info(f"Executed SQL file: {file_path} \n")
        logger.info(f"\n {df}")
        
    except (sqlite3.DatabaseError, sqlite3.Error) as e:
        logger.exception(f"SQLite error executing '{file_path}': {e}")
        raise
    except OSError as e:
        logger.exception(f"Failed to read SQL file '{file_path}': {e}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error executing '{file_path}': {e}")
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

        execute_sql_file_show(conn, "sql_queries/query_aggregation.sql")
        logger.info("Executed query_aggregation script")

        execute_sql_file_show(conn, "sql_queries/query_filter.sql")
        logger.info("Executed query_filter script")

        execute_sql_file_show(conn, "sql_queries/query_group_by.sql")
        logger.info("Executed query_group_by script")

        execute_sql_file_show(conn, "sql_queries/query_join.sql")
        logger.info("Executed query_join script")

        execute_sql_file_show(conn, "sql_queries/query_sorting.sql")
        logger.info("Executed query_sorting script")
                
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