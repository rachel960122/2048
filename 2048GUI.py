"""
Created by Rachel Xu, last updated on 05/01/2015
"""
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import * 
from TwentyFortyEight import *
from random import *
from copy import deepcopy
import math

class TwentyFortyEight_GUI():
    """
    Class to run the 2048 game GUI.
    """
    def __init__(self, twentyfortyeight):
        self.TFE = twentyfortyeight
        self.window = Tk()
        self.window.title("2048 by Rachel Xu")
        self.window.bind_all("<Key>", self.key_pressed)
        self.canvas1 = Canvas(self.window, bg = "misty rose", width = 300, height = 60)
        self.canvas2 = Canvas(self.window, bg = "seashell", width = 300, height = 280)
        self.button1 = Button(self.canvas2, text="Best Scores", anchor=NW, bg="orange", font=("Comic Sans MS", 9, "bold"), bd = 0, command=self.display_best_scores)
        self.button2 = Button(self.canvas2, text="New Game", anchor=NE, bg="coral", font=("Comic Sans MS", 9, "bold"), bd = 0, command=self.reset)
        self.photo = PhotoImage(file="owl.gif")
        self.draw_game_init()
        self.update_tiles()
        

    def draw_game_init(self):
        """
        Create items on the two canvases.
        """
        self.canvas1.pack()
        self.canvas2.pack()
        
        #coordinates
        x1,y1,x2,y2 = 50,50,250,50
        
        #contents of canvas1
        #the owl pic
        i = self.canvas1.create_image(50, 30, image=self.photo)
        #the 2048 title
        self.canvas1.create_text(112, 31, text="2", font=("Impact", 32, "bold"))
        self.canvas1.create_text(142, 31, text="0", font=("Impact", 32, "bold"))
        self.canvas1.create_text(172, 31, text="4", font=("Impact", 32, "bold"))
        self.canvas1.create_text(202, 31, text="8", font=("Impact", 32, "bold"))
        self.canvas1.create_text(110, 30, text="2", fill = "SkyBlue1", font=("Impact", 32))
        self.canvas1.create_text(140, 30, text="0", fill = "yellow", font=("Impact", 32))
        self.canvas1.create_text(170, 30, text="4", fill = "lime green", font=("Impact", 32))
        self.canvas1.create_text(200, 30, text="8", fill = "orange", font=("Impact", 32))
        #the "score" text
        self.canvas1.create_text(260, 16, text="SCORE", font=("Comic Sans MS", 12, "bold"))
        #the actual score
        self.canvas1.create_text(260, 40, text="0", font=("Comic Sans MS", 12, "bold"), tag="score")


        #contents of canvas2
        #the "best scores" button
        self.canvas2.create_window(87,26, window=self.button1)
        #the "new game" button
        self.canvas2.create_window(219,26, window=self.button2)
        #the background of canvas2
        self.canvas2.create_rectangle(50, 50, 250, 250, fill = "lavender blush", outline = "lavender blush")
        #the grid lines
        for i in range(5):
            #horizontal lines
            self.canvas2.create_line(x1-2, x1+i*50, x2+3, y2+i*50, fill="hot pink", width=5, smooth=1)
            #vertical lines
            self.canvas2.create_line(x1+i*50, y1, x1+i*50, x2, fill="hot pink", width=5, smooth=1)


    def update_tiles(self):
        """
        Update and display the tiles after each move.
        """

        #clear the original tiles
        self.canvas2.delete("rect")
        self.canvas2.delete("text")

        #text color of tiles with different numbers
        color_dic = {
            2:"LightBlue1",
            4:"SkyBlue1",
            8:"DeepSkyBlue",
            16:"RoyalBlue1",
            32:"RoyalBlue3",
            64:"blue2",
            128:"blue4",
            256:"dark green",
            512:"forest green",
            1024:"lawn green",
            2048:"yellow",
            4096:"orange",
            8192:"dark orange"
            }

        #coordinates of the tile at row 0, col 0
        x, y, z, w = 53, 53, 97, 97
        #create all the tiles based on the coordinates above
        for i in range(self.TFE.numRow):
            for j in range(self.TFE.numCol):
                value = self.TFE.grid[i][j]
                if value != 0:
                    self.canvas2.create_rectangle(x+j*50, y+i*50, z+j*50, w+i*50, fill = color_dic[value], outline = color_dic[value], tag="rect")
                    self.canvas2.create_text((x+z+j*100)/2, (y+w+i*100)/2, fill = "white", text = str(value), font=("Impact", 16), tag="text")


    def update_score(self):
        """
        Update and display the score after each move.
        """
        self.canvas1.delete("score")
        self.canvas1.create_text(260, 40, text=str(self.TFE.actualScore), font=("Comic Sans MS", 12, "bold"), tag="score")


    def reset(self):
        """
        Reset the game board to start a new game.
        """
        self.TFE.reset()
        self.update_score()
        self.update_tiles()


    def key_pressed(self, event):
        """
        Method to associate keyboard actions with the update of the game state.
        """
        key = event.keysym
        #each arrow kwy corresponds to a direction
        if key in ["Up", "Down", "Left", "Right"]:
            try:
                direction = key.upper()
                self.TFE.move(direction)
                self.update_score()
                self.update_tiles()
                #display "Game Over" and the score when the game board reaches the final state
                #record the score each time and update the list of the best five scores
                if self.TFE.game_over():
                    if len(self.TFE.bestScores) < 5:
                        self.TFE.bestScores.append(self.TFE.actualScore)
                    else:
                        mins = min(self.TFE.bestScores)
                        if self.TFE.actualScore > mins:
                            self.TFE.bestScores[self.TFE.bestScores.index(mins)] = self.TFE.actualScore
                    tv = "Your score is %d"%(self.TFE.actualScore)
                    self.window.update()
                    d = dialog(self.canvas2, self, tv)
                    self.window.wait_window(d.top)
            except:
                pass
            

    def display_best_scores(self):
        """
        Method to display the top five scores.
        """
        self.window.update()
        d = dialog2(self.canvas2, self, self.TFE.bestScores)
        self.window.wait_window(d.top)
        

    def run2048(self):
        """
        Method to run the game according to certain rules.
        """
        self.reset()
        while not self.TFE.game_over():
            for dir in ['DOWN', 'LEFT', 'DOWN', 'RIGHT']:
                try:
                    self.TFE.move(dir)
                    self.update_score()
                    self.update_tiles()
                except:
                    pass
        
        
        tv = "Your score is %d"%(self.TFE.actualScore)
        self.window.update()
        d = dialog(self.canvas2, self, tv)
        self.window.wait_window(d.top)

    def exit_game(self):
        self.window.destroy()

