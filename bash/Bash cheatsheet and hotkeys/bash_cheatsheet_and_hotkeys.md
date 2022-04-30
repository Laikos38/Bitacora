# Bash cheatsheet and hotkeys

1. `!!` Redo the last command, so for those times that you forget the `sudo`, you can type `sudo !!`.

2. Typing `cd` without arguments defaults to your home directory, same as `cd ˜ `. You can `cd -` to go to last directory, and this applies to with `git checkout -` to go to the previuos branch.
3. Hotkeys:
    1. `Ctrl + w` Deletes one word behind.
    2. `Ctrl + k` Deles everythingg from cursor to the end of the line.
    3. `Ctrl + u` Deletes everything from cursor to the start of the line.
    4. `Ctrl + y` Paste the last thing that you deleted using the above commands.
    5. `Ctrl + e` and `Ctrl + a` goes to the end and start of the line respectively.
    6. `Ctrl + l` to clear screen.
    7. `Alt + .` to cycle through the last argument of the last command.
4. `history | grep <phrase>` to search for a previous used command.
5. `touch file-{1, 2, 3}.md` or `touch file-{1..3}.md` this is called _curly braces expansion_, and in this example it creates 3 files as result: `file-1.md file-2.md file-3.md`.
6. `Ctrl + R` this is called _reverse-i-search_ and starts an autocomplete within one's history, its the perfect way to search a previuos used command.
