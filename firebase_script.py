from __future__ import unicode_literals
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
os.environ['GRPC_DNS_RESOLVER'] = 'native'

cred = credentials.Certificate("fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

tracks = db.collection(u'sofia').document(u'test').collection(u'tracks')

track = input("Enter the track")

print("printing track")
trackname = f'{track}'

pose_obj = tracks.document(trackname).collection(u'poses')
get_pose_obj = pose_obj.get()
########################################################

#########################################################

for i in range(len(get_pose_obj)):
    pose = get_pose_obj[i].to_dict()
    print("This is the",pose['title'],"track. Do you want to update the details of this pose? Then, Press 1. Else, press 0")
    f = input()
    if f:
        for field in pose:
            print(field,"--------------",pose[field])
            update = input("Press 1 to Update this field. Else press 0.")
            if update:
                data_input = input()
                if field == "video_url":
                    #upload the file from path to firebase storage
                    #get the cached mux url
                    video_mux_url = data_input
                pose_obj.document(pose['title']).update({field: data_input})


##########################################################

# to update
