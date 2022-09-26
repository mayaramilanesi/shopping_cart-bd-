from src.models.order import (
    create_order,
    delete_order)
from bson.objectid import ObjectId
from src.server.database import connect_db, db, disconnect_db


async def orders_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    orders_collection = db.order_collection

    order_id = ObjectId("0000000000000000")

    order =  {
            "user": {"_id" : ObjectId("000000000000000"),
                  "name" : "Maria",
                  "email" : "maria@gmail.com",
                  "password" : "213sd312re3",
                  "is_active" : True,
                  "is_admin" : False
            },
            "create": "maria@gmail.com",
            "address": ObjectId("0000000000000"),
            "authority":"Ok"  
    }

    if option == '1':
        new_order = await create_order(
            orders_collection,
            order
        )
        print(new_order)
        
    elif option == '2':
        result = await delete_order(
            orders_collection,
            order_id
        )
        print(result)

    await disconnect_db()