"""
Usage: 
  neo <command> [<args>...]

Options:
     --config string                    Location of client config
  -v, --version                         Print version information and quit

Management Commands:
  config      Manage NEO configs
  instance    Manage Instance
  network     Manage network
  volume      Manage Volumes
  deploy      manage Deploy

Commands:
  login       Log in to a NEO Cloud 
  logout      Log out from a NEO Cloud
  ssh         SSH in to a NEO Cloud Instance
  created     Create a resource from a file or from stdin
  delete      Delete resource by filenames, stdin, resource and names, or by resources and label selected

Run 'neo COMMAND --help' for more information on a command.
"""


from inspect import getmembers, isclass
from docopt import docopt
from docopt import DocoptExit
from . import __version__ as VERSION
import subprocess

def main():
  """Main CLI entrypoint."""
  import neo.commands
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

  if hasattr(neo.commands, command_name) and command_name!='':
    module = getattr(neo.commands, command_name)
    neo.commands = getmembers(module, isclass)
    #print len(neo.commands)
    command = [command[1] for command in neo.commands if command[0] != 'Base'][0]
    command = command(options, command_args)
    command.execute()
  else:
    print subprocess.check_output(['neo','--help'])