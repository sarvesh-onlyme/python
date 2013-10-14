=====
This app will provide information about the friends online presence 
=====
Follow the steps:
1. Browse the folloing url, login to your facebook(if not already), provide access to app. Then finally it let you to error page,  from that page copy access_token's value and paste it to info.txt access_token field
https://www.facebook.com/dialog/oauth?client_id=160947267391742&redirect_uri=http://0.0.0.0:8000&display=popup&scope=friends_online_presence&response_type=token

2.Provide other information in info.txt

3.Now open terminal, cd to facebook_chat dir -> python facebook_chat.py
