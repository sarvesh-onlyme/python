import urllib as u
import json
from threading import Timer
import os

##Variables##
user_access_token = None
userid = None
data = None
online = {"active": [], "idle": []}
new_active = []
new_deactive = []
prev_active = []

####

##Load User Data##
f = open("info.txt", 'r')
data = f.read()
f.close()
data = json.loads(data)


def get_extended_token():
    f = open('sys.txt', 'r')
    token = f.read()
    f.close()
    if token:
        user_access_token = token
    else:
        params = u.urlencode({
        "fb_exchange_token":data['access_token'],
        "grant_type" : "fb_exchange_token",
        "client_id" : data['app_id'],
        "client_secret" : data['app_secret']
        })
        access_token = u.urlopen("https://graph.facebook.com/oauth/access_token?%s" %params)
        a = access_token.read()
        user_access_token = a[a.index('=')+1:a.index('&')]
        f = open('sys.txt', 'w')
        f.write(user_access_token)
        f.close()
    return user_access_token


def get_userid(username):
    uid = u.urlopen("https://graph.facebook.com/" + username + "?fields=id,name").read()
    uid = json.loads(uid)
    return uid['id']


def get_online_friends():
    params = u.urlencode({
        "q" : "SELECT username, name, online_presence FROM user WHERE online_presence IN ('active', 'idle') AND uid IN (SELECT uid2 FROM friend WHERE uid1 = " + userid + ")",
        "access_token" : user_access_token
    })
    global prev_active

    def iterate():
        list = u.urlopen("https://graph.facebook.com/fql?%s" % params)
        ol = list.read()
        ol = json.loads(ol)['data']
        prev_active = online['active']
        online['active'] = [[i['name'], i['username']] for i in ol if i['online_presence'] == 'active']
	online['idle'] = [[i['name'], i['username']] for i in ol if i['online_presence'] == 'idle']
        print 'online-->', [i[0] for i in online['active']]
	print 'idle---->', [i[0] for i in online['idle']]
        new_active = [i for i in online['active'] if i not in prev_active]
        new_deactive = [i for i in prev_active if i not in online['active']]
        friend_active = [i[0] for i in new_active if i[1] in data['friends_username']]
        friend_deactive = [i[0] for i in new_deactive if i[1] not in data['friends_username']]
        if friend_active.__len__():
            os.system("mplayer online.mp3")
            print "Newly Online Friends-->", friend_active
        if friend_deactive.__len__():
            print "friends-offline", friend_deactive

    set_Interval(iterate, 10)

def set_Interval(func, sec):
    def func_wrapper():
        set_Interval(func, sec)
        func()
    t = Timer(sec, func_wrapper)
    t.start()
    return t

if __name__ == "__main__":
    userid = get_userid(data['username'])
    user_access_token = get_extended_token()
    get_online_friends()

