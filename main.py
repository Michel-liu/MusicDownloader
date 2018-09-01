# -*- coding: UTF-8 -*-

from GetUrl import searchanddownload,download_163_music
from pyfiglet import Figlet
import readline


def menu():
    f = Figlet()
    print(f.renderText("CoolMusic"))
    print("0. 一键下载网易云音乐我喜欢歌单")
    print("1. 手动搜索并下载音乐")
    cho = input("请选择你想要的操作：")
    if cho == "0":
        download_163_music()
    if cho == "1":
        searchanddownload()


if __name__ == "__main__":
    menu()