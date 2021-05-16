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

__usage__ = '输入/help 获取使用方法'

__version__ = '0.1.0'

__plugin_name__ = "XZhouQD's Help Menu"

nonebot.export().help = helper