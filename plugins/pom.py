from util import hook
import subprocess

@hook.command(autohelp=False)
def pom(inp):
    "pom -- Phase Of Moon"
    return subprocess.Popen("pom", stdout=subprocess.PIPE).communicate()[0]
