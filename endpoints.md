curl -X POST -F 'username=your_username' -F 'password=your_password' http://api:8000/api-token-auth/
used to retrieve the auth token 

curl -X GET -H 'Authorization: Token your_token' http://api:8000/item/
used to retrieve all items 

curl -X GET -H 'Authorization: Token your_token' http://api:8000/item/**your_item_uuid**/
used to retrieve a single item 

curl -X GET -H 'Authorization: Token your_token' http://api:8000/order/
used to retrieve all orders 

curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Token your_token' -d '{"item": "your_item_uuid", "quantity": "1"}'
used to place an order for an item 

curl -X GET -H 'Authorization: Token your_token' http://api:8000/order/**your_order_uuid**/
used to get the order 

curl -X POST -H "Content-type: application/json" -d '{"name": "Test Test", "message": "test", "email":"test@testdjango.com"}'
used to create a contact request

