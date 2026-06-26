from config.server import mcp
from config.settings import COMMUNITY_DB
from utils.db import get_db_connection


@mcp.tool()
def get_top_chatters():
    """
    Retrieve chatters sorted by message count.

    Returns:
        List containing user names and total messages.
    """
    conn = get_db_connection(COMMUNITY_DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, messages
        FROM chatters
        ORDER BY messages DESC
        """
    )

    results = cursor.fetchall()

    conn.close()

    return [
        {
            "name": name,
            "messages": messages
        }
        for name, messages in results
    ]