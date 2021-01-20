# NinjaShare

A simple bot to share your latest YouTube video as a post on Facebook.


## Overview
This bot was created for lazy people like me who forgets to share their YouTube videos on the channels Facebook page. This bot was created using Facebook's GraphAPI and YouTube Data API v3. It checks every 30 minutes if there is a new video on the specified channel (you can also change the time if you like). If there is a new video on the specified channel then it will autometiacally post on Facebook, latest video's title, desciption and link. You can also deploy this to heroku to make it run 24/7 I have included the "Procfile" for heroku.

## How to use
To use this first be sure that you have the latest version of python3. Then,

Install all the dependencies using this command:
```
$ pip install -r requirements.txt
```

Running the file:
>If you are not gonna deploy this bot to heroku delete the "Procfile", "runtime.txt", "requirements.txt".

Copy your YouTube channel id, YouTube api key and Facebook GraphAPI access token and paste them on the main.py in the specified fields. To get your YouTube upload playlist id, copy the channel id  and paste it in your-upload-playlist-id.py in the specified field and run the program. It will return your channel's upload playlist id. Now copy this id and paste it in the main.py file in the specified field. If you don't want your last YouTube video to be shared change the "pre_title" variable with th exact copy of your last video title. Run the code. If you post any YouTube video now it will autometically share it to your Facebook page.
It will be best if you upload it to any cloud platform (like Heroku) and run it 24/7.

>If you don't know how you can get the Youtube channel id, Youtube api key and Facebook GraphAPI token , watch [this](https://www.youtube.com) video where I fully explained it.


## Contributors
- Thanks to Shadeed Ur Rahman Sreyash for helping me with this project.
