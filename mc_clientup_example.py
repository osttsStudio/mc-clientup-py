import os
import sys
import time
import zipfile
import logging
import tempfile
import traceback
import urllib.request
from urllib import request
from configparser import ConfigParser

os.remove('error.log') # del old log file

logging.basicConfig(filename='error.log',level=logging.DEBUG,format="%(asctime)s - %(pathname)s - %(message)s",datefmt="%Y/%m/%d %H:%M:%S")

os.system("") # fixd print's color bug in Win10

# load local config
con = ConfigParser()
con_path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read(con_path)
Url_server = con.get('url','server')
Con_res = os.getcwd() + "./config_new.ini" # config_new.ini--server config file name
bat_res = os.getcwd() + "/.minecraft/update.bat" # a bat file for updating itself and config, and supports deleting unnecessary files
Ver_res = os.getcwd() + "./version.txt" # update logs name
Client_res = os.getcwd() + "./client.ini" # launcher name file
Ver_url = Url_server + "/version.txt" # update logs
Con_url = Url_server + "/config.ini" # config file url
Client_url = Url_server + "/client.ini" # launcher name file url

# Ver_url = "http://xxx/version.txt" # update logs
# Con_url = "http://xxx/config.ini" # config file url
# Client_url = "http://xxx/client.ini" # launcher name file url

try:
    request.urlretrieve(Con_url,Con_res)  # download server config file
    request.urlretrieve(Ver_url,Ver_res)  # download update logs

except:
    logging.debug(traceback.format_exc())

try:
    if not os.path.exists(con_path):
        print("\033[1;31;40mFile config.ini does not exist,please re-download.url:none\033[0m")
        input("Press Enter to exit.")
        os.remove('config_new.ini')
        os.remove('version.txt')
        sys.exit('config not found')
except:
    logging.debug(traceback.format_exc())

Ver_local = con.get('ver','version')
Mc_local = con.get('ver','mc_version')

# load server config
con_server = ConfigParser()
con_serverpath = os.path.join(os.path.abspath('.'),'config_new.ini') # config_new.ini--server config file name
con_server.read(con_serverpath)
Ver_server = con_server.get('ver','version')
Mc_server = con_server.get('ver','mc_version')

try:
    if not os.path.exists(Client_res):
        request.urlretrieve(Client_url,Client_res)  # download launcher name file
        print("""
client.ini下载成功，如启动器名称不是默认的client.exe请修改client.ini文件后重新运行。
The client.ini download is successful, if the launcher name is not the default：client.exe, please modify the client.ini file and run again.""")
        input("Press Enter to exit.")
        os.remove('version.txt')
        os.remove('config_new.ini')
        sys.exit('config.ini download is successful')
except:
    logging.debug(traceback.format_exc())

# launcher name config
Client_ini = ConfigParser()
Client_path = os.path.join(os.path.abspath('.'),'client.ini') # client.ini--launcher name file
Client_ini.read(Client_path)
Client = Client_ini.get('setting','name')

# config.ini does not exist

try:
    if int(Ver_local) == int(Ver_server):
        os.system(Client)
        os.remove('version.txt')
        os.remove('config_new.ini')
        sys.exit(f'start {Client} is successful')

except:
    logging.debug(traceback.format_exc())

try:
    if int(Ver_local) != int(Ver_server):

        with open(r"version.txt", encoding="utf-8") as file:
            print(file.read())
            print('更新程序版本：0.2.6')
            print(f"目前MC版本：{Mc_local}  最新MC版本：{Mc_server}")
            print("""\n\033[5;36;40mDownloading...Please wait.\033[0m\n""")

        # ===old download code===
        # def get_data():
        #     Zip_url = Url_server + "/files/chii-update.zip"
        #     response = requests.get(Zip_url)
        #     return Zip_url, response.content

        # Zip_url, data = get_data()

        # Temp_file = tempfile.TemporaryFile()

        # Temp_file.write(data)

        # Unzip = zipfile.ZipFile(Temp_file, mode='r')
        # for names in Unzip.namelist():
        #     Unzip.extract(names, './.minecraft')  # unzip to .minecraft

        # Unzip.close()
        # Temp_file.close()
        # ========================

        def report(blocknum, blocksize, totalsize):
            readsofar = blocknum * blocksize
            if totalsize > 0:
                percent = readsofar * 1e2 / totalsize
                s = "\r%5.1f%% %*d / %d" % (percent, len(str(totalsize)), readsofar, totalsize)
                sys.stderr.write(s)
                if readsofar >= totalsize:
                    sys.stderr.write("\n")
            else: # total size is unknown
                sys.stderr.write("read %d\n" % (readsofar,))

        Zip_url = Url_server + "/files/chii-update.zip"
        urllib.request.urlretrieve(Zip_url,"./chii-update.zip",report)
        # ZIP = requests.get(Zip_url)
        # with open(Zip_res,"wb") as file:
        #     file.write(ZIP.content)
        
    Unzip = zipfile.ZipFile("./chii-update.zip", mode='r')
    for names in Unzip.namelist():
        Unzip.extract(names, './.minecraft')  # unzip to .minecraft
    Unzip.close()

    time.sleep(2)
    os.remove('version.txt')
    os.remove('chii-update.zip')
    os.system('resourcepacks.exe')
    os.system(Client)
    os.remove('config_new.ini')
    sys.exit('update is successful')

except:
    logging.debug(traceback.format_exc())