from typing import Any, Dict, List

from config.server import mcp
from config.settings import WORLD_DB
from utils.db import get_db_connection, dict_from_row, dicts_from_rows


@mcp.tool()
def search_countries(name: str = "") -> List[Dict[str, Any]]:
    """
    Search countries using partial name matching.
    """
    conn = get_db_connection(WORLD_DB)

    if name:
        query = "SELECT * FROM countries WHERE name LIKE ? ORDER BY name LIMIT 20"
        params = [f"%{name}%"]
    else:
        query = "SELECT * FROM countries ORDER BY name LIMIT 20"
        params = []

    cursor = conn.execute(query, params)

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results


@mcp.tool()
def get_country(country_code: str) -> Dict[str, Any]:
    """
    Retrieve complete details of a country using ISO code.

    Args:
        country_code: Two-letter ISO code.

    Returns:
        Country information.
    """
    conn = get_db_connection(WORLD_DB)

    cursor = conn.execute(
        "SELECT * FROM countries WHERE iso2=?",
        [country_code.upper()],
    )

    result = cursor.fetchone()

    conn.close()

    return dict_from_row(result) if result else {}


@mcp.tool()
def get_countries_by_region(region: str) -> List[Dict[str, Any]]:
    """
    Retrieve countries belonging to a region.
    """
    conn = get_db_connection(WORLD_DB)

    cursor = conn.execute(
        "SELECT * FROM countries WHERE region LIKE ? ORDER BY name",
        [f"%{region}%"]
    )

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results


@mcp.tool()
def get_countries_by_currency(currency: str) -> List[Dict[str, Any]]:
    """
    Find countries using a currency.
    """
    conn = get_db_connection(WORLD_DB)

    cursor = conn.execute(
        "SELECT * FROM countries WHERE currency=? ORDER BY name",
        [currency.upper()]
    )

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results