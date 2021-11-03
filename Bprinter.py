

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
import sys


#count test threading in webdriver
counter = [0]
new_driver = 'driver'

#web driver config
options = webdriver.ChromeOptions()
options.headless = True


#using sys to get the path to the backup folder location txt file
location_backup_txt = '{}/backup-folder-location.txt'.format(sys.path[0])


# reading folder directory backup
with open(location_backup_txt, 'r') as f:
        folder_location_program = f.readline() 
f.close()

# ask for folder location and change it in the entry. Also create a backup for it.
def get_the_folder_location():
    folder_location_program = filedialog.askdirectory()
    label_where_to_save.delete(0, END)
    label_where_to_save.insert(INSERT, folder_location_program)    
    with open(location_backup_txt, 'w') as f:
        f.write(folder_location_program)  
    f.close()

def test_thread():
    print(0)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(5)



def add_more_one(new_driver):
    return new_driver + 1

def change_new_driver(new_driver):
    global counter
    return new_driver + str(len(counter))


#screenshot function
def make_a_full_screenshot(counter): 
    global new_driver

    counter.append(1)
    new_driver = change_new_driver(new_driver)     
    print(new_driver)   
    make_print_and_close_driver(new_driver)

        


def make_print_and_close_driver(driver):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)             
    driver.get('https://www.emkt.cantasys.com.br/dados/16/emkts/37899/v7/')      
    link = (r'C:\Users\andre\Desktop\test.png')
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(650, S('Height'))

    #function that ensures all images are loaded
    number_of_images_in_the_website = driver.execute_script('return document.images.length')

    images_loading = True
    while images_loading == True:         
        need_wait = False     
        for i in range(number_of_images_in_the_website - 1):
            image = driver.execute_script('return document.images[{}].complete'.format(int(i+1)))
            if image != True:
                need_wait = True

        if need_wait == False:
            driver.find_element_by_tag_name('body').screenshot(link)
            driver.quit()
           

def start_new_thread():
    threading.Thread(target= make_a_full_screenshot, args=[counter]).start()






# starting interface
root = Tk()
root.title('B. PRINTER')
root.geometry("530x460+500+300")
root.resizable(False,False)
#root.iconbitmap(r"D:\Desktop\Fresh Python\Projects_1\Bronha Printer v2\download.ico")

#               tkinter interface lines
#line 0
base_img_logo = os.path.dirname(__file__)
logo_img_path = os.path.join(base_img_logo, 'new-logo-img.png')
logo_img = PhotoImage (file = logo_img_path)
label_logo_img = Label(root, image= logo_img, compound='top' ).grid(row=0, column=1, rowspan=2)
#line 1
base_img_title = os.path.dirname(__file__)
logo_img_title_path = os.path.join(base_img_title, 'title.png')
logo_title = PhotoImage (file = logo_img_title_path)
label_logo_title = Label(root, image= logo_title, compound='top' ).grid(row=1, column=2)
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
text_prints_prog = Button(root, text='RUN', width=10,  command=start_new_thread).grid(row=9, column=3, sticky='w')
label_space_row_10 = Label(root, text ='').grid(row=10, column=0)
#line 11
label_infos = Listbox(root, height=8, width=50, fg="blue4", bg ="gray80")
label_infos.grid(row= 11, column=1, columnspan=2, sticky='w')
button_zip_file = Button(root, text='Zip Files', command= lambda: make_a_full_screenshot(counter))
button_zip_file.grid(row=11, column=3)
#button_zip_file = Button(root, text='Zip Files', command=make_a_full_screenshot).grid(row=11, column=3)
#line 12
label_version_text = Label(root, text='version 2.2').grid(row= 12, column=0)



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
