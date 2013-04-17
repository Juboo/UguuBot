from util import hook
import subprocess

@hook.command(autohelp=False)
def bash(inp):
    "bash -- Random Bash.org quotes!"
    bash = subprocess.Popen(["perl", "/home/tanner/projects/uguu/plugins/bash.pl"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
    return bash
