import argparse
import os

parser = argparse.Parser()
parser.add_argument("--zsh", help="install zsh completions", action="store_true")
args = parser.parse_args()

os.system("cp -v katti.py /usr/local/opt")
os.system("echo 'python3 /usr/local/opt/katti.py \"$@\"' > /usr/local/bin/katti")
os.system("chmod +x /usr/local/bin/katti")
os.system("mkdir -v /usr/local/etc/katti")
os.system("cp -v problem_ids.json /usr/local/etc/katti")
os.system("pip3 install -r requirements.txt")

if args.zsh:
  os.system("mkdir -v $HOME/.zsh-completions")
  os.system("cp -v _katti $HOME/.zsh-completions")
  os.system("echo 'fpath=($HOME/.zsh-completions $fpath)' >> $HOME/.zshrc")
  os.system("exec zsh")

