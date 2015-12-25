#!/usr/bin/env python
__auther__ = 'xiao'

import re
import urllib2
import time
import json
import os

def download_img():
    url_temp = 'http://himawari8.nict.go.jp/img/D531106/latest.json'
    request_temp = urllib2.Request(url_temp)
    response_temp = urllib2.urlopen(request_temp)
    data_temp = response_temp.read()

    #decode json
    json_dec = json.JSONDecoder()
    json_result = json_dec.decode(data_temp)
    date_ = str(json_result['date'])

    # get date
    pattern = re.compile(r'(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+)')
    result = re.search(pattern, str(date_))
    if result:
        year = result.group(1)
        month = result.group(2)
        day = result.group(3)
        hour = result.group(4)
        minute = result.group(5)
        second = result.group(6)
    else:
        pass

    #Download picture
    # url = "http://res.cloudinary.com/dajkskdsp/image/upload/earth/%s/%s/%s/%s_%s_%s.png" \
    #     % (year, month, day, hour, minute, second)
    # url_2 = "https://res.cloudinary.com/dajkskdsp/image/upload/earth_live_photo_vps.png"
    

    path = os.path.join(os.getcwd(), '%s/%s/%s' %(year, month, day))
    filename = "earth_%s%s%s.png" % (hour, minute, second)
    picname = os.path.join(path, filename ) # pic path under the script dir

    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.exists( os.path.join(path, filename)):
        print "file exists! %s" % filename
        return False



    url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/%s/%s/%s/%s%s%s_0_0.png" \
        % (year, month, day, hour, minute, second)

    print url

    request_img = urllib2.Request(url)
    # request_img_2 = urllib2.Request(url_2)
    try:
        response_img = urllib2.urlopen(request_img)#
    except:
        print "Wating server download..."
        time.sleep(60)#delay for server update
        response_img = urllib2.urlopen(request_img)
    data_img = response_img.read()

    
    with open(picname, 'wb') as fp:
        fp.write(data_img)

    return picname

def set_wallpaper():
    # time.sleep(30)#wait for server download
    picpath = download_img()
    if picpath:
        os.system('gsettings set org.gnome.desktop.background picture-uri "file://%s"' % (picpath))
        os.system('gsettings set org.gnome.desktop.background picture-options "centered"')
        print 'Done.'

if __name__ == '__main__':
    while True:
        print "waiting..."
        set_wallpaper()
        time.sleep(60)
