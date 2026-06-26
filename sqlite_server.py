from config.server import mcp
import tools

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )