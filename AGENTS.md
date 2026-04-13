# AGENTS.md - Asset Manager Project

FastAPI inventory/asset management system with sales tracking for ecomsense.in

## Project Structure

```
src/
├── main.py           # FastAPI app, dashboard route
├── database.py       # SQLAlchemy models
├── routes/
│   ├── inventory.py # Batch/inventory CRUD, photo uploads
│   ├── asset.py     # Fixed assets (tools)
│   └── sales.py     # Sales, ledger, payment tracking
├── templates/        # Jinja2 HTML templates
└── static/          # CSS, JS, inventory_photos/
data/
└── business.db       # SQLite database
```

## All Paths Are Relative

Code uses relative paths - works on both local and server:
- DB: `sqlite:///data/business.db`
- Templates: `templates/`
- Static: `static/`
- Uploads: `static/inventory_photos/`

## Server Info

- SSH: `carrierc@ecomsense.in`
- Project: `/var/www/ecomsense.in/`
- Service: `ecomsense-in.service`
- Domain: ecomsense.in

## Deployment (sync from local)

```bash
# Local to server sync
scp -o StrictHostKeyChecking=no -r src/* carrierc@ecomsense.in:/var/www/ecomsense.in/
scp -o StrictHostKeyChecking=no templates/* carrierc@ecomsense.in:/var/www/ecomsense.in/templates/
scp -o StrictHostKeyChecking=no static/* carrierc@ecomsense.in:/var/www/ecomsense.in/static/

# Restart service
ssh carrierc@ecomsense.in "sudo systemctl restart ecomsense-in"
```

## Git Commits

- `97edc0c` - add AGENTS.md with deployment notes
- `c2e7321` - use relative db path for server compatibility

## Quick Commands

```bash
# Run locally
cd src && python -m uvicorn main:app --reload

# SSH to server
ssh -o StrictHostKeyChecking=no carrierc@ecomsense.in

# View server logs
ssh -o StrictHostKeyChecking=no carrierc@ecomsense.in "sudo journalctl -u ecomsense-in -f"

# Restart server
ssh -o StrictHostKeyChecking=no carrierc@ecomsense.in "sudo systemctl restart ecomsense-in"
```

## Package Versions (Python 3.13)

```
fastapi==0.100.0
starlette==0.27.0
jinja2==3.1.2
uvicorn==0.23.0
sqlalchemy
python-multipart
```

## Key Features

- **Dashboard** (`/`): Net worth calculation, stock value, receivables
- **Batches** (`/batch`): Group inventory by supplier
- **Inventory** (`/add-items/{id}`, `/edit-item/{id}`, `/all-items`): Full CRUD with photo uploads
- **Assets** (`/assets-list`): Fixed assets/tools tracking
- **Sales** (`/sales`): Process sales with customer selection
- **Ledger** (`/ledger`): Track pending payments
