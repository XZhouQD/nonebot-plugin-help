import nonebot.plugin
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.log import logger


default_start = list(nonebot.get_driver().config.command_start)[0]
helper = on_command("help", priority=1, aliases={"帮助"})
helper.__help_name__ = 'help'
helper.__help_info__ = f'''{default_start}help  # 获取本插件帮助
{default_start}help list  # 展示已加载插件列表
{default_start}help <plugin_name>  # 调取目标插件帮助信息'''


@helper.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.debug(args)
    if args:
        state["content"] = args
    else:
        state["content"] = ""


@helper.got("content")
async def get_result(bot: Bot, event: Event, state: T_State):
    at = MessageSegment.at(event.get_user_id())
    if not state.get("content"):
        result = await get_help()
    elif str(state.get("content")).lower() == "list":
        plugin_set = nonebot.plugin.get_loaded_plugins()
        plugin_names = []
        for plugin in plugin_set:
            try:
                name = f'{plugin.name} | ' \
                    f'{plugin.module.__getattribute__("__help_plugin_name__")}'
            except:
                name = f'{plugin.name}'
            try:
                version = plugin.module.__getattribute__("__help_version__")
            except:
                version = ""
            plugin_names.append(f'{name} {version}')
        plugin_names.sort()
        newline_char = '\n'
        result = f'已加载插件：\n{newline_char.join(plugin_names)}'
    else:
        try:
            plugin = nonebot.plugin.get_plugin(state.get("content"))
        except AttributeError:
            plugin = None
        try:
            matchers = plugin.matcher
            infos = {}
            index = 1
            for matcher in matchers:
                try:
                    name = matcher.__help_name__
                except AttributeError:
                    name = None
                try:
                    help_info = matcher.__help_info__
                except AttributeError:
                    help_info = matcher.__doc__
                if name and help_info:
                    infos[f'{index}. {name}'] = help_info
                    index += 1
            results = [plugin.module.__getattribute__("__usage__"),
                       "", "序号. 命令名: 命令用途"]
            results.extend(
                [f'{key}: {value}' for key, value in infos.items()
                 if key and value]
            )
            result = '\n'.join(results)
        except:
            try:
                result = plugin.module.__doc__
            except AttributeError:
                result = f'{state.get("content")}插件不存在或未加载'
    await helper.finish(Message().append(at).append(
        MessageSegment.text(result)))


async def get_help():
    return f'''欢迎使用Nonebot 2 Help Plugin
支持使用的前缀：{" ".join(list(nonebot.get_driver().config.command_start))}
{default_start}help  # 获取本插件帮助
{default_start}help list  # 展示已加载插件列表
{default_start}help <plugin_name>  # 调取目标插件帮助信息
'''
