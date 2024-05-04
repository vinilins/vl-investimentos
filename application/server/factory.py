from fastapi import FastAPI


def create_api_app():
    app = FastAPI(
        title="VL Investimentos",
        version="0.0.1",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )

    @app.get("/")
    def health_root():
        return {"Hello": "World"}

    return app
