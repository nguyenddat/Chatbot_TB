from typing import * 

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.base import engine
from models.base import Base
from api import (
    chatbot
)

Base.metadata.create_all(bind=engine)

def get_application() -> FastAPI:
    application = FastAPI()
    
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(chatbot.router, prefix="/api/chat", tags=["chat"])
    return application


app = get_application()
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload = True)
