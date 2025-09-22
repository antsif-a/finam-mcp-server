from mcp.server.fastmcp import FastMCP

mcp = FastMCP('calculator')

@mcp.tool()
def add(a: int, b: int):
    return a + b

@mcp.tool()
def substract(a: int, b: int):
    return a - b

@mcp.tool()
def multiply(a: int, b: int):
    return a * b

@mcp.tool()
def divide(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError('division by zero')
    return a / b

@mcp.resource('greeting://{name}')
def get_greeting(name: str):
    return f'Hello, {name}'
