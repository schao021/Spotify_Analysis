from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# print(f'client id is {client_id}, client secret is {client_secret}')

# Authorization Token: Allows us to send request playlist/author information
def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization' : 'Basic ' + auth_base64, # Sending in and verifying authorization data
        'Content-Type' : 'application/x-www-form-urlencoded'
    }
    data = {"grant_type" : 'client_credentials'}
    result = post(url, headers=headers, data=data) # get json data
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    return {'Authorization' : 'Bearer ' + token}

def search_for_artist(token, artist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={artist_name}&type=artist&limit1' # limit makes this so it only search for 1
    
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['artists']['items']
    if len(json_result) == 0:
        print('No artist with this name exists')
        return None
    return json_result[0]
    
def get_songs_by_artists(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US' # Need to have country
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

token = get_token()
result = search_for_artist(token, 'Ken')
print(result['name'])
artist_id = result['id']
songs = get_songs_by_artists(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}") # the quotes have to be different from ' and "