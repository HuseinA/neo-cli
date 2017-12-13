"""
Usage: 
  neo <command> [<args>...]

Options:
      --config string                    Location of client config
  -v, --version                         Print version information and quit

Commands:
  login       Log in to a NEO Cloud 
  logout      Log out from a NEO Cloud
  create      Deploy you service to NEO Cloud

Run 'neo COMMAND --help' for more information on a command.
"""


from inspect import getmembers, isclass
from docopt import docopt
# from docopt import DocoptExit
from . import __version__ as VERSION
import subprocess

def main():
  """Main CLI entrypoint."""
  import neo.cli
  options = docopt(__doc__, version=VERSION, options_first=True)
  # Retrieve the command to execute.
  command_name=""
  args=""
  command_args=""

  for (k, v) in options.items(): 
    if k== '<command>' and v:
      command_name =  options ['<command>']
    if k== '<args>' and v:
      args =  options['<args>']

  if not args:
    command_args = None
  else:
    command_args =  args[0]

  if hasattr(neo.cli, command_name) and command_name!='':
    module = getattr(neo.cli, command_name)
    neo.cli = getmembers(module, isclass)
    command = [command[1] for command in neo.cli if command[0] != 'Base'][0]
    command = command(options, command_args)
    command.execute()