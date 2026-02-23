

# database.py
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

DATABASE_URL = "sqlite:///./data/business.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Batch(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    supplier_name = Column(String)
    date = Column(Date)
    items = relationship("Inventory", back_populates="batch")

class Inventory(Base):
    __tablename__ = "inventory"
    inventory_id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, ForeignKey('batches.id'))
    brand = Column(String)
    model = Column(String)
    serial = Column(String, unique=True)
    description_for_ecommerce = Column(String, nullable=True)
    purchase_price = Column(Float)
    total_expenses = Column(Float, default=0.0)
    intended_profit = Column(String)
    selling_price = Column(Float, nullable=True)
    status = Column(String, default="In-Stock")
    batch = relationship("Batch", back_populates="items")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()


# database.py additions
class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cost = Column(Float)
    purchase_date = Column(Date)
