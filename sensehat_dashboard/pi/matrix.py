from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, firestore
import time

# constants
COLLECTION = 'raspberry'
DOCUMENT = 'dashboard'

cred = credentials.Certificate("./config/key.json")
firebase_admin.initialize_app(cred)

# sensehat
sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.clear()

def update_sensehat(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        doc_readable = doc.to_dict()
        
        sensehat_color = doc_readable['matrix']['color']['value']
        sense.clear(convert_hex_to_rgb(sensehat_color))

def convert_hex_to_rgb(hex_color):
    start = 0
    end = 2
    rgb_color = []

    while end < 7:
        # get the 2 hexadecimal values that form 1 primairy color
        rgb_value = int(hex_color[start:end], 16)
        rgb_color.append(rgb_value)

        # increment the counter
        start = end
        end += 2

    # return the color array as string
    return tuple(rgb_color)
    

db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)
pi_watch = pi_ref.on_snapshot(update_sensehat)

while True:
    pass