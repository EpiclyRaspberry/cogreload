# Cog reload
automatic cog reloader for discord.py
## requirements
`discord.py 1.7.3` or above<br>
atleast `python 3.5` for `discord.py 1.7.3` support 
## usage
```py
from cogreload import watch
# you must subclass commands.Bot
class ExampleBot(commands.Bot):
    # override on_ready or setup_hook(for discord.py 2.0)
    # put the decorator here
    @watch(
        "./cogs/", #the directory where is your cogs is in
        ignore_prefix="_", # will ignore all the files that starts at "_",
        interval=1 #seconds between checks
        )
    async def on_ready(self):
        print("Bot is online!")
```
