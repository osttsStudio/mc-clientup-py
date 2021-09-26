# 基于python3的mc客户端自动更新v0.2.7

## 关于项目

<s>注：目前可通过bat更新config，更新程序自身可能会因为进程未结束拒绝访问，未测试。</s>
通过易语言暂时修复

## 使用环境

python3 Windows <s>理论上支持linux</s>（v0.1.8及以上不可在linux运行）<br>

## 使用须知
本软件仅用于更新自己的客户端<br><br>
非盈利开源软件 可二次修改 如果可以 请尽量在修改后的软件中署名原作者osttsStudio<br>

## 关于功能

简单粗暴的自动更新，程序会下载服务器配置文件并和本地配置文件进行比对,如果版本号大于本地文件，会自动下载更新包并解压覆盖，然后删除本地的服务器配置文件调用启动器（自己的服务器请下载源码修改url然后封包）

## 如何编译

#### 关于封包

pyinstaller -F xxx.py

pyinstaller -F -i xxx.ico xxx.py 封包图标

### 直接使用

因为需要修改url和部分变量 请下载源码自行编译

## 如何使用

将启动器改名为client.exe，可自定义更新程序的名字，同时需要修改bat文件<br>

如果有python3和相关库，可不编译直接运行py文件，记得修改bat文件

## TODO

- [x] 启动器支持自定义名称
- [x] 材质包在更新后会自动启用

## 更新日志

- 2021.09.26 add：程序版本号差异
- 2021.09.26 fix：因为资源服务器的不稳定性和确保不影响更新，将会从另一台服务器的配置文件获取资源服务器IP和版本对比文件，而不是从资源服务器获取，避免了资源服务器停机造成的无法更新
- 2021.09.20 add：新增进度条
- 2021.09.20 fix：修改下载方式
- 2021.09.20 fix：修改判断逻辑 如果版本不等于直接下载包
- 2021.09.16 fix：url获取改为读配置文件（仅域名 例：https://bilibili.com/config.ini 配置文件中只写https://bilibili.com，不要加 "/"）
- 2021.09.01 add：错误日志
- 2021.08.24 fix：删除无效代码
- 2021.08.24 add：更改启动器名称读取配置文件，可以修改配置文件自定义名称
- 2021.08.23 fix：优化代码结构，修复版本判断逻辑错误
- 2021.08.22 add：下载包时会打印目前版本和最新版本（mc的自定义版本 基于ImproveLib）
- 2021.08.22 fix：修复本地版本不低于最新版本更新日志不会被删除的bug
- 2021.08.21 add：下载更新包时会打印更新日志
- 2021.07.29 add：运行exe下载压缩包时会打印提示
- 2021.07.29 add：临时替代方案，用py调用基于易语言的程序更新自身并使材质包在更新后自动启用，之后会使用py重写这部分