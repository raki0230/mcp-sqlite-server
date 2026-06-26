from config.server import mcp
from config.settings import WORLD_DB
from utils.db import get_db_connection, dicts_from_rows


@mcp.tool()
def get_all_regions():
    """
    Retrieve all world regions.
    """
    conn = get_db_connection(WORLD_DB)

    cursor = conn.execute(
        "SELECT * FROM regions ORDER BY name"
    )

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results


@mcp.tool()
def get_subregions_in_region(region_id: int):
    """
    Retrieve subregions belonging to a region.
    """
    conn = get_db_connection(WORLD_DB)

    cursor = conn.execute(
        "SELECT * FROM subregions WHERE region_id=? ORDER BY name",
        [region_id]
    )

    results = dicts_from_rows(cursor.fetchall())

    conn.close()

    return results