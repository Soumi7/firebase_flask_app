import firebase_admin
from firebase_admin import credentials, firestore
databaseURL = {'databaseURL': "https://fir-flasksofia.firebaseio.com"}
cred = credentials.Certificate("/mnt/c/Users/soumi/Downloads/fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
firebase_admin.initialize_app(cred, databaseURL)
db = firestore.client()
for k in db.collection('items').get():
    print(k)