<div align="center">

# nonebot-plugin-help
### Nonebot2 轻量级帮助插件

<a href="https://raw.githubusercontent.com/xzhouqd/nonebot-plugin-help/main/LICENSE">
    <img src="https://img.shields.io/github/license/xzhouqd/nonebot-plugin-help?style=for-the-badge" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-help">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-help?color=green&style=for-the-badge" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.7.3+-blue?style=for-the-badge" alt="python">
<br />
<img src="https://img.shields.io/badge/tested_python-3.8.10-blue?style=for-the-badge" alt="python">
<img src="https://img.shields.io/static/v1?label=tested+env&message=go-cqhttp+1.0.0-beta8-fix2&color=blue&style=for-the-badge" alt="python">

<br />
<a href="https://github.com/botuniverse/onebot/blob/master/README.md">
    <img src="https://img.shields.io/badge/Onebot-v11-brightgreen?style=for-the-badge" alt="onebot">
</a>
<a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/static/v1?label=Nonebot&message=2.0.0%2Dbeta.1&color=red&style=for-the-badge" alt="nonebot">
</a>
<a href="https://pypi.org/project/nonebot-adapter-cqhttp/">
    <img src="https://img.shields.io/static/v1?label=Nonebot-adapters-onebot&message=2.0.0%2Dbeta.1&color=red&style=for-the-badge" alt="nonebot-adapters-cqhttp">
</a>
</div>

## 开发者接入此插件列表方法
### 包级别接入
使用python包形态的插件（已发布/自行开发皆可），并在插件包的__init__.py文件内增加如下代码：
```python
# 若此文本不存在，将显示包的__doc__
__usage__ = '您想在使用命令/help <your plugin package name>时提供的帮助文本'

# 您的插件版本号，将在/help list中显示
__help_version__ = '0.2.1' 

# 此名称有助于美化您的插件在/help list中的显示
# 但使用/help xxx查询插件用途时仍必须使用包名
__help_plugin_name__ = "您的插件名称（有别于nonebot-plugin-xxx的包名）" 
```
### Matcher级别接入
Matcher级别帮助请为Matcher添加如下代码：
```python
default_start = list(nonebot.get_driver().config.command_start)[0]
helper = on_command("help", priority=1, aliases={"帮助"})
helper.__help_name__ = '您的命令触发指令名'
helper.__help_info__ = f'您为此命令提供的帮助文本'
helper.__doc__ = f'您为此命令提供的帮助文本, 当您不希望使用__help_info__提供时，可以使用__doc__提供'
```
请注意：当您未提供`__help_name__`或`__help_info__`与`__doc__`中的一个时，此Matcher不会列入Matcher级别帮助！

## 实际使用
此部分介绍以使用'/'作为command_start为例。
### 获取本插件帮助
指令： /help

返回示例：
```
@<user_who_send_command> 欢迎使用Nonebot 2 Help Plugin
支持使用的前缀：/
/help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <plugin_name>  # 调取目标插件帮助信息
```
### 查看已加载插件列表
指令：/help list

返回示例：
```
@<user_who_send_command> 已加载插件：
nonebot.plugins.echo 
nonebot_guild_patch 
nonebot_plugin_cloverdata | 四叶草魔物娘属性计算插件 0.1.0
nonebot_plugin_help | XZhouQD's Help Menu 0.1.5
```

### 查看已加载某一插件用途
指令：/help <plugin_package_name>
示例：
```
/help nonebot_plugin_help

@<user_who_send_command> 欢迎使用Nonebot 2 Help Plugin
本插件提供公共帮助菜单能力
此Bot配置的命令前缀：/


序号. 命令名: 命令用途
1. help: /help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <plugin_name>  # 调取目标插件帮助信息
```

若插件未提供__usage__，则会显示__doc__，示例：
```
/help nonebot_plugin_help

@<user_who_send_command>
Nonebot 2 Help Plugin
Author: XZhouQD
Since: 16 May 2021


序号. 命令名: 命令用途
1. help: /help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <plugin_name>  # 调取目标插件帮助信息
```
