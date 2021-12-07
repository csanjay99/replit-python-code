import requests
import json
import pandas as pd

limit = 10
pincodes = []

def makeObjectFromApi(obj) :
  
  temp_obj = {}
  temp_obj['officename'] = obj['officename']
  temp_obj['pincode'] = obj['pincode']
  temp_obj['divisionname'] = obj['divisionname']
  temp_obj['regionname'] = obj['regionname']
  temp_obj['circlename'] = obj['circlename']
  temp_obj['taluka'] = obj['taluk']
  temp_obj['districtname'] = obj['districtname']
  temp_obj['statename'] = obj['statename']
  return temp_obj

def requestData(i) :
  url1 = 'https://api.data.gov.in/resource/6176ee09-3d56-4a3b-8115-21841576b2f6?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset='
  url2 = str(limit*i)
  url = url1 + url2
  response = requests.get(url)
  response = response.json()
  #text = json.dumps(response, indent=2)
  #print(response['records'])
  records = response['records']
  #print(records)

  for obj in records:
    pincodes.append(makeObjectFromApi(obj))
'''
for i in range(5000):
  requestData(i)
  if i==1000 :
    print(i)
'''

print('total number of postal regions = '+str(len(pincodes)))

pincode_df = pd.DataFrame(data=pincodes)
#print(pincode_df)
pincode_df.to_excel("pincodes1.xlsx", engine="xlsxwriter")

