

#libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import shutil
import threading
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



text_test = '1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'



def get_the_folder_location():
    folder_location_program = filedialog.askdirectory()
    return(folder_location_program)



root = Tk()
root.title('B. PRINTER')
root.geometry("530x460+500+300")
root.resizable(False,False)
#root.iconbitmap(r"D:\Desktop\Fresh Python\Projects_1\Bronha Printer v2\download.ico")






label_version_text = Label(root, text='version 2.0', fg="blue4").grid(row= 0, column=0)

#image 
logo_img = PhotoImage (file = r"D:\Desktop\Fresh Python\Projects_1\Bronha Printer v2\title.png")
label_logo_img = Label(root, image= logo_img ).grid(row=1, column=2)

label_where_to_save = Label(root, text='D:\Desktop\Fresh Python\Projects_1\Bronha Printer v2\title.png\ ', width=60).grid(row=2, column=1, columnspan=4)

button_change_directory = Button(text="Change Directory", command= lambda : get_the_folder_location()).grid(row=3, column=2)

label_space_row_4 = Label(root, text ='').grid(row=4, column=0)
label_folder_name = Label(root, text ='Folder').grid(row=5, column=1)

text_prints_prog = Entry(root, width=17)
text_prints_prog.grid(row=6, column=1)
text_prints_prog.insert(INSERT, 'PRINTS-PROG-V')
#_row 6 column 2
check_button_desk = Checkbutton(text='Screenshot Desk', bg ="gray80")
check_button_desk.grid(row=6, column=2)
check_button_desk.select()
check_button_mobile = Checkbutton(text='Screenshot Mobile', bg ="gray80").grid(row=6, column=3)

label_space_row_7 = Label(root, text ='').grid(row=7, column=0)

label_print_name = Label(root, text ='Name').grid(row=8, column=1)
label_url = Label(root, text ='URL').grid(row=8, column=2)

text_prints_prog = Entry(root, width=15).grid(row=9, column=1)
text_prints_prog = Entry(root, width=30).grid(row=9, column=2)
text_prints_prog = Button(root, text='RUN', width=10).grid(row=9, column=3, sticky='w')

label_space_row_10 = Label(root, text ='').grid(row=10, column=0)

label_infos = Listbox(root, height=8, width=50, fg="blue4", bg ="gray80")
label_infos.grid(row= 11, column=1, columnspan=2, sticky='w')

label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
label_infos.insert(END, text_test)
button_zip_file = Button(root, text='Zip Files').grid(row=11, column=3)


root.mainloop()



