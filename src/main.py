from fastapi import FastAPI

from src.api.power_station import router as power_station_router

app = FastAPI(title="Power Station API Task 1")

app.include_router(power_station_router)

@app.get("/")
async def root():
    return {"status": "ok"}
