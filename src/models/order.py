async def create_order(orders_collection, order):
	try:
		address_user = await get_order_by_email_user(orders_collection, order["user"]["email"])
		
		if not address_user:
			result = await orders_collection.insert_one(order)
			return await get_order_by_email_user(orders_collection, order["user"]["email"])
	
		return await get_order_by_email_user(orders_collection, order["user"]["email"])

	except Exception as e:
		print(f'create_order.error: {e}')


async def get_order_by_email_user(orders_collection, email):
	try:
		orders_cursor =  orders_collection.aggregate([
			{
				"$match":{ "user.email": email}
			}
		])
		return await orders_cursor.to_list(1)

	except Exception as e:
		print(f'get_order.error: {e}')


async def delete_order(orders_collection, order_id):  
    try:
        order = await orders_collection.delete_one(
            {'_id': order_id}
        )
        if order.deleted_count:
            return {'status': 'Order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')

