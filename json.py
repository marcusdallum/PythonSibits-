import json
import os

filename = "/newjson.json"

#create new json file

newjson = {'Key 1' : {'Key 1.2:'Hello World'}}
    print(newjson)
    jsonfile = json.dumps(newjson)
    f = open(filename, 'a')
    f.write(jsonfile)
    f.close

#update a json, load the data to dict, then save over the top

f = open(filename, 'a')
json_dict = json.load(f)
f.close()
# this will update the original data
json_dict["Key 1"]['Key 1.3'] =  'data'	
f = open(a , 'w')
jsonfile = json.dumps(json_dict)
print(jsonfile)
f.write(jsonfile)
f.close()
