from tkinter import *
import Scroller
from PIL import ImageTk, Image



def print_results(txt):
    txt.delete(1.0, END)
    txt.insert(INSERT, "results for: " + (str(keyword.get())) + "\n\n")
    noChoice = True
    if zap_bin.get() == 1:
        show_zap_results(txt)
        noChoice = False
    if od_bin.get() == 1:
        show_officeDepot_results(txt)
        noChoice = False
    if ivory_bin.get() == 1:
        show_ivory_results(txt)
        noChoice = False
    if noChoice:
        txt.insert(INSERT, "Please Choose Website")

def show_zap_results(txt):
    txt.insert(INSERT, "www.Zap.co.il \n\n")
    Scroller.search_results_zap(str(keyword.get()), Scroller.zapProductsList)
    if len(Scroller.zapProductsList) > 0:
        idx = 1
        for item in Scroller.zapProductsList:
            txt.insert(INSERT, str(idx) + ") " + item["title"] + "\t\t\t\t\t\t\t" + item["price"] + "\n")
            idx = idx + 1
    else:
        txt.insert(INSERT, "Oops... Nothing was found :(")

def show_officeDepot_results(txt):
        txt.insert(INSERT, "\n\nwww.OfficeDepot.co.il \n\n")
        Scroller.search_results_officeDepot(str(keyword.get()), Scroller.odProductList)
        if len(Scroller.odProductList) > 0:
            idx = 1
            for item in Scroller.odProductList:
                txt.insert(INSERT, str(idx) + ") " + item["title"] + "\t\t\t\t\t\t\t\t" + item["price"] + "\n")
                idx = idx + 1
        else:
            txt.insert(INSERT, "Oops... Nothing was found :(")


def show_ivory_results(txt):
    txt.insert(INSERT, "\n\nwww.ivory.co.il \n\n")
    Scroller.search_results_ivory(str(keyword.get()), Scroller.ivoryProductList)
    if len(Scroller.ivoryProductList) > 0:
          idx = 1
          for item in Scroller.ivoryProductList:
              space = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
              txt.insert(INSERT, str(idx) + ") " + item["title"] + space + item["price"] + "\n")
              idx = idx + 1
    else:
          txt.insert(INSERT, "Oops... Nothing was found :(")

# initiate Tkinter
root = Tk()
root.title("Prices Finder")
root.geometry("450x200+0+0")
root.configure(background='#4B4B4B')


zap_bin = IntVar()
od_bin = IntVar()
ivory_bin = IntVar()

# initiate Text widget
txt = Text(root, width=35, height=15, bg='#d6d6c2')
scrollbar = Scrollbar(root)
scrollbar.config(command=txt.yview)
txt.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
txt.pack(side=BOTTOM, fill=BOTH, expand=True)

# create frame
frame = Frame(root, bg='#4B4B4B')
lable = Label(frame, text="What would you like to buy?", font='bold', bg='#4B4B4B', fg='white')
keyword = StringVar()
entry = Entry(frame, textvariable=keyword, width='40', font='italic')
button = Button(frame, text="Search", command=lambda: print_results(txt), font='bold', bg='#2e2e1f', fg='white')
rights_lable = Label(txt, text="Created By Ido Finder ©", bg='#d6d6c2', fg='black')
img = ImageTk.PhotoImage(Image.open("logo-final2.gif"))
panel = Label(root, image=img, highlightthickness=0, borderwidth=0)
panel.pack(anchor=N)

# creating the checkbuttons
zap_check = Checkbutton(root, text="\t\tzap.co.il", variable=zap_bin, selectcolor='black', fg='white', bg='#4B4B4B',activebackground='light green')
od_check = Checkbutton(root, text="\tOfficedepot.co.il", variable=od_bin, selectcolor='black', fg='white', bg='#4B4B4B',activebackground='light green')
ivory_check = Checkbutton(root, text="\t\tIvory.co.il", variable=ivory_bin, selectcolor='black', fg='white', bg='#4B4B4B',activebackground='light green')

# packing all widgets
frame.pack()
zap_check.pack(anchor=NE)
od_check.pack(anchor=NE)
ivory_check.pack(anchor=NE)
lable.pack()
entry.pack()
button.pack()
rights_lable.pack(side=BOTTOM)


root.mainloop()
