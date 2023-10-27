import aiohttp
import requests
from aiohttp import web
from middlewares import logging_middleware, authorization_middleware
import json 
import ssl   

VAULT_URL = "https://your-vault-url"  # Replace with your HashiCorp Vault URL

async def retrieve_secrets():
    try:
        # Make a request to HashiCorp Vault to retrieve secrets
        response = requests.get(f"{VAULT_URL}/v1/your/secret/path")
        response.raise_for_status()  # Check for HTTP errors

        if response.status_code == 200:
            secrets = response.json()  # Parse the JSON response
            # Store the secrets locally or use them as needed
            with open("secrets.json", "w") as file:
                json.dump(secrets, file)  # Serialize and write secrets to a file
            return secrets
        else:
            print(f"Failed to retrieve secrets. Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request to HashiCorp Vault failed: {e}")
        return None

# Create an aiohttp client session context
async def create_client_session_context(app):
    # Load mTLS certificate and private key
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain('path/to/cert.pem', 'path/to/key.pem')

    app["client_session"] = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context))
    yield
    await app["client_session"].close()

# GET Request Handler
async def get_handler(request):
    return web.json_response({"method": "GET", "message": "GET Request Successful"})

# POST Request Handler
async def post_handler(request):
    data = await request.json()
    return web.json_response({"method": "POST", "message": "POST Request Successful", "data_received": data})

# PUT Request Handler
async def put_handler(request):
    data = await request.json()
    return web.json_response({"method": "PUT", "message": "PUT Request Successful", "data_received": data})

# PATCH Request Handler
async def patch_handler(request):
    data = await request.json()
    return web.json_response({"method": "PATCH", "message": "PATCH Request Successful", "data_received": data})

# DELETE Request Handler
async def delete_handler(request):
    return web.json_response({"method": "DELETE", "message": "DELETE Request Successful"})

# Create an aiohttp web application
app = web.Application()

# Add the client session context
app.cleanup_ctx.append(create_client_session_context)

# Add middleware to the aiohttp application
app.middlewares.append(logging_middleware)
app.middlewares.append(authorization_middleware)  # Add other middlewares as needed

# Add routes for different request types
app.router.add_get('/', get_handler)
app.router.add_post('/', post_handler)
app.router.add_put('/', put_handler)
app.router.add_patch('/', patch_handler)
app.router.add_delete('/', delete_handler)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
