from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Docker GitHub Actions Lab",
    version="1.0.0",
)


@app.get("/")
def home() -> dict[str, str]:
    return {
        "message": "FastAPI Docker Actions application version 1"
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "healthy",
        "deployment": "docker-github-actions",
        "version": "v1"
    }