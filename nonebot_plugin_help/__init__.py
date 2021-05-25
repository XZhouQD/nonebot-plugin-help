"""
Nonebot 2 Help Plugin
Author: XZhouQD
Since: 16 May 2021
"""
from pathlib import Path
import nonebot

from .handler import helper

# store all subplugins
_sub_plugins = set()
# load sub plugins
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve()))

__usage__ = '''欢迎使用Nonebot 2 Help Plugin
/help  # 获取本插件帮助
/help list  # 展示已加载插件列表
/help <plugin_name>  # 调取目标插件帮助信息
'''

__version__ = '0.1.2'

__plugin_name__ = "XZhouQD's Help Menu"

nonebot.export().help = helper