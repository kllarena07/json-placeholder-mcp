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
def get_post_from_id(
    id: int,
    description="Get a post by id from JSONPlaceholder"
):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    return response.json()

@mcp.tool()
def get_comments_from_post_id(
    id: int,
    description="Get post comments from JSONPlaceholder"
):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/comments?postId={id}")
    return response.json()

if __name__ ==  "__main__":
    mcp.run()
