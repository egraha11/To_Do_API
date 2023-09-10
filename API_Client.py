import requests
import json


url = 'http://127.0.0.1:5000'


#Test Put
task_id = 1

entry = {"Desc": "Clean", "Importance": 2}

response = requests.put(url + "/id/" + str(task_id), data= entry)

print(response.status_code)
print(json.loads(response.content))






#Test GET
response_2 = requests.get(url + "/id/" + str(id))

print(response_2.status_code)
print(json.loads(response_2.content))


#Test Patch
patch_id = 1

entry_2 = json.dumps({"Desc": "Grocery Shop", "Importance": 1})

response_3 = requests.patch(url + '/id/' + str(patch_id), data = entry_2)

print(response_3.status_code)
print(json.loads(response_3.content))

#Test Delete
delete_id = 1

response4 = requests.delete(url + '/id/' + str(delete_id))

print(response_3.status_code)
print(json.loads(response_3.content))