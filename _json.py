import json

mydict = {
    "name": "Mahadi hasan",
    "age" : 18,
    "number" : "01701902728",
    "student": True,
    "Job" : False,
    "roll"  : None,
}
typejs = json.dumps(mydict)
typepy = json.loads(typejs)

print(type(typejs))
print(type(typepy))