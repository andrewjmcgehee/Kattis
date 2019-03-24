import argparse
import os

parser = argparse.Parser()
parser.add_argument("--zsh", help="install zsh completions", action="store_true")
args = parser.parse_args()

os.system("mv -v katti.py /usr/local/opt")
os.system("mkdir -v /usr/local/etc/katti")
os.system("mv -v problem_ids.json /usr/local/etc/katti")
os.system("pip3 install -r requirements.txt")

if args.zsh:
  os.system("mkdir -v $HOME/.zsh-completions")
  os.system("mv -v _katti $HOME/.zsh-completions")
  os.system("echo -v 'fpath=($HOME/.zsh-completions $fpath)' >> $HOME/.zshrc")
  os.system("exec zsh")

