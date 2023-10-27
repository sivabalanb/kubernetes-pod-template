from aiohttp import web

# Logging Middleware
async def logging_middleware(request, handler):
    # Log the request details before handling it
    print(f"Received request: {request.method} {request.path}")
    response = await handler(request)
    return response

# Authorization Middleware (Sample)
async def authorization_middleware(request, handler):
    # Check for authorization here (e.g., verify authentication token)
    # For simplicity, we'll just allow all requests in this example
    response = await handler(request)
    return response

# You can define other middlewares here
