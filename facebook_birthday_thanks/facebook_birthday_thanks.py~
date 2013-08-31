#Like and comments on your B'day's wall post

import urllib as u
import json
import datetime as dt

#Data
Access_Token = "ACCESS_TOKEN"
BDay_Date = "B'Date"
Since_Date = BDay_Date
Untill_Date = BDay_Date
username = 'USERNAME'
comment_message = "YOUR COMMENT HERE!"

params = u.urlencode({"access_token": Access_Token, "since":Since_Date, "untill": Untill_Date})
like_param = u.urlencode({"access_token": Access_Token})
comment_param = u.urlencode({"access_token": Access_Token, "message":comment_message})
feeds = u.urlopen("https://graph.facebook.com/"+username+"/feed?%s" %params)
data = feeds.read()
data = json.loads(data)
print data['data'].__len__()
for d in data['data']:
    post_id = d['id']
    post_from = d['from']
    like_url = "https://graph.facebook.com/" + post_id + "/likes"
    like = u.urlopen(like_url, like_param)
    comment_url = "https://graph.facebook.com/" + post_id + "/comments"
    comment = u.urlopen(comment_url, comment_param)
    if like.read() == 'true':
        try:
            msg = d['message']
            print post_from['name'], "\t->", msg
        except Exception, e:
            print post_from['name'], "\t->", "No-message"
