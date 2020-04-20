# Python-Sudoku-MySQL

[Downloads](https://github.com/VarunS2002/Python-Sudoku-MySQL/releases)

This is a fully fledged sudoku game written in Python using Tkinter GUI and uses MySQL database for data

### Usage:

-Run the query sql script atleast once before running the sudoku program 

-Default values of host, username and password for connecting to MySQL are localhost, root and *no password* respectively

-To change these values place the mysql_config.txt file in the same folder as the sudoku program

-The main part of the config file should look like this:


host:<br />
localhost<br />
username:<br />
root<br />
password:<br />
testpass<br />


-localhost, root and testpass are the custom values for host, username and password respectively

-If any of these lines are left empty the program will use the default values for the particular field


### Note:

-The query sql script has 3 games defined by default which are soft coded in the Sudoku program

-To add more games you will need to add them in the database

-You can use the insert games tool provided to do that

-Insert Games tool:
[Downloads](https://github.com/VarunS2002/Python-Sudoku-MySQL-Insert_Games/releases)

-Increase the value of the gno column by 1 everytime you add a new game without the tool

-No code changes have to be made in the main program after adding new games 

-Adding incorrect values, rows or columns in the database may cause the program to not function correctly and result in errors 

### Features:

-Input numbers in the grid by repeatedly clicking a box

-3 different games

-Randomly chooses one game on start

-Shows you the game currently active

-Added Choose Game option to manually change the game

-Restart Game option

-Check Result option

-Show Solution option

-About option with version, link for releases and for sources

-PEP 8 format
