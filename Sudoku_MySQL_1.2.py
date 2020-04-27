from tkinter import *
from tkinter import messagebox
import os
import random
import webbrowser
import mysql.connector as sql


class Box:

    def __init__(self, root):

        # Main Window

        self.root = root
        root.title("Sudoku")
        root.resizable(False, False)

        # Default Connection Properties

        self.host = "localhost"
        self.username = "root"
        self.password = ""

        # Manual Connection Properties

        config_exists = os.path.isfile("mysql_config.txt")
        if config_exists:
            config = open("mysql_config.txt", "r")
            read_save = config.read()
            list_items = read_save.split("\n")
            if len(list_items[3]) != 0:
                self.host = list_items[3]
            if len(list_items[5]) != 0:
                self.username = list_items[5]
            if len(list_items[7]) != 0:
                self.password = list_items[7]
        else:
            pass

        # Database Connection

        try:
            self.my_db = sql.connect(
                host=f"{self.host}",
                user=f"{self.username}",
                passwd=f"{self.password}"
            )

        # Connection Error Window

        except:
            self.root.title("Error")
            self.root.geometry("200x30")
            error_message = Label(self.root, text="Incorrect credentials for MySQL")
            error_message.pack(fill="y", expand="1")
            self.root.mainloop()
            quit()

        # Setting Database and Cursor

        self.c = self.my_db.cursor()
        self.c.execute("use sudoku")

        # Flag

        self.c.execute("select gno from start")
        s_gno = self.c.fetchall()
        self.l_gno = []
        for x in s_gno:
            self.l_gno.append(x[0])
        self.flag = random.choice(self.l_gno)
        self.str_flag = str(self.flag)

        # Game Lists

        self.start = []
        self.game = []
        self.game_solved = []

        # Buttons List

        self.boxes = []

    # Populating Lists

    def flag_copy(self, no):

        # Start List

        self.c.execute(f"select * from start where gno={no}")
        fetch = list(self.c.fetchall()[0])
        fetch.pop(0)
        self.start = fetch.copy()

        # Game List

        self.game = self.start.copy()

        # Game Solved List

        self.c.execute(f"select * from solved where gno={no}")
        s_fetch = list(self.c.fetchall()[0])
        s_fetch.pop(0)
        self.game_solved = s_fetch.copy()

    # Releases

    def releases(self):
        webbrowser.open_new("https://github.com/VarunS2002/Python-Sudoku-MySQL/releases/")
        self.info.attributes('-topmost', False)

    # Sources

    def sources(self):
        webbrowser.open_new("https://github.com/VarunS2002/Python-Sudoku-MySQL/")
        self.info.attributes('-topmost', False)

    # Choose Game Window

    def choose_window(self):
        self.window = Toplevel()
        self.window.title("Choose")
        self.window.resizable(False, False)
        self.window.geometry('220x200')
        self.window.attributes('-topmost', True)
        self.window.grab_set()
        self.window.focus_force()
        return self.window

    # Choose Game Ok Button

    def do_ok(self):
        self.flag = self.listbox.get(ACTIVE)
        self.flag_copy(self.flag)
        self.str_flag = str(self.flag)
        self.new()
        self.window.destroy()

    # Choose Game Cancel Button

    def do_cancel(self):
        self.window.destroy()

    # Choose Game Function

    def choose_game(self):
        self.window = self.choose_window()
        self.listbox = Listbox(self.window)
        for x in self.l_gno:
            self.listbox.insert(END, x)
        self.listbox.focus_force()
        button_frame = Frame(self.window)

        ok = Button(button_frame, command=self.do_ok, text="Ok")
        ok.pack(side='left', fill='x', expand='1')

        cancel = Button(button_frame, command=self.do_cancel, text="Cancel")
        cancel.pack(side='right', fill='x', expand='1')

        self.listbox.pack(side='top', fill='both', expand='1')
        button_frame.pack(side='top', fill='x', expand='1')

        self.window.mainloop()

    # Choose Number Function

    def choose(self, btn_index):
        get_text = self.boxes[btn_index]['text']
        set_text = (get_text % 9) + 1
        self.boxes[btn_index].config(text=set_text)
        self.game[btn_index] = set_text

    # Restart Game Function

    def new(self):
        self.game = self.start.copy()
        for z in range(81):
            self.boxes[z].config(text=self.game[z])
            if self.game[z] == 0:
                self.boxes[z].config(state=NORMAL)
                self.text_colour = "blue"
            else:
                self.text_colour = "black"
                self.boxes[z].config(state=DISABLED)
            self.boxes[z].config(fg=self.text_colour)

        # Setting Option Menu Attributes

        self.options.entryconfig(self.options.index(0), label=f"Choose Game: {self.str_flag}")
        self.options.entryconfig(self.options.index("Check Result"), state=NORMAL)

    # Check Result Function

    def check(self):
        if self.game == self.game_solved:
            messagebox.showinfo("Result", "You won")
        else:
            messagebox.showinfo("Result", "You lost")

    # Show Solution Function

    def sol(self):
        for z in range(81):
            self.boxes[z].config(text=self.game_solved[z], state=DISABLED)

        # Setting Option Menu Attributes

        self.options.entryconfig(self.options.index("Check Result"), state=DISABLED)

    # About Window

    def about_window(self):
        self.info = Toplevel()
        self.info.title("About")
        self.info.resizable(False, False)
        self.info.geometry('220x100')
        self.info.attributes('-topmost', True)
        self.info.grab_set()
        self.info.focus_force()
        return self.info

    # About Function

    def about(self):
        self.info = self.about_window()

        version = Label(self.info, text="Version: 1.2")
        version.pack(side='top', pady="5")
        release = Button(self.info, text="Releases", fg="blue", cursor="hand2", borderwidth=0, command=self.releases)
        release.pack(side='top', pady="5")
        source = Button(self.info, text="Sources", fg="blue", cursor="hand2", borderwidth=0, command=self.sources)
        source.pack(side='top', pady="5")

        self.info.mainloop()

    # Quit Function

    def close(self):
        ask_quit = messagebox.askyesno("Quit", "Do you want to quit?")
        if ask_quit:
            quit()
        elif not ask_quit:
            pass

    # Grid Function

    def grid(self):
        i = 0
        k = 0

        for rowindex in range(9):

            for colindex in range(9):

                # Setting Grid Color

                if rowindex in (0, 1, 2, 6, 7, 8) and colindex in (3, 4, 5):
                    bg_colour = "light grey"
                elif rowindex in (3, 4, 5) and colindex in (0, 1, 2, 6, 7, 8):
                    bg_colour = "light grey"
                else:
                    bg_colour = "white"

                # Iterating Start List

                value = self.start[k]
                k = k + 1

                # Setting Text Color

                if value == 0:
                    self.text_colour = "blue"
                else:
                    self.text_colour = "black"

                # Adding Button Objects to List

                self.boxes.append(i)

                # Creating Buttons

                self.boxes[i] = Button(self.root, width=8, height=4, bg=bg_colour, fg=self.text_colour, text=value,
                                       command=lambda btn_index=i: self.choose(btn_index))
                self.boxes[i].grid(row=rowindex, column=colindex, sticky=N + S + E + W)

                # Setting Text Color

                if self.text_colour == 'black':
                    self.boxes[i].config(state=DISABLED)

                # Increasing Value of i for Iteration

                i += 1

    # Option Menu Function

    def create_menu(self):
        menubar = Menu(self.root)
        self.options = Menu(menubar, tearoff=0)
        self.options.add_command(label=f"Choose Game: {self.str_flag}", command=self.choose_game)
        self.options.add_command(label="Restart Game", command=self.new)
        self.options.add_separator()
        self.options.add_command(label="Check Result", command=self.check)
        self.options.add_command(label="Show Solution", command=self.sol)
        self.options.add_separator()
        self.options.add_command(label="About", command=self.about)
        self.options.add_command(label="Quit", command=self.close)
        menubar.add_cascade(label="Menu", menu=self.options)

        # Setting Main Window Attributes

        self.root.config(menu=menubar)
        self.root.protocol('WM_DELETE_WINDOW', self.close)


if __name__ == "__main__":
    master = Tk()
    box_instance = Box(master)
    box_instance.flag_copy(box_instance.flag)
    box_instance.grid()
    box_instance.create_menu()
    master.mainloop()
