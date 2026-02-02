from sqlalchemy import String, Numeric, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database import Base

class PowerStation(Base):
    __tablename__ = "power_stations"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(100), nullable = False)
    station_type: Mapped[str] = mapped_column(String(50), nullable = False)
    power_mw: Mapped[float] = mapped_column(Numeric(10, 2), nullable = False)
    description: Mapped[str | None] = mapped_column(Text)