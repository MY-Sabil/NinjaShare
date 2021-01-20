import facebook
from googleapiclient.discovery import build
import time

#enter your youtube channel id and upload playlist id here (check your upload playlist id by running the second python file)
channel_id = ''
upload_playlist_id = ''

#enter your youtube api key here
youtube_api_key = ""

#enter your graph api access token here
fb_token = ""

#sending the api key to google
youtube = build('youtube', 'v3', developerKey= youtube_api_key)

#sending access token to graph api
fb = facebook.GraphAPI(access_token = fb_token)

#sending a request to youtube for uploads playlist info
video_info_request = youtube.playlistItems().list(
    part = 'snippet',
    playlistId = upload_playlist_id,
    maxResults = 1
)

#write your latest video title here if you don't want it to post your latest video
pre_title = "a"

while True:
    #executing the request
    response = video_info_request.execute()

    #get the video title, description and link from response
    video_title = response['items'][0]['snippet']['title']
    video_description = response['items'][0]['snippet']['description']
    video_link = "https://www.youtube.com/watch?v=" + response['items'][0]['snippet']['resourceId']['videoId']

    print(video_title + '\n\n'+ video_description + '\n\n' + video_link)

    #checking if the video title matches the pre_title if it matches it doesn't post
    if pre_title != video_title:
        #what to send on facebook post
        text = video_title + '\n\n'+ video_description + '\n\n' + video_link

        #sending the post request
        fb.put_object(parent_object='me', connection_name='feed', message= text)

        #changing the pre_title to new video title
        pre_title = video_title

    #wait for these seconds (you can enter your own gap time)
    time.sleep(1800)