from config.server import mcp
from config.settings import WORLD_DB
from utils.db import get_db_connection, dicts_from_rows


@mcp.tool()
def get_database_stats():
    """
    Retrieve database statistics.
    """
    conn = get_db_connection(WORLD_DB)

    tables = [
        "countries",
        "cities",
        "states",
        "regions",
        "subregions"
    ]

    stats = {}

    for table in tables:
        cursor = conn.execute(
            f"SELECT COUNT(*) as count FROM {table}"
        )

        stats[f"total_{table}"] = cursor.fetchone()["count"]

    conn.close()

    return stats


@mcp.tool()
def get_popular_currencies():
    """
    Retrieve the most widely used currencies.
    """
    conn = get_db_connection(WORLD_DB)

    cursor = conn.execute("""
        SELECT
            currency,
            currency_name,
            COUNT(*) AS country_count
        FROM countries
        WHERE currency IS NOT NULL
        GROUP BY currency, currency_name
        ORDER BY country_count DESC
        LIMIT 20
    """)

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results