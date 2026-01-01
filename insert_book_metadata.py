# I think that an efficient way to find the tags of #book inside my 
# whole obsidian vault is by using grep, but as this is a python 
# programme, I don't know if I can insert shell execution in here. 
# I should probably be able to do so if there is a built library.

import subprocess
# There is indeed a library called subprocess that is  able to 
# access the terminal. It seems that with subprocess.run() I can
# run any command from the shell. I think that the command should
# look something like 
# 'rg -r "#book" home/schronding/Documents/clean_sync'

books = ""
# books.join(subprocess.run(['shell', 'rg -r "#book" home/schronding/Documents/clean_sync']))

# Here my purpose is to insert the list of the books as a string 
# inside the variable 'books'. 
# FileNotFoundError: [Errno 2] No such file or directory: 'shell'
# It seems like there is no 'shell'. It probably goes by another name. 
# It seems that what is missing is the argument 'shell=True' in the
# method '.run()'

# subprocess.run(['shell', 'rg -r "#book" home/schronding/Documents/clean_sync'], shell=True)
# The command seems to work, but I don't know if I am missing the syntax
# of ripgrep, or if I wrote the routed incorrectly. 
# pwd returned /home/schronding/Documents/clean_sync

# subprocess.run(['shell', 'rg -r "#book" /home/schronding/Documents/clean_sync'], shell=True)

# The error 
# rg -r "#book" /home/schronding/Documents/clean_sync: 1: shell: not found 
# persists. I might be messing up with the ripgrep syntax
# It seems thar ripgrep uses a syntax similar to sed. The thing I have 
# notice is that even if the command works, it will probably just return the 
# line that contains the hashtag '#book', but what I want is the title
# of the note. I will assume that the titles are on the first line of the
# markdown file. I don't how I can narrow the search of ripgrep, but at 
# least I found a command that I think will work

subprocess.run(['shell', 'rg --files | rg #book'], shell=True)

# It stil says that the shell hasn't been found
# rg --files | rg #book: 1: shell: not found
# It seems I indeed need to wrap the searching term between quotes 
# so ripgrep can found it. While it seems that the command worked, it 
# didn't print anything, which is weird 
# rg --files | rg #book
# rg: ripgrep requires at least one pattern to execute a search
# rg --files | rg "#book"
# Nothing
# It seems I was overcomplicating things 