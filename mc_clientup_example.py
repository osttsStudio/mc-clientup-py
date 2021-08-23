# ====================================================

# Author:狐日泽
# Version:0.2.0
# name:mc_clientup_py

# 基于python3的简单粗暴mc客户端自动更新程序
# 程序会下载服务器配置文件并和本地配置文件进行比对
# 如果版本号大于本地文件，会自动下载更新包并解压覆盖，然后删除服务器配置文件

# Simple and rude mc client automatic update program based on python3.
# The program will download the server configuration file and compare it with the local configuration file.
# If the version number is greater than the local file, the update package will be automatically downloaded and decompressed and overwritten, and then the server configuration file will be deleted.

# ====================================================

import os
import sys
import time
import zipfile
import requests
import tempfile
from urllib import request
from configparser import ConfigParser

os.system("") # fixd print's color bug in Win10

Con_res = os.getcwd() + "./config_new.ini" # config_new.ini--server config file name
Zip_res = os.getcwd() + "./xxx.zip" # update file name
bat_res = os.getcwd() + "/.minecraft/update.bat" # a bat file for updating itself and config, and supports deleting unnecessary files
Ver_res = os.getcwd() + "./version.txt" # update logs name
Ver_url = "http://xxx/xxx.txt" # update logs
Con_url = "http://xxx/xxx.ini" # config file url

request.urlretrieve(Con_url,Con_res)  # download server config file
request.urlretrieve(Ver_url,Ver_res)  # download update logs

# load local config
con = ConfigParser()
con_path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read(con_path)
Ver_local = con.get('ver','version')
Mc_local = con.get('ver','mc_version')

# load server config
con_server = ConfigParser()
con_serverpath = os.path.join(os.path.abspath('.'),'config_new.ini') # config_new.ini--server config file name
con_server.read(con_serverpath)
Ver_server = con_server.get('ver','version')
Mc_server = con_server.get('ver','mc_version')

# config.ini does not exist
if not os.path.exists(con_path):
    print("\033[1;31;40mFile config.ini does not exist,please re-download.url:none\033[0m")
    input("Press Enter to exit.")
    os.remove('config_new.ini')
    os.remove('version.txt')
    sys.exit(1)

if int(Ver_local) == int(Ver_server):
    os.system('client.exe')
    os.remove('config_new.ini')
    os.remove('version.txt')
    sys.exit(0)

if int(Ver_local) < int(Ver_server):

    with open(r"version.txt", encoding="utf-8") as file:
        print(file.read())
        print(f"目前版本：{Mc_local}  最新版本：{Mc_server}")
        print("\033[5;36;40mDownloading...Please wait.\033[0m")

    def get_data():
        Zip_url = "http://xxx/xxx.zip"
        response = requests.get(Zip_url)
        return Zip_url, response.content

    Zip_url, data = get_data()

    Temp_file = tempfile.TemporaryFile()

    Temp_file.write(data)

    Unzip = zipfile.ZipFile(Temp_file, mode='r')
    for names in Unzip.namelist():
        Unzip.extract(names, './.minecraft')  # unzip to .minecraft

    Unzip.close()
    Temp_file.close()
    
    time.sleep(2)
    os.remove('version.txt')
    os.remove('config_new.ini')
    os.system('client.exe')
    os.system('resourcepacks.exe')
    sys.exit(0)

if int(Ver_local) > int(Ver_server):
    print("\033[1;31;40mThe version is wrong,please re-dowoload. url:none\033[0m")
    input("Press Enter to exit.")
    os.remove('config_new.ini')
    os.remove('version.txt')
    sys.exit(1)