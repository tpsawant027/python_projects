# Program to find vaccine appointments by Pincode
import requests
import csv
import pandas as pd
pincode_list = []
with open('pincode.csv') as pincode:
    pincode_dict = csv.DictReader(pincode)
    for row in pincode_dict:
        pincode_list.append(row['Pincode'])
pincode_list.sort()   

pincode = input("Enter pincode: ")
if pincode not in pincode_list:
    raise ValueError('Invalid Pincode')
date_ = input("Enter date (dd-mm-yyyy): ")

param = {"pincode": pincode, "date": date_} 
endpoint = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
response = requests.get(endpoint,params= param).json()
response_list = response['sessions']
filtered_response_lst = []
for ele in response_list:
    ele_dict = {
        'center name': ele['name'],
        'address': ele['address'],
        'fee_type': ele['fee_type']
    }
    filtered_response_lst.append(ele_dict)

# print(filtered_response_lst)

#constructing pandas dataframe
data_frame = pd.DataFrame(filtered_response_lst)
print(data_frame.to_markdown())
print(data_frame.to_string())