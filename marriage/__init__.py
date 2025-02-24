from asyncio import create_task
from .marriage import Marriage

async def setup_after_ready(bot):
    await bot.wait_until_red_ready()
    cog = Marriage(bot)
    for command in cog.get_commands():
        if not command.parent:
            # Prepend "m" to the command name if one already exists in the bot
            if bot.get_command(command.name):
                command.name = f"m{command.name}"
            # Update aliases similarly
            new_aliases = []
            for alias in command.aliases:
                if bot.get_command(alias):
                    new_aliases.append(f"m{alias}")
                else:
                    new_aliases.append(alias)
            command.aliases = new_aliases
    await bot.add_cog(cog)

async def setup(bot):
    create_task(setup_after_ready(bot))
