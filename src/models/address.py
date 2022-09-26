from bson.objectid import ObjectId

async def create_address(address_collection, address):
	try:
		address_user = await get_address_by_email_user(address_collection, address["user"]["email"])
		
		if not address_user:
			result = await address_collection.insert_one(address)
			return await get_address_by_email_user(address_collection, address["user"]["email"])
		else:
			filter = {"_id" : address_user[0]["_id"]}
			new_value = { "$addToSet": {
				"address": address["address"][0]
				}
			}

			await address_collection.update_one(filter, new_value)
			return await get_address_by_email_user(address_collection, address["user"]["email"])

	except Exception as e:
		print(f'create_address.error: {e}')


async def get_address_by_email_user(address_collection, email):
	try:
		address_cursor =  address_collection.aggregate([
			{
				"$match":{ "user.email": email}
			}
		])
		return await address_cursor.to_list(1)

	except Exception as e:
		print(f'get_address.error: {e}')


async def delete_address(address_collection, address_id):
	try:
		address = await address_collection.delete_one(
			{'_id': address_id}
		)
		if address.deleted_count:
			return {'status': 'Address deleted'}
	except Exception as e:
		print(f'delete_address.error: {e}')
