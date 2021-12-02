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

# ref = db.reference('/')

# # Read the data at the posts reference (this is a blocking operation)
# print(ref.get())

# https://firebase.google.com/docs/database/admin/retrieve-data

tracks = db.collection(u'sofia').document(u'test').collection(u'tracks')

track = input("Enter the track")

print("printing track")
trackname = f'{track}'

print(trackname)
# print(str(tracks.document(str(trackname).decode('utf8')).collection(u'poses')))



get_bal = tracks.document(trackname).collection(u'poses').get()
print(get_bal[0])

bal = u'{}'.format(get_bal[0].to_dict())
bal2 = get_bal[0].to_dict()
print("------------------------")
print(bal)
print("bal2",bal2)
print("-----------------")
print(type(bal))
print(type(bal2))
for k in bal2.keys():
    print(k)
    print(bal2[k])

# bal = u'{}'.format(get_bal.to_dict())
# print(bal['fff'])

# ref = db.reference("/sofia/test/tracks/beginners/")
# print(ref.get())



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


