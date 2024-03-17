"""
> Decorated text and alignment
> changed window color
> added Declaration
> can add multiple options via code
> perfected the line above and below info by length calculation
> To do :
   add the output(on the Run terminal) into a text file what?
   with open :) Done partially and completely
   did not do the custom file name thing Done
"""

from tkinter import *
from tkinter import filedialog

# ----- GLOBALS ------------
FILE = "Info_collector.txt"


# ----- END GLOBALS ------------


# ---------------- METHODS ----------------------------------------------------------------------
def file_location():
    """
    change file_location
    :return: None
    """
    file = filedialog.asksaveasfile(defaultextension=".txt")
    if file is None:
        return
    else:
        global FILE
        FILE = file.name


def check_info() -> bool:
    """
    checks if required fields are empty
    :return: true if valid
    """
    if firstname_entry.get() != "" and address_entry.get() != "" and post_entry.get() != "" and email_entry.get != "":
        return True
    else:
        return False


def submit():
    """
    put all info in a text file
    :return: None
    """
    if check_info():
        intro = ("=" * 10 + " Info:{} ".format(firstname_entry.get().capitalize()) + "=" * 10)
        name = ("Name    : {}".format(firstname_entry.get().capitalize(), lastname_entry.get()))
        email = ('E-Mail  : {}'.format(email_entry.get()))
        father = ('Father  : {}'.format(father_entry.get().capitalize()))
        address = ('Address : {}'.format(address_entry.get().capitalize()))
        post = ('post    : {}'.format(post_entry.get().capitalize()))
        outro = ("=" * 13 + "=" * (len(str(firstname_entry.get())) + 1) + "=" * 13)

        file_text = (
                intro + "\n" + name + "\n" + email + "\n" + father + "\n" + address + "\n" + post + "\n" + outro + "\n")

        with open(r"{}".format(FILE), 'a', encoding="utf8") as fp:
            fp.write(file_text)

        firstname_entry.delete(0, END)
        lastname_entry.delete(0, END)
        email_entry.delete(0, END)
        father_entry.delete(0, END)
        address_entry.delete(0, END)
        post_entry.delete(0, END)


# ---------------- END METHODS -----------------------------------------------------------------


# ================== MAIN WINDOW ===================================================
window = Tk()
window.config(background='#a94df4')
window.title("Info Collector")
window.resizable(False, False)

frame = Frame(window, relief=RAISED, bd=8)
frame.pack(pady=10, padx=10)

firstname_label = Label(frame, text="First Name : ", font=('Arial', 15))
firstname_label.grid(row=0, column=0)
firstname_entry = Entry(frame, font=('Consoles', 15, 'bold'))
firstname_entry.grid(row=0, column=1)

lastname_label = Label(frame, text="Last Name : ", font=('Arial', 15))
lastname_label.grid(row=1, column=0)
lastname_entry = Entry(frame, font=('Consoles', 15, 'bold'))
lastname_entry.grid(row=1, column=1)

address_label = Label(frame, text="Address     : ", font=('Arial', 15))
address_label.grid(row=2, column=0)
address_entry = Entry(frame, font=('Consoles', 15, 'bold'))
address_entry.grid(row=2, column=1)

post_label = Label(frame, text="Post office : ", font=('Arial', 15))
post_label.grid(row=3, column=0)
post_entry = Entry(frame, font=('Consoles', 15, 'bold'))
post_entry.grid(row=3, column=1)

father_label = Label(frame, text="Father       : ", font=('Arial', 15))
father_label.grid(row=4, column=0)
father_entry = Entry(frame, font=('Consoles', 15, 'bold'))
father_entry.grid(row=4, column=1)

email_label = Label(frame, text="E-mail        : ", font=('Arial', 15))
email_label.grid(row=5, column=0)
email_entry = Entry(frame, font=('Consoles', 15, 'bold'))
email_entry.grid(row=5, column=1)

Button(frame, text="Submit", command=submit, bg="pink", font=("Arial", 9, "bold")).grid(row=7, column=0, columnspan=2,
                                                                                        pady=5)
Button(frame, text="Save to", command=file_location, bg="pink", font=("Arial", 9, "bold")).grid(row=7, column=1, pady=5)

window.mainloop()

# ================== END MAIN WINDOW ===============================================
