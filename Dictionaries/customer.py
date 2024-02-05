# Key-value pairs
customer = {
    "name": "Brian Ngoya",
    "age": 22,
    "is_verified": True
}

print(customer["name"]) # Returns the value of the key name
customer["name"] = "Brian Ngoyarez"
print(customer.get("birthdate", "Jan 1, 1980")) # Returns none which indicates the absence of a key. Does not return the KeyError message