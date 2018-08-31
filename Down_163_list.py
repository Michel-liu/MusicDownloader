import requests
import re
import json
import os
import time
from random import choice

url = "https://music.163.com/weapi/v3/playlist/detail"
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
formdata = {
    'params':'F7GRNfKegJd1KXq4OVfll2AZgXkB+nZEWgc4ePKbvxz9swMTyERW82+vNA6DOuc/aM+fnikD/5+L9ihn1qCBq1tKxIRtmdpfPmtr5NTZUE3O98KIOGoqL00pqi0v3hMqYFCF1/EWgPQCzO3TP/mLs3jOlK5wKGyktF8SpEmJtgOOyz4acROxnYKwkEU0K8W9FLaef6Pgu/4QOJUpEmYM++8cmQ9ZL8SvFxYAhXHQ+9I=',
    'encSecKey':'b5b485cb61cb140a6265db1b8604717f836a0aa2b4da6d0b167c527fba33f0b362ce8934db5ca3a1957b33e5d93ff1daf718a3899f6ef3ead65da7cf8df0a194af871a9d945ccb5e740053d799fbf008b207ee57b9f553ffc4e5d639f1edbca4a92c8d1bf132fecd9ee48fb64c9cdf0cc75a2ec86029f7d9a4afa41e3355d995'
}

def getSongList():
    try:    
        response = requests.post(url, headers=header, data=formdata)
        content = None

        if response.status_code == requests.codes.ok:
            content = response.text

    except RequestException as e:
        print (e)
        return


    lists = json.loads(content)
    tracks = lists.get('playlist').get('tracks')
    name_list=[]
    for track in tracks:
        item={}
        item['name']=track.get('name')
        item['singer']=track.get('ar')[0]['name']
        name_list.append(item)
        print(item)
    return name_list

