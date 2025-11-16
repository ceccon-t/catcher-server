# Catcher Server 

Minimal server that accepts any request to any endpoint and logs the HTTP method/verb, endpoint and body payload received.

The server always responds with a 200 OK response, and logs to the console the information about the request.

## Quick start

### 1. Create and activate a virtual environment (optional, but strongly recommended)

Create virtual environment:

```bash 
python3 -m venv env
```

Activate it:

```bash 
source env/bin/activate
```

### 2. Install dependencies

```bash 
pip install -r requirements.txt
```

### 3. Run the server

Using the default port (9999):

```bash 
python server.py
```

Optionally, you can use a custom port:

```bash 
PORT=8000 python server.py
```

## Examples

Simple GET request:

```bash 
curl "http://localhost:9999/some/endpoint?a=b
```

POST with a payload:

```bash
curl -X POST "http://localhost:9999/api/v1/something?id=1" \
    -H "Content-Type: application/json" \
    -d '{"hello": "world"}'
```

## Usage

See [LICENSE](LICENSE).

You are free to use this project without paying me anything.

But, if you do, you are morally obliged to go read The Catcher In The Rye.

