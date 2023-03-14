import json

with open("webcrwaling/test.json",'r',encoding='utf-8') as file:
    json_data = json.load(file)
    for i in range(4):
        print(f"{json_data['name'][i]}\t\t{json_data['price'][i]}\t\t{json_data['review'][i]}\t\t")