class dialog():
    """
    Class to create a dialog when the game is over.
    """
    def __init__(self, parent, GUI, tv):
        self.top = Toplevel(master=parent, bg = "pink", bd = 0)
        self.GUI = GUI
        Label(self.top, text = "GAME OVER", bg = "pink", font = ("Comic Sans MS", 16, "bold"), anchor=S).pack()
        Label(self.top, text = tv, bg = "pink", font = ("Comic Sans MS", 14, "bold"), anchor = N, height = 2).pack()
        
        button1 = Button(self.top, text = "Play Again", width = 11, height = 2, bg = "lavender", font = ("Comic Sans MS", 9, "bold"), command = self.reset_and_exit)
        button1.pack(side=LEFT)
        button2 = Button(self.top, text = "Exit 2048", width = 11, height = 2, bg = "lavender", font = ("Comic Sans MS", 9, "bold"), command = self.GUI.window.destroy)
        button2.pack(side=RIGHT)
        
    def reset_and_exit(self):
        self.GUI.reset()
        self.top.destroy()
                    
class dialog2():
    """
    Class to create a dialog to display the top five scores when the "Best Scores" button is clicked.
    """
    def __init__(self, parent, GUI, scorelist):
        self.GUI = GUI
        self.bestScores = sorted(scorelist, reverse = True)
        self.top = Toplevel(master=parent, bg = "pink", bd = 0)
        
        Label(self.top, text = "Top Five Scores", bg = "pink", font = ("Comic Sans MS", 16, "bold"), anchor=S).pack()

        #iterate over the list of five scores and display each score
        for score in self.bestScores:
            Label(self.top, text = score, fg = "deep pink", bg = "pink", font = ("Comic Sans MS", 14, "bold"), anchor=S).pack()
            
        button1 = Button(self.top, text = "Back to the Game", width = 15, height = 1, bg = "lavender", font = ("Comic Sans MS", 9, "bold"), command = self.top.destroy)
        button1.pack()

        
if __name__ == "__main__":
	# create the TwentyFortyEight class instance
	twentyfortyeight = TwentyFortyEight(4, 4)
	my2048GUI = TwentyFortyEight_GUI(twentyfortyeight)
	mainloop()
