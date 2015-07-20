|---------------------------------|
|"2048" single-player puzzle game |
|				  |
|create by Rachel Xu, 05/01/2015  | 
|---------------------------------|


DESCRIPTION OF THE GAME
=======================
2048 is played on a gray 4?4 grid, with numbered tiles that slide smoothly when a player moves them using the four arrow keys.Every turn, a new tile will randomly appear in an empty spot on the board with a value of either 2 or 4. Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. The resulting tile cannot merge with another tile again in the same move. Higher-scoring tiles emit a soft glow.

A scoreboard on the upper-right keeps track of the user's score. The user's score starts at zero, and is incremented whenever two tiles combine, by the value of the new tile. As with many arcade games, the user's best score is shown alongside the current score. A game of 2048 in progress.

The game is won when a tile with a value of 2048 appears on the board, hence the name of the game. After reaching the 2048 tile, players can continue to play (beyond the 2048 tile) to reach higher scores. The maximum possible tile is 131,072 (or 217); the maximum possible score is 3,932,156; the maximum number of moves is 131,038. When the player has no legal moves (there are no empty spaces and no adjacent tiles with the same value), the game ends.

----Wikipedia, "2048(video game)"

The original version of the game is developed by Gabriele Cirulli, available at http://gabrielecirulli.github.io/2048/


HOW TO RUN THE GAME
===================
The whole game is written in Python and consists of three files (make sure that they are  in the same directory): 

1.TwentyFortyEight.py, which contains the game logic
2.2048GUI.py, the graphical user interface created with the Tkinter module
3.owl.gif, the gif image of an owl used in the design of the GUI

steps to run the game:

1.Run "2048GUI.py"
2.Use the arrow keys to swipe the tiles in different directions (up, down, left and right)
3.Click on the "Best Scores" button to see the top five scores
4.Click on the "New Game" button to start a new game


ADDITIONAL INFORMATION
======================
1.The implementation of this version of 2048 is purely based on the game logic instead of the source code of the Cirulli version, therefore all the code is original;

2.(Almost)Every class and the methods contained in the class has a string that describe the primary function of the class/method. There are also plenty of comments in the code that explain the code in detail; 

3.Due to a failed (or not-as-successful-as-expected...) attempt to create an optimized AI that automatically runs the game, there's some code commented out in TwentyFortyEight.py, including the method for caculating the heuristic score of every game state and the function for choosing the next direction based on the evaluation of the predicted result of each move. If needed, uncomment the "print(Run2048())" command (for Python 2, delete the parentheses around "Run2048()") in TwentyFortyEight.py. Then run the script for NO MORE THAN TWICE (otherwise the program freezes for some reason that I have yet to figure out)to see the text-based result;

4.The game has already been tested and it functions well although some features are not quite the same as the Cirulli version;

5.If you don't like the colors of the game board, tiles or text, feel free to change them (it's very convenient);

6.Contact info:
    Rachel Xu
    Bryn Mawr College
    rxu1@brynmawr.edu