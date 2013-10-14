#Like and comments on your B'day's wall post

import urllib as u
import json
import datetime as dt

#Data
Access_Token = "CAACEdEose0cBAHqWmaY5eTq8S46MKzJ6SZBwNVayfHNGoZAO6aYoXLPtGwo3ZAXNyfoD3tNjacCFLxVi98sgNdxz5sVO5loXLcxTKlgvZBfdAjgov3cvMfrE2gdy8nCJjoSvmBZAaYW9mUUiJkcJfFh1xIX8MtXd3E4vFKAyboQbqgwN5fYYgD1QjPC2H1pYZD"
BDay_Date = "2013-09-01"
Since_Date = "2013-08-31"
Untill_Date = "2013-09-2"
username = 'Sarvesh1991'
comment_message = "YOUR COMMENT HERE!"

params = u.urlencode({"access_token": Access_Token, "since":Since_Date})
like_param = u.urlencode({"access_token": Access_Token})
comment_param = u.urlencode({"access_token": Access_Token, "message":comment_message})
feeds = u.urlopen("https://graph.facebook.com/"+username+"/feed?limit=100&%s" %params)
data = feeds.read()
data = json.loads(data)
print data['data'].__len__()
for d in data['data']:
    post_id = d['id']
    post_from = d['from']
    like_url = "https://graph.facebook.com/" + post_id + "/likes"
    like = u.urlopen(like_url, like_param)
    #comment_url = "https://graph.facebook.com/" + post_id + "/comments"
    #comment = u.urlopen(comment_url, comment_param)
    if like.read() == 'true':
        try:
            msg = d['message']
            print post_from['name'], "\t->", msg
        except Exception, e:
            print post_from['name'], "\t->", "No-message"
