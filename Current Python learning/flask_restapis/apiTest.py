import json, requests, io, zipfile

headers = {
    'Authorization': 'Bearer F88pQWs8hoPzbeCg4xTGifDxxs1eKu',
    'X-PlayerUID': '9418fd52-baef-401c-a2b3-e6fe16d93596',
}

data = {
    'pipeline': 'animated_face',
    'pipeline_subtype': 'base/legacy',
    'name': 'haircuts test',
    'parameters': json.dumps({
        'haircuts': {
            'base': [
                'female_NewSea_J086f',
                'male_NewSea_J003m',
            ],
        },
    }),
}

files = {
    'photo': open('photo.jpg', 'rb'),
}

avatar = requests.post(
    'https://api.avatarsdk.com/avatars/',
    headers=headers, data=data, files=files,
).json()

print(avatar)
# avatar = requests.get(avatar['url'], headers=headers).json()
#
# haircuts_url = avatar['haircuts']
# haircuts = requests.get(haircuts_url, headers=headers).json()
#
# for haircut in haircuts:
#     identity = haircut['identity']
#
#     mesh_url = haircut['mesh']
#     mesh = requests.get(mesh_url, headers=headers)
#     with io.BytesIO(mesh.content) as zipmemory:
#         with zipfile.ZipFile(zipmemory) as archive:
#             archive.extractall()
#
#     texture_url = haircut['texture']
#     texture = requests.get(texture_url, headers=headers)
#     with open(identity + '.jpg', 'wb') as texture_file:
#         texture_file.write(texture.content)