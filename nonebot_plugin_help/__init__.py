"""
Nonebot 2 Help Plugin
Author: XZhouQD
Since: 16 May 2021
"""
from pathlib import Path
import nonebot

from .handler import helper


default_start = list(nonebot.get_driver().config.command_start)[0]

# store all subplugins
_sub_plugins = set()
# load sub plugins
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve()))

__usage__ = f'''欢迎使用Nonebot 2 Help Plugin
支持使用的前缀：{" ".join(list(nonebot.get_driver().config.command_start))}
{default_start}help  # 获取本插件帮助
{default_start}help list  # 展示已加载插件列表
{default_start}help <plugin_name>  # 调取目标插件帮助信息
'''

__version__ = '0.1.3'

__help_plugin_name__ = "XZhouQD's Help Menu"

nonebot.export.help = helper
