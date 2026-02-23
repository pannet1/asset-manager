# main.py
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import func # Add this import

from database import engine, Base, get_db, Inventory, Asset
from routes import inventory, asset  # Import both routers

# Initialize Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Mount Static for Product Photos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Register Routers
app.include_router(inventory.router)
app.include_router(asset.router)


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    # 1. Inventory Stats (Excluding 'Sold')
    inventory_stats = db.query(
        func.count(Inventory.inventory_id).label("count"),
        func.sum(Inventory.purchase_price).label("total_cost")
    ).filter(Inventory.status != "Sold").first()

    # 2. Asset Stats
    asset_stats = db.query(
        func.count(Asset.id).label("count"),
        func.sum(Asset.cost).label("total_cost")
    ).first()

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "item_count": inventory_stats.count or 0,
        "stock_value": inventory_stats.total_cost or 0.0,
        "asset_count": asset_stats.count or 0,
        "asset_value": asset_stats.total_cost or 0.0
    })
