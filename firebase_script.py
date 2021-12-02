from __future__ import unicode_literals
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
os.environ['GRPC_DNS_RESOLVER'] = 'native'

# Use the application default credentials
#cred = credentials.Certificate("/mnt/c/Users/soumi/Downloads/fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
#project_id = "fir-flasksofia"

#cred = credentials.Certificate("/mnt/c/Users/soumi/Downloads/fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")

def make_unicode(inp):
    if type(inp) != unicode:
        inp =  inp.decode('utf-8')
    return inp

cred = credentials.Certificate("fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

tracks = db.collection(u'sofia').document(u'test').collection(u'tracks')

track = input("Enter the track")

trackname = f'{track}'

#track_name = u'track_name'

print(trackname)
print(str(tracks.document(str(trackname).decode('utf8')).collection(u'poses')))

for k in tracks.document(track_name).collection(u'poses').get():
    print(k)


# frank_ref.set({
#     u'name': u'Frank',
#     u'favorites': {
#         u'food': u'Pizza',
#         u'color': u'Blue',
#         u'subject': u'Recess'
#     },
#     u'age': 12
# })

#Update age and favorite color
# frank_ref.update({
#     u'age': 13,
#     u'favorites.color': u'Red'
# })


