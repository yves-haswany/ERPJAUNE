from fastapi import FastAPI
from app.routers import auth, products

app = FastAPI(title="Multi-Tenant Retail ERP")

app.include_router(auth.router)
app.include_router(products.router)
