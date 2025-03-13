import tkinter
def set_tile(row,column):
    pass
def new_game(row,column):
    pass
#game standards
player1 = "X"
player2 = "O"
current_player = player1
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
colour_red = "#FF0000"
colour_blue = "#0000FF"
colour_gray = "#808080"
colour_light_gray = "#D3D3D3"

 #the window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player +"'s turn", font=("Consolas", 20), background=colour_gray, foreground="white")

label.grid(row=0, column=0)

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), background=colour_gray, foreground = colour_blue, width = 4, height = 1,
                                             command = lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row= row + 1, column = column)

button = tkinter.Button(frame, text = "restart", font=("Consalas", 20), background = colour_gray, 
                        foreground = "white", command = new_game)
button.grid(row=4, column=0)
frame.pack


window.mainloop()