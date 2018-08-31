# -*- coding: UTF-8 -*-
import os
import requests
from config import FileSaveDir
from config import headers


def get_index():
    info={}
    try:
        with open('index.txt','r') as f:            
            for line in f.readlines():
                list1=line.split('|')
                if len(list1) != 2:
                    continue
                if checkFilesExist(list1[0]+".mp3"):
                    print(list1[0]+".mp3"+"文件存在，已经跳过")
                    continue
                info[list1[0]]=list1[1]
                print(list1)
                print(list1[0]+'--索引添加成功')
        return info
    except Exception:
        print('获取索引失败！')
        return {}


def downloader(dict):
    for key,value in dict.items():
        try:
            response=requests.get(value[:-1],headers=headers)
            print(value[:-1])
            print(key+':'+str(response.status_code))
            with open(FileSaveDir + key+'.mp3','wb') as f1:
                f1.write(response.content)
            print(key+'.mp3 下载成功')
        except Exception:
            print("下载出错！")


def downloaderddirectly(dict):
    for item in dict:
        if checkFilesExist(item['save_title']+".mp3"):
            print(item['save_title']+".mp3"+"文件存在，已经跳过")
            continue
        try:
            response = requests.get(item['music_url'], headers=headers)
            print(item['save_title'] + ':' + str(response.status_code))
            with open(FileSaveDir + item['save_title'] + '.mp3', 'wb') as f1:
                f1.write(response.content)
            print(item['save_title'] + '.mp3 下载成功')
        except Exception:
            print("Error")


def checkFilesExist(fileName):
    return os.path.exists(FileSaveDir + fileName)

if __name__=='__main__':
    dict = get_index()
    downloader(dict)