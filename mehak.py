import json

python_data={   
    'name':'mehak',
    'quali':'m.tech',
    'city_Bhopal': True,  
}
print(json.dumps(python_data))


python='{"name": "mehak","quali": "m.tech","city_Bhopal": true}'
print(json.loads(python))