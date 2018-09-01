import requests
import json
from requests import RequestException
from config import formdata
url = "https://music.163.com/weapi/v3/playlist/detail"
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}


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
    return name_list