dict = {"name":"Bob", "ref":"Pyton", "sys":"Win"}
print("Dictionary: ", dict)

print("\nReference:", dict["ref"])
print("\nKeys:", dict.keys())

del dict["name"]
dict["user"] = "Tom"
print("\nDictionary:", dict)

print("\nls There A name Key?:", "name" in dict)