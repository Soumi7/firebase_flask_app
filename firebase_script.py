import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
#cred = credentials.Certificate("/mnt/c/Users/soumi/Downloads/fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
#project_id = "fir-flasksofia"

#cred = credentials.Certificate("/mnt/c/Users/soumi/Downloads/fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")

cred = credentials.Certificate("fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

doc_ref = db.collection(u'test').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})