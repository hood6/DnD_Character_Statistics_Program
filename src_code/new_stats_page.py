from tkinter import Tk, Label, Button, Entry


# Notes:
# - I could place many of the labels and entry fields in other labels or frames
#   to make it easier to place them within the main window
class StatsEntryWindow:
    """
    This is the entry page where Dungeons & Dragons players can enter their
    statistics for a new character. When called, this class will open a tkinter
    window where they can enter their statistics

    Soon to be added functionality:
    - Level characters here
    - Buttons to go to stats page and dice roller
    """
    # Dictionary that keeps track of the text, row, and column of each label
    labels = {"Name:": [0, 0],
              "Race:": [0, 2],
              "Class:": [1, 2],
              "Level:": [2, 2],
              "Exp:": [0, 4],
              "Strength:": [3, 0],
              "Dexterity:": [4, 0],
              "Constitution:": [5, 0],
              "Intelligence:": [3, 2],
              "Wisdom:": [4, 2],
              "Charisma:": [5, 2],
              "Proficiency:": [3, 4],
              "Initiative:": [4, 4],
              "Speed:": [5, 4],
              "Health:": [6, 0],
              "Armor Class:": [7, 0],
              "Hit Die:": [8, 0]}

    # Dictionary that keeps track of the key, row, and column of each entry
    # field
    entries = {"NAME": [0, 1],
               "RACE": [0, 3],
               "CLASS": [1, 3],
               "LVL": [2, 3],
               "EXP": [0, 5],
               "STR": [3, 1],
               "DEX": [4, 1],
               "CON": [5, 1],
               "INT": [3, 3],
               "WIS": [4, 3],
               "CHAR": [5, 3],
               "PROF": [3, 5],
               "INITIATIVE": [4, 5],
               "SPD": [5, 5],
               "HEAL": [6, 1],
               "AC": [7, 1],
               "HITDIE": [8, 1]}

    # Empty dictionary that will keep track of the values typed into each
    # entry field
    entry_submit_values = {}

    # Maximum row and column values
    MAX_COL = 5
    MAX_ROW = 9

    def __init__(self):
        """
        Sets up the page. Window is set at the root window, then the set_label,
        set_entries, and set_button are called to initialized all of the labels,
        entry fields, and the button to submit all of the data.
        """
        self.window = Tk()
        self.set_label(self.window)
        self.set_entries(self.window)
        self.set__submit_button(self.window)
        self.window.mainloop()

    def set_label(self, root):
        """
        Sets up all of the labels throughout the window. The labels dictionary
        is used to format all of the labels created by this method. Padding is
        assigned based on whether the label falls next to the border of the
        window or if they fall near another stat block.

        :param root: Main window that the labels will be contained in
        """
        # key == label text, value = row and column number
        for key, value in self.labels.items():
            if value[1] is 0:
                padding_x = (0, 0)
            else:
                padding_x = (50, 0)
            if value[0] is 2 or value[0] is 5:
                padding_y = (0, 25)
            else:
                padding_y = (0, 0)
            # [0] is row, [1] is column
            Label(root, text=key).grid(row=value[0],
                                       column=value[1],
                                       padx=padding_x,
                                       pady=padding_y)

    def set_entries(self, root):
        """
        Sets up all of the entry fields throughout the window. The labels dictionary
        is used to format all of the labels created by this method. Padding is
        assigned based on whether the field falls next to the border of the
        window or if they fall near another stat block. The data contained
        within the fields is also assigned to a dictionary so that they can
        be retrieved when it is time to place the data in a text file.

        :param root: Main window that the entry fields will be contained in
        """
        # key == entry name, value == row and column number
        for key, value in self.entries.items():
            if value[1] is 4:
                padding_x = (0, 0)
            else:
                padding_x = (0, 50)
            if value[0] is 2 or value[0] is 5:
                padding_y = (0, 25)
            else:
                padding_y = (0, 0)
            # [0] is row, [1] is column
            self.entry_submit_values[key] = Entry(root)
            self.entry_submit_values[key].grid(row=value[0],
                                               column=value[1],
                                               padx=padding_x,
                                               pady=padding_y)

    def set_submit_button(self, root):
        """
        Sets the button to the bottom of the window. When this button is
        clicked, the data from the entry fields is recorded in a text file,
        which can be accessed by other windows. When the file is created,
        it is named after the character's name (Paul will become paul.txt)

        :param root: Main window that the entry fields will be contained in
        """
        submit_button = Button(root,
                               text="Submit Character",
                               command=self.send_to_file)
        submit_button.grid(row=self.MAX_ROW,
                           column=self.MAX_COL)

    def send_to_file(self):
        """
        Sends data to a new text file
        """
        # print(self.entry_submit_values["NAME"].get())
        # print(self.entry_submit_values["HITDIE"].get())
        # TODO add save feature

    def load_file(self):
        return
        # TODO add load feature


# Testing the class
if __name__ == "__main__":
    print("not button, ignore")
    StatsEntryWindow()
