from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import post_routes, product_routes, collection_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(post_routes.router)
app.include_router(product_routes.router)
app.include_router(collection_routes.router)