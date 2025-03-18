
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
 
# Load CSV file
df = pd.read_csv('christmas_movies.csv', encoding='UTF-8')
df.columns = df.columns.str.upper()
print(df.info())
 
# Fill missing data
df.fillna({'TYPE' : 'Unidentified','DESCRIPTION' : 'No data','RATING': 'Not Rated', 'IMDB_RATING': 'Not Rated','RUNTIME' : 'No data','GENRE' : 'Unidentified','DIRECTOR' : 'No data','STARS' : 'No data' ,'RELEASE_YEAR': 'No Data', 'VOTES': 'Not Rated'}, inplace=True)
 
# Drop unnecessary columns
df.drop(columns=['META_SCORE', 'GROSS', 'IMG_SRC'], inplace=True)
#replace full stops with space in title as they are invalid for firebase
df['TITLE'] = df['TITLE'].str.replace('.',' ')
df['TITLE'] = df['TITLE'].str.replace('?',' ')
df['TITLE'] = df['TITLE'].str.replace('#',' ')
df.set_index('TITLE', inplace=True)
# Save cleaned data
df.to_csv('new_christmas.csv')
 
#f = open("new_christmas.csv","r")
print(df.info())
 
# Firebase initialization
cred = credentials.Certificate("lc-230625-firebase-adminsdk-fbsvc-63a70fc11d.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://lc-230625-default-rtdb.europe-west1.firebasedatabase.app/'
    })
 
# Convert DataFrame to dictionary
data_dict = df.T.to_dict()
 
# Upload data to Firebase
ref = db.reference('/')
print(data_dict)
ref.set(data_dict)

#for key, value in data_dict.items():
    #ref = db.reference('/'+key)
    #print('Title: ', key)
    #ref.update({key:value})
    
#ref.set(data_dict)




































