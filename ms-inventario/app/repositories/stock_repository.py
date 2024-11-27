from app import db
from app.models import Stock
from sqlalchemy.sql import func

class StockRepository:
    
    
    def save(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock
    
    
    def get_stock(self,  producto_id:int) -> int:
        result = db.session.query(func.sum(Stock.cantidad * Stock.entrada_salida)).filter(Stock.producto == int(producto_id)).scalar()
        return result

    