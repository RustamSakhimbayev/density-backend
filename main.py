from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем запросы с фронтенда (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # пока разрешим всем
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    # Временные тестовые данные
    return [
        {"name": "DOGE 1M1", "value": 120, "color": "#f87171"},
        {"name": "XPL 1M", "value": 60, "color": "#a78bfa"},
        {"name": "XRP 3.9M", "value": 90, "color": "#60a5fa"}
    ]
