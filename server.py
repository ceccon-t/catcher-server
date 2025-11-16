import logging
import os
from flask import Flask, request, Response

def create_app() -> Flask:
    app = Flask(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    logger = logging.getLogger("catcher-server")

    all_methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"]

    @app.route("/", defaults={"caught_path": ""}, methods=all_methods)
    @app.route("/<path:caught_path>", methods=all_methods)

    def echo(caught_path: str) -> Response:
        query_string = request.query_string.decode("utf-8") if request.query_string else ""
        display_path = request.path if not query_string else f"{request.path}?{query_string}"

        body_text = request.get_data(as_text=True) or "" 
        
        logger.info("Method: %s | Endpoint: %s | Body: %s", request.method, display_path, body_text)

        return Response("OK\n", mimetype="text/plain")
    
    return app

if __name__ == "__main__":
    port_str = os.environ.get("PORT", "9999")
    try:
        port = int(port_str)
    except ValueError:
        raise SystemExit(f"Invalid PORT value: {port_str}. Must be an integer.")
    
    app = create_app()
    app.run(host="0.0.0.0", port=port)