import sqlite3
from config.settings import DB_PATH


def get_db_connection(db_name: str):
    """
    Create and return a sqlite connection.

    Args:
        db_name: Database filename.

    Returns:
        sqlite3 connection object.
    """
    conn = sqlite3.connect(DB_PATH / db_name)
    conn.row_factory = sqlite3.Row
    return conn


def dict_from_row(row):
    """
    Convert sqlite row into dictionary.
    """
    return dict(row) if row else None


def dicts_from_rows(rows):
    """
    Convert list of sqlite rows into dictionaries.
    """
    return [dict(row) for row in rows]