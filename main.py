import json, requests

url = 'https://pottcounty.govbuilt.com/workflows/Invoke?token=CfDJ8K2SvNL_4s9PsSxPsU2Nf9mWQKTySoAs6gWwQK74eJgm6CnN2oS1ZpbcnkW6WehHDsj33gk-gchW_2Okcy4kSomEyMWlz5pEIQ4Y4DkCoiG3NUexbENshyZJ6Gd055RqlQERUC_d7ysrdtyjLPi7APksfWOtD6dMeqciEl-ACdUM4hhrctZWhZBe9Fszo0j5OOtW1U3oSk1hVlH5kI4xgUm5dZVc6lM0AvDyEVIctoae'

json_response = requests.get(url).json()
def create_json(data, comp):
    json_data = {}
        
    for k, v in data.items():
        print(f"{k}: {type(v)}")
        if v is None:
            json_data[k] = None
        else:
            if 'date' in str(k).lower():
                json_data[k] = 'date'
                if comp and comp.get(k) is None:
                    comp[k] = 'date'
            else:
                if comp and comp.get(k) is None:
                    comp[k] = type(v).__name__
                json_data[k] = type(v).__name__
    
    if not comp:
        return json_data
    return comp 

json_typing = {}

with open('PermitTypes.txt', 'w') as file:
    for obj in json_response:
        json_typing[obj['CaseType']] = create_json(obj, json_typing.get(obj['CaseType'], None))
        file.write(obj['CaseType'])
        file.write('\n') 
        
for key, obj in json_typing.items():
    for k, v in obj.items():
        if'date' in str(k).lower():
            json_typing[key][k] = "date"

with open('output.json', 'w') as json_file:
    json.dump(json_typing, json_file, indent=2)

