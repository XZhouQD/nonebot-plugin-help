<div align="center">

# Archived
No further development in this repo.

# nonebot-plugin-help

### Nonebot2 轻量级帮助插件

<a href="https://raw.githubusercontent.com/xzhouqd/nonebot-plugin-help/main/LICENSE">
    <img src="https://img.shields.io/github/license/xzhouqd/nonebot-plugin-help?style=for-the-badge" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-help">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-help?color=green&style=for-the-badge" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-help">
    <img src="https://img.shields.io/pypi/dm/nonebot-plugin-help?style=for-the-badge" alt="pypi download">
</a>
<img src="https://img.shields.io/badge/require_python-3.8+-blue?style=for-the-badge" alt="python">
<br />
<img src="https://img.shields.io/badge/tested_python-3.10.6-blue?style=for-the-badge" alt="python">
<img src="https://img.shields.io/badge/tested_env-go_cqhttp_1.0.0-blue?style=for-the-badge" alt="python">
<img src="https://img.shields.io/badge/tested_Nonebot-2.0.0_rc4-red?style=for-the-badge" alt="nonebot">
</div>

## Bot可对本插件进行的配置

### 配置 help 插件是否at发送者（重要，可选） ![nonebot-plugin-help](https://img.shields.io/static/v1?label=nonebot-plugin-help&message=0.6.1&color=red)

0.6.1 版本起，新增是否at发送者配置，适用于adapter不支持at_sender的用户，如KOOK

可在.env配置文件内通过配置项`help_at_sender`配置，例如：
```
help_at_sender = false
```

### 配置 help 插件优先级与阻塞（可选） ![nonebot-plugin-help](https://img.shields.io/static/v1?label=nonebot-plugin-help&message=0.4.0&color=red)

0.4.0 版本起，新增插件优先级与阻塞设置（可选），默认为`priority=1, block=False`

用户可在.env 配置文件内通过配置项`help_block`与`help_priority`进行配置，例如，以下配置可将 help 命令配置为`priority=100, block=True`

```
help_block = true
help_priority = 100
```

### 配置 help 插件忽略列表与`to_me`规则（可选） ![nonebot-plugin-help](https://img.shields.io/static/v1?label=nonebot-plugin-help&message=0.6.0&color=red)

0.6.0 版本起，新增忽略插件与`to_me`规则（可选），`help_ignore_plugins`默认不忽略任何插件，`to_me`默认值为`False`。  

`help_ignore_plugins`：可配置不希望 help 插件列出的插件包名列表，例如，以下配置可忽略`nonebot_plugin_localstore`与`nonebot_plugin_apscheduler`插件。  
`help_to_me`：可配置是否只有私聊或提及Bot时才响应 help 命令。

```
help_ignore_plugins=["nonebot_plugin_localstore", "nonebot_plugin_apscheduler"]
help_to_me=true
```

## 开发者接入此插件列表方法

您可以直接参考本插件的接入方式，阅读源代码即可！

### 插件级别元数据接入 ![nonebot2](https://img.shields.io/static/v1?label=Nonebot&message=2.0.0%2Dbeta.4&color=red)

使用自 **Nonebot 2.0.0-beta.4** 版本起新增的插件元数据进行插件级统一接入（不包含 Matcher 级别接入）

```python
# New way of self registering (use PluginMetadata)
__plugin_meta__ = nonebot.plugin.PluginMetadata(
    name='您的插件名称（有别于nonebot-plugin-xxx的包名）',
    description='您的简单插件描述',
    usage='''您想在使用命令/help <your plugin package name>时提供的帮助文本''',
    type='{插件分类}', # From 2.0.0 Stable Version, 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。
    homepage='{项目主页}', # From 2.0.0 Stable Version
    config=Config, # From 2.0.0 Stable Version, 插件配置项类，如无需配置可不填写。
    extra={'version': '0.6.0'}
)
```

### 插件级别传统接入 ![nonebot2](https://img.shields.io/static/v1?label=Nonebot&message=2.0.0%2Dbeta.1&color=red)

使用 python 包形态的插件（已发布/自行开发皆可），并在插件包的**init**.py 文件内增加如下代码：

```python
# 您的插件版本号，将在/help list中显示
# Deprecated for nonebot-plugin-help 0.3.1+, prefer PluginMetadata.extra['version']
__help_version__ = '0.6.0'
# 此名称有助于美化您的插件在/help list中的显示
# 但使用/help xxx查询插件用途时仍必须使用包名
# Deprecated for nonebot-plugin-help 0.3.0+, prefer PluginMetadata.name
__help_plugin_name__ = "您的插件名称（有别于nonebot-plugin-xxx的包名）"
# Deprecated for nonebot-plugin-help 0.3.0+, prefer PluginMetadata.usage
# 若此文本不存在，将显示包的__doc__
__usage__ = '您想在使用命令/help <your plugin package name>时提供的帮助文本'
```

### Matcher 级别接入 ![nonebot2](https://img.shields.io/static/v1?label=Nonebot&message=2.0.0%2Dbeta.1&color=red)

Matcher 级别帮助请为 Matcher 添加如下代码：

```python
default_start = list(nonebot.get_driver().config.command_start)[0]
helper = on_command("help", priority=1, aliases={"帮助"})
helper.__help_name__ = '您的命令触发指令名'
helper.__help_info__ = '您为此命令提供的帮助文本'
helper.__doc__ = '您为此命令提供的帮助文本, 当您不希望使用__help_info__提供时，可以使用__doc__提供'
```

请注意：当您未提供`__help_name__`或`__help_info__`与`__doc__`中的一个时，此 Matcher 不会列入 Matcher 级别帮助！

## 实际使用

此部分介绍以使用'/'作为 command_start 为例。

### 获取本插件帮助

指令： /help

返回示例：

```
@<user_who_send_command> 欢迎使用Nonebot2 Help Menu
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
nonebot_plugin_cloverdata | 四叶草魔物娘属性计算插件 | 0.1.0
nonebot_plugin_guild_patch
nonebot_plugin_help | Nonebot2 Help Menu | 0.4.1
```

### 查看已加载某一插件用途

指令：/help <plugin_package_name | plugin_help_name>
示例：

```
/help nonebot_plugin_help

@<user_who_send_command> Nonebot2 Help Menu: Nonebot2轻量级帮助插件
欢迎使用Nonebot2 Help Menu                       // 这里是插件元数据提供的帮助
本插件提供公共帮助菜单能力
此Bot配置的命令前缀：/

/help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <插件名>  # 调取目标插件帮助信息


序号. 命令名: 命令用途                             // 这里是Matcher级别接入提供的帮助
1. help: /help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <plugin_name>  # 调取目标插件帮助信息
```

或使用提供的插件美化名示例：

```
/help Nonebot2 Help Menu

@<user_who_send_command> Nonebot2 Help Menu: Nonebot2轻量级帮助插件
欢迎使用Nonebot2 Help Menu                       // 这里是插件元数据提供的帮助
本插件提供公共帮助菜单能力
此Bot配置的命令前缀：/

/help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <插件名>  # 调取目标插件帮助信息


序号. 命令名: 命令用途                             // 这里是Matcher级别接入提供的帮助
1. help: /help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <plugin_name>  # 调取目标插件帮助信息
```

若插件未提供**usage**，则会显示**doc**，示例：

```
/help nonebot_plugin_help

@<user_who_send_command>
Nonebot 2 Help Menu
Author: XZhouQD
Since: 16 May 2021


序号. 命令名: 命令用途
1. help: /help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <plugin_name>  # 调取目标插件帮助信息
```
