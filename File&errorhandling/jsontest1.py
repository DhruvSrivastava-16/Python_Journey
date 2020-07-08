
import json
'''
with open("data1.json","r") as file:
    d=json.load(file)
    print(d)
    '''
s={
 "name":"Mumma",
 "School":"RGC",
 "Age": 52,
 "Marks": [10,10]
 }
    
with open("data2.json","w") as file:
    json.dump(s,file)
   