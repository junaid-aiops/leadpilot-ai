from fastapi import FastAPI


app = FastAPI(
    title="LeadPilot AI API",
    version="1.0.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Verify that the API is running."""
    return {
        "status": "healthy",
        "service": "leadpilot-api",
    }