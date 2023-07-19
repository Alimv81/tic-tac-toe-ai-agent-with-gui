from tkinter import *
from tkinter import messagebox
from tkinter import ttk as ttk
from utils.algorithms import *

play_as_X = False


def set_first_player(f, c):
    global play_as_X
    play_as_X = c
    f.destroy()


def run_ask_page():
    ask_page = Tk()
    b1 = Button(ask_page, text='play as X', command=lambda: set_first_player(ask_page, True), background='#266e39')
    b1.pack(pady=20)
    b1.config(height=2, width=70)

    b2 = Button(ask_page, text='play as O', command=lambda: set_first_player(ask_page, False), background='#266e39')
    b2.pack(pady=20)
    b2.config(height=2, width=70)

    l1 = Label(ask_page, text='the player with X annotation will \n begin the match',
               foreground='#cc1b38', font=("Arial", 15), background='black')
    l1.pack(pady=20)
    l1.config(height=2, width=70)

    ask_page.title('choosing pin')
    ask_page.geometry('300x300+800+300')
    ask_page.config(background='black')
    ask_page.resizable(False, False)
    ask_page.mainloop()


def run_game_page():
    root = Tk()

    root.config(background='black')
    root.geometry("600x650+600+200")

    bg = PhotoImage(file="data/board_image_re.png", height=600, width=600)

    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    cmr = ttk.Combobox(root, )
    cmr['values'] = ['row 1', 'row 2', 'row 3']
    cmr.place(x=30, y=615)
    cmr.config(width=10)
    cmr.current(0)

    cmc = ttk.Combobox(root, )
    cmc['values'] = ['column 1', 'column 2', 'column 3']
    cmc.place(x=150, y=615)
    cmc.config(width=10)
    cmc.current(0)

    exit_button = Button(root, text="Exit", command=lambda: root.destroy(),
                         font=('Arial', 15), foreground='red', background='#0b1aa1')
    exit_button.place(x=500, y=605)
    exit_button.config(height=1, width=5)

    bg_o = PhotoImage(file="data/o_player_re.png", height=100, width=95)
    bg_x = PhotoImage(file="data/x_player_re.png", height=100, width=100)

    if not play_as_X:
        row, column = ai_move(board)
        player_label = Label(root, image=bg_x)
        player_label.place(x=column * 150 + 100, y=row * 175 + 80)

    def place_player(row, column, player_x):
        if board[row*3 + column] == ' ':
            if len(get_available_moves(board)) == 0:
                messagebox.showinfo(title='Statues', message='no one has won!')
                root.destroy()
            else:
                player_label = Label(root, image=bg_x if player_x else bg_o)
                player_label.place(x=column * 150 + 100, y=row * 175 + 80)
                board[row*3 + column] = -1
                if check_win(board, -1):
                    messagebox.showinfo(title='Statues', message='YOU HAVE WON!')
                    root.destroy()

            if len(get_available_moves(board)) == 0:
                messagebox.showinfo(title='Statues', message='no one has won!')
                root.destroy()
            else:
                row, column = ai_move(board)
                player_label = Label(root, image=bg_x if not player_x else bg_o)
                player_label.place(x=column * 150 + 100, y=row * 175 + 80)
                if check_win(board, 1):
                    messagebox.showinfo(title='Statues', message='YOU HAVE LOST!')
                    root.destroy()

    place = Button(root, text="place", command=lambda: place_player(cmr.current(), cmc.current(), play_as_X),
                   font=('Arial', 15), foreground='#1fc296', background='#0b1aa1')
    place.place(x=300, y=605)
    place.config(height=1, width=5)

    root.resizable(False, False)
    root.mainloop()
