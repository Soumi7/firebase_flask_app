from __future__ import unicode_literals
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import os
os.environ['GRPC_DNS_RESOLVER'] = 'native'

cred = credentials.Certificate("fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
firebase_admin.initialize_app(cred,{
    'storageBucket': 'bucket_name'
})

db = firestore.client()
bucket = storage.bucket()

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
                    # upload the file from path to firebase storage
                    # get the cached mux url
                    # pass url to data_input
                    data_input = video_mux_url
                if field == "image":
                    # upload the img to firebase storage
                    # get the url
                    # pass img url to data_input
                    blob = bucket.blob(data_input)
                    blob.upload_from_filename(data_input)
                    blob.make_public()
                    print(blob.public_url)
                    image_url = blob.public_url
                    data_input = image_url
                pose_obj.document(pose['title']).update({field: data_input})


##########################################################
