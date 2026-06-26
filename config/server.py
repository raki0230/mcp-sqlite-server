from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    name="SQLite Server",
    host="0.0.0.0",
    port=8000,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
        allowed_hosts=[
            "127.0.0.1:*",
            "localhost:*",
            "mcp-sqlite-server-wi5j.onrender.com",
        ],
        allowed_origins=[
            "http://127.0.0.1:*",
            "http://localhost:*",
            "https://mcp-sqlite-server-wi5j.onrender.com",
        ],
    ),
)