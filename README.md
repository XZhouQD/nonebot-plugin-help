# nonebot-plugin-help
A general help plugin for nonebot2

为nonebot2插件提供泛用的帮助列表

## 开发者接入此插件列表方法

使用python包形态的插件（已发布/自行开发皆可），并在插件包的__init__.py文件内增加如下代码：
```python
# 若此文本不存在，将显示包的__doc__
__usage__ = '您想在使用命令/help <your plugin package name>时提供的帮助文本'

# 您的插件版本号，将在/help list中显示
__help__version__ = '0.1.4' 

# 此名称有助于美化您的插件在/help list中的显示
# 但使用/help xxx查询插件用途时仍必须使用包名
__help__plugin_name__ = "您的插件名称（有别于nonebot-plugin-xxx的包名）" 
```

## 实际使用
### 查看已加载插件列表
指令：/help list

返回示例：
```
@<user_who_send_command> 已加载插件：
dice: XZhouQD's Roll 0.1.0
nonebot_plugin_help: XZhouQD's Help Menu 0.1.0
nonebot_plugin_apscheduler 
nonebot_plugin_status 
```

### 查看已加载某一插件用途
指令：/help <plugin_package_name>
示例：
```
/help help

@<user_who_send_command> 欢迎使用Nonebot 2 Help Plugin，请输入/help 获取使用方法
```

若插件未提供__usage__，则会显示__doc__，示例：
```
/help nonebot_plugin_status

@<user_who_send_command>
@Author         : yanyongyu
@Date           : 2020-09-18 00:00:13
@LastEditors    : yanyongyu
@LastEditTime   : 2021-03-16 17:05:58
@Description    : None
@GitHub         : https://github.com/yanyongyu
```