### DESCRIPTION

This platformer is still in development.
There is no clear objective to this project.

Currently 4 maps playable

**New gameplay **
- 1v1 : 2 players, first to the winning block win

**Controls Player 1 : Arrows**
**Controls Player 2 : [Z,S,Q,D]**

### COMPILE TUTORIAL 

First, install pyinstaller :
```
pip install pyinstaller
```

Then, go on the project folder and compile the main.py file using :
```
pyinstaller --onefile --noconsole --add-data "images;images" main.py
```
*This command can take some time.*

Then, in the **dist** folder, you now have a ***main.exe*** file. Just run it to play the game.


### IDEAS

Ennemies :
- flying
- throwing
- walking same path
- try to go to player

type of blocks : 
- portals
- locked door (need a key to open it)

Game over screen (need lives system)

Score (need pieces to collect on the levels)

Winning screen :
- timer shown at the end
- score shown at the end


