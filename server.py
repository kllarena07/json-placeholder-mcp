from fastmcp import FastMCP
import requests

mcp = FastMCP(name="JSONPlaceholder Caller")

@mcp.tool()
def get_all_posts(
    description="Get all posts from JSONPlaceholder"
):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()

@mcp.tool()
def get_one_post(
    description="Get one post from JSONPlaceholder"
):
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

if __name__ ==  "__main__":
    mcp.run()
