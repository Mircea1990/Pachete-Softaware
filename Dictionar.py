thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)
thisdict.update({"year": 2020})
print(thisdict)
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("model")
print(thisdict)