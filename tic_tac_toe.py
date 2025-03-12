import tkinter

#game standards
player1 = "X"
player2 = "O"
current_player = player1
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
colour_red = "FF0000"
colour_blue = "0000FF"
colour_gray = "#808080"
colour_light_gray = "#D3D3D3"

 #the window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player +"'s turn", font=("Consolas", 20), background=colour_gray, foreground="white")

label.grid()
label.coloum()

window.mainloop()