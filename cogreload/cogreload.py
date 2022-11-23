#pylint:disable=W0613
import functools
import asyncio
from pathlib import Path
import os
import logging
from discord import __version__ as version
from discord.ext.commands.errors import ExtensionError
logger=logging.getLogger(__name__)

class Reloader:
    def __init__(self,bot,path, interval, ignore_prefix="_"):
        self.bot=bot
        self.loop=asyncio.get_event_loop()
        self.path=path 
        self.iprefix=ignore_prefix
        self.files=[]
        self.mod=[]
        self.interval=interval
    
    async def start(self):
        if not Path(self.path).is_dir():
            raise FileNotFoundError("The path to cogs doesn't exists")
        self.files=[str(f) for f in [e for e in Path(self.path).iterdir() if os.path.isfile(e)] if not str(f).startswith(self.iprefix) and str(f).endswith(".py")]
        
        for file in self.files:
            self.mod.append(os.path.getmtime(file))
        self.bot.loop.create_task(self._start())
        
    async def _start(self):
        logger.info("watching changes for files:\n %s " % "\n".join(self.files))
        while True:
            for index, time, file in zip(range(len(self.files)),self.mod,self.files):
                if os.path.getmtime(file) != time:
                    try:
                        await self.bot.reload_extension(file.replace("\\",".").replace("/",".")[:-3])
                        logger.info("Reloaded %s Cog" % file)
                        self.mod[index] = os.path.getmtime(file)
                    except ExtensionError as e:
                          logger.error("Cannot reload %s cog:\n" % (file,),exc_info=e)
                    
            await asyncio.sleep(self.interval)


def watch(path,*,interval=1,ignore_prefix:str="_"): 
    def inner(func):
#        if not asyncio.iscoroutine(func):
#            raise ValueError("The function must be a coroutine")
        @functools.wraps(func)
        async def coro(bot):
            if func.__name__=="on_ready" or func.__name__=="setup_hook":
                reloader=Reloader(bot,path,interval,ignore_prefix)
                await reloader.start()
                return await func(bot)
            raise NameError("This decorator must be applied to on_ready or setup_hook")
        return coro
    return inner