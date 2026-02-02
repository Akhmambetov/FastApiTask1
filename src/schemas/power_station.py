from pydantic import BaseModel, Field, ConfigDict

class PowerStationBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    station_type: str = Field(min_length=1, max_length=50)
    power_mw: float = Field(gt=0)
    description: str | None = None

class PowerStationCreate(PowerStationBase):
    pass

class PowerStationUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    station_type: str | None = Field(default=None, min_length=1, max_length=50)
    power_mw: float | None = Field(default=None, gt=0)
    description: str | None = None

class PowerStationRead(PowerStationBase):
    model_config = ConfigDict(from_attributes=True)
    id: int