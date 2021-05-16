import nonebot.plugin
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.log import logger

helper = on_command("help", priority=1, aliases={"帮助"})


@helper.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.info(args)
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
                name = f'{plugin.name}: {plugin.module.__getattribute__("__plugin_name__")}'
            except:
                name = plugin.name
            try:
                version = plugin.module.__getattribute__("__version__")
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
            result = plugin.module.__getattribute__("__usage__")
        except:
            try:
                result = plugin.module.__doc__
            except AttributeError:
                result = f'{state.get("content")}插件不存在或未加载'
    await helper.finish(Message().append(at).append(MessageSegment.text(result)))


async def get_help():
    return f'''您已键入/help命令，现为您展示此命令相关帮助：
/help list  展示已加载插件列表
/help <plugin_name>  调取目标插件帮助信息
'''
