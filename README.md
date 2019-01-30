# Kattis
Problems I have solved, and cool things I have learned on open.kattis.com 

I will try to always push solutions/snippets with detailed comments. This repo is for learning purposes. Feel free to use my solutions, 
change them, steal them and rip them off as your own, whatever you like... as long as you learn from them!

## Conventions:
All kattis solutions are named by their problem id on kattis and are enclosed in a directory by that name. If they have sample inputs
or expected outputs those will be included in the directory. All files that are not enclosed in a directory are some kind of code
snippet which I find helpful or interesting.

NOTE: Ratings listed in solutions are tentative. They constantly change and update as new submissions are made.

# Installation of Katti Automation (Mac / Linux)

To install the Katti command line tool, simply download the katti.py file  and follow these steps.

NOTE: Python 3 is required and "python3" must be linked.

1. Move the katti.py file into your local binaries with:
```
$ mv katti.py /usr/local/bin
```
2. Login to Kattis and download your person .kattisrc file from:
```
https://icpc.kattis.com/download/kattisrc
```
3. Move your .kattisrc to your home directory:
```
$ mv .kattisrc ~/
```
4. Alias "katti" in your .bashrc / .zshrc file:
```
alias katti="/usr/local/bin/python3 /usr/local/bin/katti.py"
```
5. Source your rc file:
```
$ source .zshrc
```
```
$ source .bashrc
```
