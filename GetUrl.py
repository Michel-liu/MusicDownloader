import requests
import os
from random import random
from time import time
import json

def search_song(self, key_word, page=1, num=20):
        ''' 根据关键词查找歌曲 '''
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        url += '?new_json=1&aggr=1&cr=1&flag_qc=0&p=%d&n=%d&w=%s' \
            % (page, num, key_word)
        rst = requests.get(url)
        data_list = json.loads(rst.text[9:-1])['data']['song']['list']
        song_list = []
        for line in data_list:
            item={}
            media_mid=line['file']['media_mid']
            item['title'] = line['title']
            item['singer'] = line['singer']
            item['filename'] = "C400%s.m4a" % media_mid
            item['song_mid'] = line['mid']
            item['album'] = line['album']

            guid = int(random() * 2147483647) * int(time() * 1000) % 10000000000
            item['guid']=guid
            song_list.append(item)
            # song = Song(media_mid=media_mid, song_mid=song_mid,
            #             title=title, singer=singer, album=album, data=line)
            # song_list.append(song)
        return song_list[0]

def get_vkey(song_list):
    song_list_vkey=[]
    for item in song_list:
        url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?'
        url += 'format=json&platform=yqq&cid=205361747&songmid=%s&filename=%s&guid=%s' \
            % (item['song_mid'], item['filename'], item['guid'])
        rst = requests.get(url)
        vkey = json.loads(rst.text)['data']['items'][0]['vkey']
        item['vkey']=vkey
        song_list.append(item)
    return song_list_vkey

def get_music_url(song_list_vkey):
    song_url_list=[]
    for item in song_list_vkey:
        url = 'http://dl.stream.qqmusic.qq.com/%s?' % item['filename']
        music_url = url + 'vkey=%s&guid=%s&fromtag=30' % (item['vkey'], item['guid'])
        item['music_url']=music_url
        song_url_list.append(item)
    return song_url_list

def SaveFile(song_url_list):
    with open('index.txt','w+') as f:
        for item in song_url_list:
            f.write(item['title']+'_'+item['singer']+'|'+item['music_url'])
    


