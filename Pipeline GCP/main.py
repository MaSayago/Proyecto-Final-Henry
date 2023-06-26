import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery
import functions_framework
import ast
import datetime
import json

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    file_name = event['name']
    file_type = file_name.split('.')[-1]
    

    if '/' in file_name:
        main_folder = file_name.split('/')[0]
        last_folder = file_name.split('/')[1]

        if main_folder == 'Google Maps Json':
            dataset = 'googlefinal.'
            if file_name.split('/')[1] == 'reviews-filtrados':
              table_name = 'reviews-google'
              table_esquema = [
                {"name": "user_id", "type": "INTEGER", "mode": "NULLABLE"},
                {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                {"name": "time", "type": "DATETIME", "mode": "NULLABLE"},
                {"name": "rating", "type": "INTEGER", "mode": "NULLABLE"},
                {"name": "text", "type": "STRING", "mode": "NULLABLE"},
                {"name": "pics", "type": "STRING", "mode": "NULLABLE"},
                {"name": "resp", "type": "STRING", "mode": "NULLABLE"},
                {"name": "gmap_id", "type": "STRING", "mode": "NULLABLE"}]

            elif file_name.split('/')[1] == 'filtered_bars.json':
              table_name = 'metadata-sitios'
              table_esquema = [
                {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'address', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'gmap_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'description', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'latitude', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'longitude', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'category', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'avg_rating', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'num_of_reviews', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'price', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'hours', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'MISC', 'type': 'RECORD', 'mode': 'NULLABLE'},
                {'name': 'relative_results', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'url', 'type': 'STRING', 'mode': 'NULLABLE'}]
            else: 
                table_name = file_name.split('.')[0].split('/')[1]
    

        if main_folder == 'Yelp json':
            dataset = 'yelpfinal.'
            if last_folder == "businesss_json.json":
                table_name = "business"
                table_esquema = [
                {"name": "business_id","type": "STRING", "mode": "NULLABLE" },
                {"name": "name","type": "STRING","mode": "NULLABLE"},
                {"name": "address", "type": "STRING", "mode": "NULLABLE"},
                {"name": "city","type": "STRING","mode": "NULLABLE"},
                {"name": "state","type": "STRING","mode": "NULLABLE"},
                { "name": "postal_code","type": "STRING","mode": "NULLABLE"},
                {"name": "latitude","type": "FLOAT","mode": "NULLABLE"},
                {"name": "longitude","type": "FLOAT","mode": "NULLABLE" },
                {"name": "stars","type": "FLOAT","mode": "NULLABLE" },
                {"name": "review_count","type": "INTEGER","mode": "NULLABLE"},
                {"name": "attributes","type": "STRING","mode": "NULLABLE"},
                {"name": "categories", "type": "STRING","mode": "NULLABLE" },
                {"name": "hours","type": "STRING","mode": "NULLABLE"}]
            elif last_folder == "checkin_json.json":
                table_name = "checkin"
                table_esquema = [
                    {'name': 'business_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                    {'name': 'date', 'type': 'STRING', 'mode': 'NULLABLE'}]
            elif last_folder == "reviews_filtered.json":
                table_name = "reviews-yelp"
                table_esquema = [
                {'name': 'review_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'user_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'business_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'stars', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'text', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'useful', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'funny', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'cool', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'date', 'type': 'DATETIME', 'mode': 'NULLABLE'}]
            elif last_folder == "tip_filtered.jsonl":
                table_name = "tips"
                table_esquema = [
                {'name': 'user_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'business_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'text', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'date', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                {'name': 'compliment_count', 'type': 'INTEGER', 'mode': 'NULLABLE'}]
            elif last_folder == "user_filtered.jsonl":
                table_name = "users"
                table_esquema = [
                {'name': 'user_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'review_count', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'yelping_since', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'useful', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'funny', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'cool', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'elite', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'friends', 'type': 'STRING', 'mode': 'NULLABLE'},
                {'name': 'fans', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'average_stars', 'type': 'FLOAT', 'mode': 'NULLABLE'},
                {'name': 'compliment_hot', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_more', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_profile', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_cute', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_list', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_note', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_plain', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_cool', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_funny', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_writer', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                {'name': 'compliment_photos', 'type': 'INTEGER', 'mode': 'NULLABLE'}]
            else:
                table_name = file_name.split('.')[0].split('/')[1]
                
          
    if file_type == 'json' or file_type == "jsonl":
        try:
            data = pd.read_json('gs://' + event['bucket'] + '/' + file_name)
        except ValueError as e:
            if 'Trailing data' in str(e):
                data = pd.read_json('gs://' + event['bucket'] + '/' + file_name, lines = True)
            else:
                print('Ocurrió un error cargando el archivo JSON:', e)

    if main_folder == 'Yelp json':
            df = pd.read_json('gs://' + event['bucket'] + '/' + 'business_filtered.json')
            business_ids = set(df['business_id'])
            
            if last_folder == "businesss_json.json":
                data.drop(columns=["is_open"], inplace=True)
                data[['attributes', 'categories', 'hours']] = data[['attributes', 'categories', 'hours']].astype(str)
                
            elif last_folder == "checkin_json.json":
                data = data[data['user_id'].isin(business_ids)]
  
            elif last_folder == "reviews_filtered.json":
                data = data[data['user_id'].isin(business_ids)]
                
            elif last_folder == "tip_filtered.jsonl":
                data = data[data['user_id'].isin(business_ids)]
                
            elif last_folder == "user_filtered.jsonl":
                data = data[data['user_id'].isin(business_ids)]
                data["yelping_since"] = data["yelping_since"].astype(str)
                
            else:
                pass
    
    if main_folder == 'Google Maps Json':
        with open('gs://' + event['bucket'] + '/' + 'filtered_bars.json', lines=True) as f:
            data = json.load(f)
            df_filtered = pd.DataFrame(data)
            gmap_id = df_filtered["gmap_id"]
            
            if 'review' in last_folder:
                data = last_folder[last_folder['gmap_id'].isin( gmap_id)]
                table_esquema= None
                data= data.astype(str)

            elif table_name == 'metadata-sitios':
                data = last_folder[last_folder['gmap_id'].isin(gmap_id)]
                table_esquema= None
                data= data.astype(str)
            else: 
                pass

    
    data.to_gbq(destination_table= dataset + table_name, 
                            project_id='proyectofinal-389013', 
                            table_schema= table_esquema ,
                            if_exists='append', progress_bar=False,  auth_local_webserver=False,  location='us-east1')