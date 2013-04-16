from util import hook
import subprocess
import random

with open("plugins/data/fortunes.txt") as f:
    fortunes = [line.strip() for line in f.readlines()
                if not line.startswith("//")]


@hook.command(autohelp=False)
def fortune(inp):
    "fortune -- Fortune cookies on demand."
    fortune = subprocess.Popen("fortune", stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
#    return random.choice(fortunes)
    return fortune
