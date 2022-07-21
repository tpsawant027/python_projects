# Program to find vaccine appointments by Pincode
import requests
import csv


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


# function to find vaccine centres by pincode and date
def find_by_pin(pincode,date_):
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
    return filtered_response_lst