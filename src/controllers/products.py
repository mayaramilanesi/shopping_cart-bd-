from src.models.product import (
    create_product,
    delete_product,
    get_products,
    get_product
)
from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    product_collection = db.product_collection

    product =  {
        "name": "Mesa de escritório 20",
        "description": "cadeira de madeira",
        "price": "300.00",
        "image": "hahaha",
        "code": 5495.0
    }

    if option == '1':
        product = await create_product(
            product_collection,
            product
        )
        print(product)
    elif option == '2': 
        product = await get_product(
            product_collection,
            product["code"]
        )
        print(product)
    elif option == '3': 
        product = await get_product(
            product_collection,
            product["code"]
        )

        result = await delete_product(
            product_collection,
            product["_id"]
        )
        print(result)
    elif option == '4':
        products = await get_products(
            product_collection,
            skip=0,
            limit=5
        )
        print(products)

    await disconnect_db()
