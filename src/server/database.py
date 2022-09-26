# CONEXÃO COM BANCO DE DADOS

from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class DataBase:
    client: AsyncIOMotorClient = None
    database_uri = ""
    users_collection = None # VARIÁVEIS PARA ACESSAR AS COLEÇÕES
    address_collection = None
    product_collection = None
    order_collection = None
    order_items_collection = None

db = DataBase()

async def connect_db(): # CONEXÃO COM O BANCO
    # conexao mongo, com no máximo 10 conexões async
    db.client = AsyncIOMotorClient(
        db.database_uri,
        maxPoolSize=10, # QUANTIDADE DE CONEXÕES ASSINCRONAS QUE VOU PERMITIR
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    db.users_collection = db.client.shopping_cart.users # CHAMANDO AS COLEÇÕES
    db.address_collection = db.client.shopping_cart.address
    db.product_collection = db.client.shopping_cart.products
    db.order_collection = db.client.shopping_cart.orders
    db.order_items_collection = db.client.shopping_cart.order_items

async def disconnect_db(): # FECHAR CONEXÃO COM O BANCO
    db.client.close()
