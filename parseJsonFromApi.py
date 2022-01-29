from urllib.request import urlopen
import json

url = "https://pdc.fedoraproject.org/rest_api/v1/product-versions/"
response = urlopen(url)

data_json = json.loads(response.read())

json_count = data_json['count']
print('api count total no of results: ' + str(json_count))  #counting how many dic are there inside 'results' in josn data

# json_active = data_json['results'][1]['name'][1]
# print(json_active)

list1 = []
for i in range(0,json_count):
    active_value = data_json['results'][i]['active']
    #active_value is bool
    if(active_value == True):
        name_value = data_json['results'][i]['name']
        list1.append(str(name_value))
#printing list of short string having the names of active FADORA releases
print(list1)

    