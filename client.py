import requests

url = "http://localhost:8000/mcp"

headers = {
    "Accept": "text/event-stream, application/json",
}

body = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1,
    "params": {}
}

response = requests.post(url, headers=headers, json=body)

for line in response.iter_lines():
    if line:
        print(line)