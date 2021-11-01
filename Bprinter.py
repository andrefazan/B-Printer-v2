

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


# reading folder directory backup
with open(r'backup-directory.txt', 'r') as f:
        folder_location_program = f.readline() 
f.close()

# ask for folder location and change it in the entry. Also create a backup for it.
def get_the_folder_location():
    folder_location_program = filedialog.askdirectory()
    label_where_to_save.delete(0, END)
    label_where_to_save.insert(INSERT, folder_location_program)    
    with open(r'backup-directory.txt', 'w') as f:
        f.write(folder_location_program)  
    f.close()


# starting interface
root = Tk()
root.title('B. PRINTER')
root.geometry("530x460+500+300")
root.resizable(False,False)
#root.iconbitmap(r"D:\Desktop\Fresh Python\Projects_1\Bronha Printer v2\download.ico")

#               tkinter interface lines
#line 0
label_version_text = Label(root, text='version 2.0', fg="blue4").grid(row= 0, column=0)
#line 1
base_img_logo = os.path.dirname(__file__)
logo_img_path = os.path.join(base_img_logo, 'new-logo-img.png')
logo_img = PhotoImage (file = logo_img_path)

base_img_title = os.path.dirname(__file__)
logo_img_title_path = os.path.join(base_img_title, 'title.png')
logo_title = PhotoImage (file = logo_img_title_path)

label_logo_title = Label(root, image= logo_title, compound='top' ).grid(row=1, column=2)
label_logo_img = Label(root, image= logo_img, compound='top' ).grid(row=0, column=3, rowspan=2)
#line 2
label_where_to_save = Entry(root, width=60)
label_where_to_save.grid(row=2, column=1, columnspan=4)
label_where_to_save.insert(INSERT, folder_location_program)
#line 3
button_change_directory = Button(text="Change Directory", command= lambda : get_the_folder_location()).grid(row=3, column=2)
#line 5
label_space_row_4 = Label(root, text ='').grid(row=4, column=0)
#line 4
label_folder_name = Label(root, text ='Folder').grid(row=5, column=1)
#line 6
text_prints_prog = Entry(root, width=17)
text_prints_prog.grid(row=6, column=1)
text_prints_prog.insert(INSERT, 'PRINTS-PROG-V')
#_row 6 column 2
check_button_desk = Checkbutton(text='Screenshot Desk', bg ="gray80")
check_button_desk.grid(row=6, column=2)
check_button_desk.select()
check_button_mobile = Checkbutton(text='Screenshot Mobile', bg ="gray80").grid(row=6, column=3)
#line 7
label_space_row_7 = Label(root, text ='').grid(row=7, column=0)
#line 8
label_print_name = Label(root, text ='Name').grid(row=8, column=1)
label_url = Label(root, text ='URL').grid(row=8, column=2)
#line 9
text_prints_prog = Entry(root, width=15).grid(row=9, column=1)
text_prints_prog = Entry(root, width=30).grid(row=9, column=2)
#line 10
text_prints_prog = Button(root, text='RUN', width=10).grid(row=9, column=3, sticky='w')
label_space_row_10 = Label(root, text ='').grid(row=10, column=0)
#line 11
label_infos = Listbox(root, height=8, width=50, fg="blue4", bg ="gray80")
label_infos.grid(row= 11, column=1, columnspan=2, sticky='w')
button_zip_file = Button(root, text='Zip Files').grid(row=11, column=3)

#label_infos.insert(1, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(2, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(3, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(4, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(5, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(6, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(7, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(8, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
#label_infos.insert(9, 'PRINTS-PROG-Vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

root.mainloop()
