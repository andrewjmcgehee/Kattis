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

**1. Move the katti.py file into your local opt directory with:**
```
$ mv katti.py /usr/local/opt
```
**2. Login to Kattis and download or copy and paste your personal .kattisrc file from:**
```
https://icpc.kattis.com/download/kattisrc
```
**3. Move your .kattisrc to your home directory:**
```
$ mv .kattisrc $HOME
```
**4. Create a simple executable shell script which your OS can find in your $PATH:**
```
$ echo 'python3 /usr/local/opt/katti.py "$@"' > /usr/local/bin/katti 
$ chmod +x /usr/local/bin/katti 
```
**5. Source your rc file:**
##### Zsh or Oh-My-Zsh
```
$ source .zshrc
```
##### Bash
```
$ source .bashrc
```

Please note that katti writes a small json config file to /usr/local/etc called "katti.json."
This is normal behavior.

## Zsh or Oh-My-Zsh Completions

If you would like zsh or oh-my-zsh to complete katti's options for you, follow these steps.
Otherwise it is safe to discard the "_katti" file.

**1. Locate or create one of the following directories:**
##### Zsh
```
$ mkdir -v /usr/local/share/zsh/functions
```
##### Oh-My-Zsh
```
$ mkdir -v $HOME/.oh-my-zsh/completions
```
**2. Make sure that one of the directories in step 1 is in your $FPATH:**
```
$ print -rl -- $FPATH
```
**3. If not, add this to your .zshrc file:**
```
fpath=($fpath <your_directory_here>)
```
**4. Move the "_katti" compdef file into the directory from step 1 with:**
```
$ mv _katti <your_directory_here>
```
**5. Launch a new terminal session**
