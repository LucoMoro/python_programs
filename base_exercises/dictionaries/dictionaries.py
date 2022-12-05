customer = {
    "name": "LucoMoro",
    "age": 30,
    "is_verified": True
}

print(customer["name"]) #if "name" does not exits we get an error
print(customer.get("name")) #if "name" does not exits we don't get an error
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"
print(customer.get("birthdate", "Jan 1 1980")) 