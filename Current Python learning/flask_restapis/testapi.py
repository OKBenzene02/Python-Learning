import requests

BASE = "http://127.0.0.1:5000/"
headers = {"Content-Type": "application/json"}

# Sample data for Orders table
sample_data = [
    {'id': 1, "user_id": 1, "product": "Apple_iPhone_14 Pro Max_512GB_Gold,Oppo_f21s-pro 5g,vivo-Y72-5G-8-128-Black", "pincode": 500013, 'date': '18-06-2023',
     'timeslots': '10-12', "placedID": 123},
    {'id': 2, "user_id": 2, "product": "Apple_iPhone_14 Pro Max_512GB_Gold,Oppo_f21s-pro 5g,vivo-Y72-5G-8-128-Black", "pincode": 500013, 'date': '18-06-2023',
     'timeslots': '8-10', "placedID": 13434},

]

# Sample data for Slots table
slots_data = [
    {"slotid": 1, "product": "Apple_iPhone_14 Pro Max_512GB_Gold", "date": "D1", "timeslots": "8-10"
     , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 2, "product": "Apple_iPhone_14 Pro Max_512GB_Gold", "date": "D1", "timeslots": "10-12"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 3, "product": "Apple_iPhone_14 Pro Max_512GB_Gold", "date": "D1", "timeslots": "12-14"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 4, "product": "Oppo_f21s-pro 5g", "date": "D1", "timeslots": "10-12"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 5, "product": "Oppo_f21s-pro 5g", "date": "D1", "timeslots": "14-16"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 6, "product": "Oppo_f21s-pro 5g", "date": "D1", "timeslots": "16-18"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 7, "product": "vivo-Y72-5G-8-128-Black", "date": "D1", "timeslots": "10-12"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 8, "product": "vivo-Y72-5G-8-128-Black", "date": "D1", "timeslots": "13-15"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
    {"slotid": 9, "product": "vivo-Y72-5G-8-128-Black", "date": "D1", "timeslots": "17-19"
        , "available": "yes", 'avail_count': 3, 'orderone': None, 'ordertwo': None, 'orderthree': None},
]

# Sample data for Pincode table
pincode_details = [
    {"pinid": 1, "pincode1": 500001, "pincode2": 500010, "distance": 5, "zone": 1},
    {"pinid": 2, "pincode1": 500011, "pincode2": 500050, "distance": 10, "zone": 2},
    {"pinid": 3, "pincode1": 600001, "pincode2": 600010, "distance": 5, "zone": 3},
    {"pinid": 4, "pincode1": 600011, "pincode2": 600050, "distance": 10, "zone": 4},
]

# Adding slots data.......
for data in slots_data:
    response = requests.put(BASE + 'shopify/1/Apple_iPhone_14 Pro Max_512GB_Gold/500013', json=data,headers=headers)
    print(response.json())
input()

# Adding pincode data......
for data in pincode_details:
    response = requests.put(BASE + 'shopify/1/Apple_iPhone_14 Pro Max_512GB_Gold,Oppo_f21s-pro 5g,vivo-Y72-5G-8-128-Black/500007',
                            json=data,headers=headers)
    print(response.json())
input()

# Request for the product to get the required details......
response = requests.get(BASE + "shopify/2/Apple_iPhone_14 Pro Max_512GB_Gold,Oppo_f21s-pro 5g,vivo-Y72-5G-8-128-Black/500007",
                        headers=headers)
print(response.json())

# Placing the order after getting the request for the availability of the products......
for data in sample_data:
    response = requests.put(BASE +
                            f"shopify/{data['user_id']}/{data['product']}/{data['pincode']}",
                            json=data, headers=headers)
    print(response.json())


