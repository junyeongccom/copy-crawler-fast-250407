# crawler/main.py

from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.app_router import router as app_router

app = FastAPI()

app.include_router(app_router)


@app.get(path="/")
async def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 크롤러님 환영합니다</h1>
    <h2>{current_time}</h2>
</div>
</body>
""")
