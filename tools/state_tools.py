from typing import Any, Dict, List

from config.server import mcp
from config.settings import WORLD_DB
from utils.db import get_db_connection, dicts_from_rows


@mcp.tool()
def search_states(
        name: str = "",
        country_code: str = ""
) -> List[Dict[str, Any]]:
    """
    Search states or provinces.
    """
    conn = get_db_connection(WORLD_DB)

    query = "SELECT * FROM states WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")

    if country_code:
        query += " AND country_code=?"
        params.append(country_code.upper())

    query += " ORDER BY name LIMIT 30"

    cursor = conn.execute(query, params)

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results


@mcp.tool()
def get_states_in_country(country_code: str):
    """
    Retrieve states or provinces of a country.
    """
    conn = get_db_connection(WORLD_DB)

    cursor = conn.execute(
        "SELECT * FROM states WHERE country_code=? ORDER BY name",
        [country_code.upper()]
    )

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results