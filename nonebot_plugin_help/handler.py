import nonebot.plugin
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, Arg
from nonebot.adapters import Event
from nonebot.adapters import Message
from nonebot.rule import to_me

from .config import Config

command_starts = list(nonebot.get_driver().config.command_start)
default_start = command_starts[0]
plugin_config = Config.parse_obj(nonebot.get_driver().config)
enable_at_sender = plugin_config.help_at_sender

helper = on_command("help", priority=plugin_config.help_priority, aliases={"帮助"}, block=plugin_config.help_block,
                    rule=to_me() if plugin_config.help_to_me else None)
# Matcher level info registering, still active in-use
helper.__help_name__ = 'help'
helper.__help_info__ = f'''{default_start}help  # 获取本插件帮助
{default_start}help list  # 展示已加载插件列表
{default_start}help <plugin_name>  # 调取目标插件帮助信息'''


@helper.handle()
async def handle_first_receive(event: Event, matcher: Matcher, args: Message = CommandArg()):
    if args:
        matcher.set_arg("content", args)
    else:
        result = f'''欢迎使用Nonebot2 Help Menu
支持使用的前缀：{" ".join(list(nonebot.get_driver().config.command_start))}
{default_start}help  # 获取本插件帮助
{default_start}help list  # 展示已加载插件列表
{default_start}help <plugin_name>  # 调取目标插件帮助信息
'''
        if enable_at_sender:
            await matcher.finish(result, at_sender=True)
        else:
            await matcher.finish(result)


@helper.got("content")
async def get_result(event: Event, content: Message = Arg()):
    arg = content.extract_plain_text().strip()
    if arg.lower() == "list":
        plugin_set = nonebot.plugin.get_loaded_plugins()
        plugin_names = []
        for plugin in plugin_set:
            if plugin.name in plugin_config.help_ignore_plugins:
                continue
            # plugin.name, then metadata name or legacy help name
            name = f'{plugin.name} | '
            try:
                name += plugin.metadata.name if plugin.metadata and plugin.metadata.name \
                    else plugin.module.__getattribute__("__help_plugin_name__")
            except:
                name = plugin.name
            # PluginMetadata.extra['version'] preferred, then legacy or optional
            try:
                version = plugin.metadata.extra.get('version', plugin.module.__getattribute__("__help_version__")) \
                    if plugin.metadata else plugin.module.__getattribute__("__help_version__")
            except:
                version = ""
            plugin_names.append(f'{name} | {version}')
        plugin_names.sort()
        newline_char = '\n'
        result = f'已加载插件：\n{newline_char.join(plugin_names)}'
    else:
        # package name
        plugin = nonebot.plugin.get_plugin(arg)
        # try nickname/helpname
        if not plugin:
            plugin_set = nonebot.plugin.get_loaded_plugins()
            for temp_plugin in plugin_set:
                try:
                    name = temp_plugin.metadata.name if temp_plugin.metadata and temp_plugin.metadata.name \
                        else temp_plugin.module.__getattribute__("__help_plugin_name__")
                except:
                    name = temp_plugin.name
                if name == arg:
                    plugin = temp_plugin
        # not found
        if not plugin:
            result = f'{arg} 不存在或未加载，请确认输入了正确的插件名'
        else:
            results = []
            # if metadata set, use the general usage in metadata instead of legacy __usage__
            if plugin.metadata and plugin.metadata.name and plugin.metadata.usage:
                results.extend([f'{plugin.metadata.name}: {plugin.metadata.description}', plugin.metadata.usage])
            else:
                # legacy __usage__ or __doc__
                try:
                    results.extend([plugin.module.__getattribute__("__help_plugin_name__"),
                                    plugin.module.__getattribute__("__usage__")])
                except:
                    try:
                        results.extend([plugin.name, plugin.module.__doc__])
                    except AttributeError:
                        pass
            # Matcher level help, still legacy since nb2 has no Matcher metadata
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
            if index > 1:
                results.extend(["", "序号. 命令名: 命令用途"])
                results.extend(
                    [f'{key}: {value}' for key, value in infos.items()
                     if key and value]
                )
            results = list(filter(None, results))
            result = '\n'.join(results)
    if enable_at_sender:
        await helper.finish(result, at_sender=True)
    else:
        await helper.finish(result)
