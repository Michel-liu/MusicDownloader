#!/home/sun/annconda3/bin python3.6
# -*- coding: UTF-8 -*-
import os
import requests

fileSaveDir = '/Users/liuhuan/Music/'

def get_index():
    info={}
    try:
        with open('index.txt','r') as f:            
            for line in f.readlines():
                list1=line.split('|')
                if len(list1) != 2:
                    continue
                if checkFilesExist(list1[0]+".mp3"):
                    print("文件存在，已经跳过")
                    continue
                info[list1[0]]=list1[1]
                print(list1)
                print(list1[0]+'--索引添加成功')
        return info
    except Exception:
        print('获取索引失败！')
        return {}

def downloader(dict):
    headers={
        'Accept':'*/*',
        'Accept-Encoding':'identity;q=1, *;q=0',
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Range':'bytes=0-3870056',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Cookie':'pgv_pvi=7700441088; pt2gguin=o1965190613; RK=vgJt6SHwRW; ptcz=76f62a257754120641d25b3a9721c88358cf4507e35e939c910e57775af3db8c; pgv_pvid=5700638918; pgv_si=s5409642496; uin=o1965190613; skey=@Ss1CmNo3x; ptisp=cm',
        'Host':'dl.stream.qqmusic.qq.com',
        'Referer':'http://y.qq.com/',
        'Connection':'keep-alive'
    }
    try:
        for key,value in dict.items():
            response=requests.get(value[:-1],headers=headers)
            print(value[:-1])
            print(key+':'+str(response.status_code))
            with open(fileSaveDir + key+'.mp3','wb') as f1:
                f1.write(response.content)
            print(key+'.mp3 下载成功')
    except Exception:
        print("下载出错！")

def checkFilesExist(fileName):
    return os.path.exists(fileSaveDir + fileName)

def main():
    dict=get_index()
    downloader(dict)

if __name__=='__main__':
    main()