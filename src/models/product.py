async def create_product(product_collection, product):
      try:
            product_result = await product_collection.insert_one(product)
            
            if product_result.inserted_id:
                  return await get_product(product_collection, product["code"])
      except Exception as e:
            print(f'create_product.error:{e}')
            
            
async def get_product(product_collection, code):
      try:
            data = await product_collection.find_one({'code': code})
            if data:
                  return data
      except Exception as e:
            print(f'get_product.error:{e}')
            
async def get_products(product_collection, skip, limit):
    try:
        product_cursor = product_collection.find().skip(int(skip)).limit(int(limit))
        products = await product_cursor.to_list(length=int(limit))
        return products

    except Exception as e:
        print(f'get_users.error: {e}')

async def delete_product(product_collection, product_id):  
    try:
        product = await product_collection.delete_one(
            {'_id': product_id}
        )
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')