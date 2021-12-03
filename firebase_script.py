from __future__ import unicode_literals
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import os
import mux_python

os.environ['GRPC_DNS_RESOLVER'] = 'native'
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

cred = credentials.Certificate("fir-flasksofia-firebase-adminsdk-zq0sm-c1b8842fd6.json")
firebase_admin.initialize_app(cred,{
    'storageBucket': 'fir-flasksofia.appspot.com' # GET BUCKET NAME
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
    print("This is the",pose['title'],"pose. Do you want to update the details of this pose? Then, Press 1. Else, press 0")
    f = input()
    if f:
        for field in pose:
            print(field,"--------------",pose[field])
            update = input("Press 1 to Update this field. Else press 0.")
            if update == '0':
                pass
            else :
                data_input = input()
                if field == "video_url":
                    # upload the file from path to firebase storage
                    # get the cached mux url
                    # pass url to data_input
                    blob = bucket.blob(data_input)
                    blob.upload_from_filename(data_input)
                    blob.make_public()
                    print(blob.public_url)
                    video_storage_url = blob.public_url

                    # MUX

                    assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))
                    input_settings = [mux_python.InputSettings(url=video_storage_url)]
                    create_asset_request = mux_python.CreateAssetRequest(input=input_settings)
                    create_asset_response = assets_api.create_asset(create_asset_request)
                    # https://docs.mux.com/guides/video/stream-video-files
                    PLAYBACK_ID = create_asset_response['data']['playback_ids'][id]
                    video_mux_url = "https://stream.mux.com/"+PLAYBACK_ID+".m3u8"

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
