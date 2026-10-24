[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/o2QcGGke)
# W9_6

In some scenarios, programs contain unsaved user data, and the user may accidentally do something that typically causes the program to close. In CLI programs, this occurs if the user sends a keyboard interrupt (CTRL + C). Handle the KeyboardInterrupt in a menu-driven program, which collects user-inserted lines.

If the user has inserted 0 lines during a program run, there is nothing to save. Handle the keyboard interrupt (CTRL + C) smoothly by informing the user that the program is closing suddenly.

If the user has inserted 1 or more lines and then presses CTRL + C, prompt the user to confirm if they would like to save the lines to a file. If the user confirms with yes, ask for the filename to write. Otherwise close the program gracefully.

In the example program runs below, keypair ^C indicates user initiated KeyboardInterrupt. Text after ^C on the same line represents program output after keyboard interrupt (color glitch).

Run 1
````
Program starting.
Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: 1
Insert text: First line.

Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: 1
Insert text: Second line.

Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: ^CKeyboard interrupt and unsaved progress!
Save before quit(y/n)?: y
Insert filename: file1.txt
Program ending.
````

Run 2
````
Program starting.
Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: ^CClosing suddenly.
Program ending.
````

Run 3
````
Program starting.
Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: 1
Insert text: Some content.

Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: 5
Unknown option!

Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: 1
Insert text: Some more content.

Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: ^CKeyboard interrupt and unsaved progress!
Save before quit(y/n)?: y
Insert filename: file3.txt
Program ending.
````

Run 4
````
Program starting.
Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: 1
Insert text: Temporary.

Options:
1 - Insert line
2 - Save lines
0 - Exit
Your choice: ^CKeyboard interrupt and unsaved progress!
Save before quit(y/n)?: n
Program ending.
````
