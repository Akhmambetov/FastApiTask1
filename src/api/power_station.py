from fastapi import APIRouter
from sqlalchemy import select
from starlette.exceptions import HTTPException

from src.database import SessionDep
from src.models.power_station import PowerStation
from src.schemas.power_station import PowerStationRead, PowerStationCreate, PowerStationUpdate

router = APIRouter(tags=["Power Stations"])

@router.post("/power_stations", response_model=PowerStationRead)
async def create_power_station(data: PowerStationCreate, session: SessionDep):
    power_station = PowerStation(
        name=data.name,
        station_type=data.station_type,
        power_mw=data.power_mw,
        description=data.description,
    )
    session.add(power_station)
    await session.commit()
    await session.refresh(power_station)

    return power_station

@router.get("/power_station", response_model=list[PowerStationRead])
async def get_power_stations(session: SessionDep):
    query = select(PowerStation)
    result = await session.execute(query)

    return result.scalars().all()

@router.get("/power_station/{station_id}", response_model=PowerStationRead)
async def get_power_station(station_id: int, session: SessionDep):
    power_station = await session.get(PowerStation, station_id)
    if not power_station:
        raise HTTPException(status_code = 404, detail = "PowerStation was not found")

    return power_station

@router.patch("/power_stations/{station_id}", response_model=PowerStationRead)
async def update_power_station(station_id: int, data: PowerStationUpdate, session: SessionDep):
    power_station = await session.get(PowerStation, station_id)
    if not power_station:
        raise HTTPException(status_code = 404, detail = "PowerStation was not found")

    for field in data.model_fields_set:
        setattr(power_station, field, getattr(data, field))

    await session.commit()
    await session.refresh(power_station)

    return power_station

@router.delete("/power_stations/{station_id}")
async def delete_power_station(station_id: int, session: SessionDep):
    power_station = await session.get(PowerStation, station_id)
    if not power_station:
        raise HTTPException(status_code=404, detail="PowerStation was not found")

    await session.delete(power_station)
    await session.commit()

    return {"ok": True}