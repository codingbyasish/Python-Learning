api_response = {
    "first_name": "Asish",
    "age": 29,
    "last_name": "Mallick",
    "email": "asishmallick@live.com",
    "password": "Test@4321",
    "commission": 10
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))

api_response["password"] = "Asish"
print(api_response)


for key, value in api_response.items():
    print(key, " => ", value)
