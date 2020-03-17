from sense_hat import SenseHat
from firebase_admin import credentials, firestore
import firebase_admin
import time

COLLECTION = 'raspberry'
DOCUMENT = 'sense-data'

cred = credentials.Certificate("./config/firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)

sense = SenseHat()

def update_sensor_data():
    while True:
        sensor_dict = {
            'sensor': {
                u'pressure' : sense.get_pressure(),
                u'temperature' : sense.get_temperature()
            }
        }

        sensor_data = sensor_dict['sensor']

        pi_ref.set(sensor_dict)

        # Every 5 minutes
        time.sleep(60 * 5)

update_sensor_data()