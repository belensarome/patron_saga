from app import db
from app.models import Stock
from app.repositories import StockRepository
from datetime import datetime
from app import cache
from threading import Lock

repository = StockRepository()
lock = Lock()


class StockService:
    
    def retirar(self, stock: Stock) -> Stock:
        result = None
        if stock is not None:
            stock.fecha_transaccion = stock.fecha_transaccion if stock.fecha_transaccion is not None else datetime.now()
            stock.entrada_salida = -1 # Salida de Producto
            with lock:
                if cache.get('en_uso'):
                    raise ValueError("Otra operación está en curso. Intenta nuevamente.")
                if (repository.get_stock(stock.producto) - stock.cantidad) < 0:
                    raise ValueError("stock insuficiente.")
                cache.set('en_uso', True)
                result = repository.save(stock)
                cache.set('en_uso', False)
                cache.set(f'stock_{stock.id}', result, timeout=60)
        return result

    def ingresar(self, stock: Stock) -> Stock:
        result = None
        if stock is not None:
            stock.fecha_transaccion = stock.fecha_transaccion if stock.fecha_transaccion is not None else datetime.now()
            stock.entrada_salida = 1 # Entrada de Producto
            result = repository.save(stock)
            cache.set(f'stock_{stock.id}', result, timeout=60)
        return result
    
    def consultar_stock(self, producto_id: int) -> int:
        cantidad = repository.get_stock(producto_id)
        #cache.set(f'cantidad_{producto_id}', cantidad, timeout=5)
        return cantidad 

    

    