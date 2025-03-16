from fastapi import FastAPI
from contextlib import asynccontextmanager
from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise

DATABASE_URL = "postgres://postgres:postgres@db:5432/postgres"

class Item(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    value = fields.IntField()
    description = fields.TextField()

    class Meta:
        table = "item"

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(db_url=DATABASE_URL, modules={"models": ["main"]})
    yield  
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

@app.get("/async/")
async def aeasy():
    count = await Item.filter(value__gt=500).count()
    return {"count": count}

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["main"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
