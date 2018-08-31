import requests
import os
from random import random
from time import time
import json

def menu(self):
    print("0. 一键下载网易云音乐我喜欢歌单")
    print("1. 手动搜索并下载音乐")
    cho = input("请选择你想要的操作：")
    if cho == "0":
        pass
    if cho == "1":
        searchanddownload()


def searchanddownload():
    key_word = input("请输入你想搜索的歌曲名称：")
    l = search_song(key_word)
    f_l = choose_music(l)
    add_vkey = get_vkey(f_l)
    s_u_l = get_music_url(add_vkey)
    SaveFile(s_u_l)


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
        return song_list

def choose_music(song_list):
    index = 0
    for song in song_list:
        print(index+'. ', song['title']+" ", song['singer']+" ", song['album'])
        index++
    s = input("请选择你想要下载的音乐（多选请用空格隔开）：")
    choose = str(s).split(' ')
    res = []
    for i in choose:
        res.append(song_list[int(i)])
    return res


def get_vkey(song_list):
    song_list_vkey=[]
    for item in song_list:
        url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?'
        url += 'format=json&platform=yqq&cid=205361747&songmid=%s&filename=%s&guid=%s' \
            % (item['song_mid'], item['filename'], item['guid'])
        rst = requests.get(url)
        vkey = json.loads(rst.text)['data']['items'][0]['vkey']
        item['vkey']=vkey
        song_list_vkey.append(item)
    return song_list_vkey

def get_music_url(song_list_vkey):
    song_url_list=[]
    for item in song_list_vkey:
        url = 'http://dl.stream.qqmusic.qq.com/%s?' % item['filename']
        music_url = url + 'vkxey=%s&guid=%s&fromtag=30' % (item['vkey'], item['guid'])
        item['music_url']=music_url
        song_url_list.append(item)
    return song_url_list

def SaveFile(song_url_list):
    with open('index.txt','w+') as f:
        for item in song_url_list:
            f.write(item['title']+'_'+item['singer']+'|'+item['music_url'])
