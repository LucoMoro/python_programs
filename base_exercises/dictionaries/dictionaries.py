customer = {
    "name": "LucoMoro",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("name"))
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"
print(customer.get("birthdate", "Jan 1 1980")) 