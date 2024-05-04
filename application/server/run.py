import uvicorn

from application.server.factory import create_api_app
from application.settings import Settings


app = create_api_app()
settings = Settings()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.server_port, log_level="info")
