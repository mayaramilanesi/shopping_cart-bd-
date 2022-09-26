from bson.objectid import ObjectId

async def create_order_item(order_items_collection, order_item):
	try:
		order_item_user = await get_order_item_by_email_user(order_items_collection, order_item["order"]["user"]["email"])
		if not order_item_user:
        
			await order_items_collection.insert_one(order_item)
			return await get_order_item_by_email_user(order_items_collection, order_item["order"]["user"]["email"])
		
		return await get_order_item_by_email_user(order_items_collection, order_item["order"]["user"]["email"])

	except Exception as e:
		print(f'create_order_item.error: {e}')


async def get_order_item_by_email_user(order_items_collection, email):
	try:
		order_item_cursor =  order_items_collection.aggregate([
			{
				"$match":{ "order.user.email": email}
			}
		])
		return await order_item_cursor.to_list(1)

	except Exception as e:
		print(f'get_address.error: {e}')


async def delete_order_item(order_items_collection, order_item_id):
      try:
            order_item_delete = await order_items_collection.delete_one({'_id': order_item_id})
            if order_item_delete.deleted_count:
                  return {'status': 'Order_item deleted'}
      except Exception as e:
        print(f'delete_order_item.error: {e}')
