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

# Retrieve a list of the top artists for a specific genre
def get_several_artist(token, genre, amount):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q=year%3A2025%20genre%3A{genre}&type=artist&limit={amount}'
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['artists']['items']
    return json_result

def get_songs_by_artists(token, artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US' # Need to have country
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result


def search_for_album(token, artist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q=remaster%2520track%3ADoxy%2520artist%3A{artist_name}&type=album' # limit makes this so it only search for 1
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['albums']['items']
    return json_result

def get_tracks_from_albums(token, album_id):
    url = f'https://api.spotify.com/v1/albums/{album_id}/tracks'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    response = json.loads(result.content)
    return response.get('items', [])

def get_tracks_using_id(token, song_id):
    url = f'https://api.spotify.com/v1/tracks/{song_id}'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result
    # return response.get('items', [])
    # return response.get('items', [])

def test():
    token = get_token()
    # fetch your albums
    album = search_for_album(token, 'Drake')
    album_id_list = [a['id'] for a in album]
    total_song_list = []
    total_track_list = []
    # for each album ID, fetch its tracks and extend your master list
    for album_id in album_id_list:
        # print(type(album_id))
        tracks = get_tracks_from_albums(token, album_id)
        total_song_list.extend(tracks)
    # now total_song_list contains every track dict from each album
    print(f"Found {len(total_song_list)} total tracks across {len(album_id_list)} albums")
    # print(total_song_list)
    for track_id in total_song_list:
        tracks = get_tracks_using_id(token, track_id['id'])
        print(tracks)
        total_track_list.extend(tracks)
    print('done')
# test()