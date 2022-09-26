from src.models.address import (
    create_address,
    get_address_by_email_user,
    delete_address)

from bson.objectid import ObjectId

from src.server.database import connect_db, db, disconnect_db


async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    address_collection = db.address_collection

    delete_id = ObjectId("6330a7786d279d8b6f8153de")
    
    address =  {
        "user": {
            "_id" : ObjectId("00000000000000"),
            "email" : "ludomagalu12@gmail.com",
            "password" : "213sd312re3",
            "is_active" : True,
            "is_admin" : False    
        },
        "address": [
           {
                "street" : "Rua xx e Sete, Numero 3333",
                "cep" : "8465312",
                "district" : "São Paulo",
                "city" : "São Paulo",
                "state" : "São Paulo",
                "is_delivery" : True
            } 
        ]
    }

    if option == '1':
        new_address = await create_address(address_collection, address)
        print(new_address)
        
    elif option == '2':
        address = await get_address_by_email_user(address_collection, address["user"]["email"])
        print(address)
            
    elif option == '3':
        result = await delete_address(
            address_collection,
            delete_id
        )

        print(result)
        
    await disconnect_db()
        