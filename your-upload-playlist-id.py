from googleapiclient.discovery import build


#enter your youtube channel id here
channel_id = ''

#enter your youtube api key here
youtube_api_key = ""

#sending the api key to google
youtube = build('youtube', 'v3', developerKey= youtube_api_key)

#sending a request to youtube for the channel upload playlist id
request = youtube.channels().list(
    part = 'contentDetails',
    id = channel_id
)

response = request.execute()

playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

print(playlist_id)

#now copy the id and paste it to main.py
