import random
import requests
import string
import urllib


def get_random_tracks():
    #Get token from: https://developer.spotify.com/console/get-search-item/

    search_api_token = input("Paste token: ")
    wildcard = f'%{random.choice(string.ascii_lowercase)}%'
    query = urllib.parse.quote(wildcard)
    offset = random.randint(0, 2000)
    url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track"
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {search_api_token}"
        }
    )
    response_json = response.json()
    track_id = []
    for i in response_json['tracks']['items']:
        track_id.append(i['id'])

    return track_id

def add_tracks_to_library():
    #Get token from: https://developer.spotify.com/console/get-search-item/
    my_track_ids = get_random_tracks()
    print("my_track_ids", my_track_ids)
    api_token = input("Paste token: ")
    url = "https://api.spotify.com/v1/me/tracks/"
    response = requests.put(
        url,
        json={
            "ids": my_track_ids
        },
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_token}"
        },
    )
    if response.status_code in range(200, 299):
        print("Added 20 random tracks to library")
    else:
        print("Failed to add tracks to library")

add_tracks_to_library()
