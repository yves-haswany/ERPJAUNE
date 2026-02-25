from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.routers import auth, products

app = FastAPI(title="Multi-Tenant Retail ERP")

# ✅ CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routers
app.include_router(auth.router)
app.include_router(products.router)


# ✅ Root route
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>ERP Jaune</title>
        </head>
        <body>
            <h1>Welcome to ERP Jaune</h1>
            <p>The application is running successfully.</p>
            <a href="/docs">Go to API Documentation</a>
        </body>
    </html>
    """