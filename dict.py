import functions

Dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(Dict.values())
print(Dict.items())
print(Dict.keys())

data_types = [1, "adam", "1", {"nick": 22}, ["hello World!"]]

print(data_types[3].values())

if data_types[0] == 2:
    print("yes")
else:
    print("nope")
    
print(functions.counting())