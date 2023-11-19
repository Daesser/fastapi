from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote

#Uncomment for sqlalchemy binding: Note: No auto-update on column. Tables need to be recreated
#models.Base.metadata.create_all(bind=engine)

#Alembic: In alembic/env.py file add "target_metadata = Base.metadata". Run alembic revision --autogenerate -m "auto create tables" to auto create tables in data base
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}



