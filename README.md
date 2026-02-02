# FastAPI CRUD для электростанций

### Используемые библиотеки
+ fastapi
+ uvicorn
+ sqlalchemy
+ aiosqlite
+ alembic
+ pydantic

### Установка зависимостей
```pip install -r requirements.txt```

### База данных
Применение миграций:
```alembic upgrade head```

Создание новой миграции:
```alembic revision --autogenerate -m "Описание миграции"```

### Запуск приложения
```python -m uvicorn src.main:app --reload``` 

Приложение будет доступно по:
```http://127.0.0.1:8000``` или ```http://localhost:8000/```

Swagger UI:
```http://127.0.0.1:8000/docs```
