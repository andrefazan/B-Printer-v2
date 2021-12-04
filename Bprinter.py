#native libraries
import sys
import threading
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import pip

#check if libraries are installed 
def check_if_library_selenium_are_installed():
    try:    
        from selenium import webdriver
        #test message
        print('ok selenium')
    except:
        pip.main(['install', 'selenium'])       

def check_if_library_webdrivermanager_are_installed():
    try:    
        from webdriver_manager.chrome import ChromeDriverManager
        #test message
        print('ok webdriver-manager')
    except:
        pip.main(['install', 'webdriver-manager'])       


#checking libraries
check_if_library_selenium_are_installed()
check_if_library_webdrivermanager_are_installed()


#importing non-native libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




#using a list because that can be changed in a functions D: (I dont know why, but the global call function didnt work)   (  D:  ) ** 2
counter = [0]
check_if_working = [0]
number_of_prints = [0]
new_driver = 'driver'

#web driver config DESK
options = webdriver.ChromeOptions()
options.headless = True

#web driver config MOBILE
mobile_emulation = {
    "deviceMetrics": {"pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}
options_mobile = webdriver.ChromeOptions()
options_mobile.add_argument("--start-maximized")
options_mobile.add_experimental_option("mobileEmulation", mobile_emulation)
options_mobile.headless = True


#using sys to get the path in the user PC to make the "backup folder location" txt file
location_backup_txt = '{}/backup-folder-location.txt'.format(sys.path[0])

# reading folder backup
with open(location_backup_txt, 'r') as f:
        folder_location_program = f.readline() 
f.close()

# ask for folder location and change it in the entry. Also changed in the backup.
def get_the_folder_location():
    folder_location_program = filedialog.askdirectory()
    label_where_to_save.delete(0, END)
    label_where_to_save.insert(INSERT, folder_location_program)    
    with open(location_backup_txt, 'w') as f:
        f.write(folder_location_program)  
    f.close()

#change the new_driver name for a new use
def change_new_driver(new_driver):
    return new_driver + str(1)


    
#screenshot function
def make_a_full_screenshot(counter): 

    increment_working_message(check_if_working)
    display_and_hide_working_message(check_if_working)

    global new_driver

    #check if is the first print, to create the folder
    if len(counter) == 1:
        #create new folder
        create_new_folder()

    new_driver = change_new_driver(new_driver)     
    print(new_driver)   
    increment_listbox_line_number()

def create_new_folder():
    local_to_save = label_where_to_save.get()
    name_folder = entry_folder_name.get()
    path_new_folder = '{}/{}'.format(local_to_save,name_folder)
    os.makedirs(path_new_folder)
    counter.append(1)
    

def increment_listbox_line_number():       
    listbox_line_to_write = int(len(counter)-2)
    make_print_and_close_driver(listbox_line_to_write)

def make_print_and_close_driver(listbox_line_to_write):
    print(listbox_line_to_write)    
    local_to_save = label_where_to_save.get()
    name_folder = entry_folder_name.get()
    url = entry_url_print.get()
    name_print = entry_name_print.get()

    #delete entry values (name and url)
    entry_url_print.delete(0, END)
    entry_name_print.delete(0, END)

    driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)             
    driver.get(url)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(650, S('Height'))
    path_print = ('{}/{}/{}.png'.format(local_to_save,name_folder,name_print))       

    #function that ensures all images are loaded
    number_of_images_in_the_website = driver.execute_script('return document.images.length')
    print(number_of_images_in_the_website)
 




    images_loading = True
    while images_loading == True:         
        need_wait = False     
        for i in range(number_of_images_in_the_website - 1):

            #verify if image are loaded
            image = return_image_load_state(driver, i)
            if image != True:
                print('need wait', i)
                need_wait = True

        if need_wait == False:
            driver.find_element_by_tag_name('body').screenshot(path_print)
            driver.quit()
            decrement_working_message(check_if_working)
            display_and_hide_working_message(check_if_working)
            print('finished ')

            number_of_prints.append(1)            
            label_infos.insert(listbox_line_to_write, str('Generated {}: {}'.format((len(number_of_prints)-1),name_print)))     

def return_image_load_state(driver, image_number):    
    try:
        image = driver.execute_script('return document.images[{}].complete'.format(int(image_number+1))) 
        print(image_number)               
        return(image)
    except:
        #some sites may bug this function, so i did that    '-'
        return(True)    
   



def start_new_thread():
    threading.Thread(target= make_a_full_screenshot, args=[counter]).start()

def increment_working_message(check_if_working):
    check_if_working.append(1)
    
def decrement_working_message(check_if_working):
    check_if_working.pop()


def display_and_hide_working_message(check_if_working):
    if len(check_if_working) > 1:
        label_info_workink.grid(row= 11, column=1, columnspan=2)
        
    else:
        label_info_workink.grid_forget()
        

# starting interface
root = Tk()
root.title('B. PRINTER')
root.geometry("530x480+500+300")
root.resizable(False,False)
#root.iconbitmap(r"D:\Desktop\Fresh Python\Projects_1\Bronha Printer v2\download.ico")

#               tkinter interface lines
#line 0
base_img_logo = os.path.dirname(__file__)
logo_img_path = os.path.join(base_img_logo, 'new-logo-img.png')
logo_img = PhotoImage (file = logo_img_path)
label_logo_img = Label(root, image= logo_img, compound='top' ).grid(row=0, column=1, rowspan=2)
#line 0 second image
base_img_logo2 = os.path.dirname(__file__)
logo_img_path2 = os.path.join(base_img_logo2, 'old-logo-img.png')
logo_img2 = PhotoImage (file = logo_img_path2)
label_logo_img2 = Label(root, image= logo_img2, compound='top' ).grid(row=0, column=3, rowspan=2, sticky='w')
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
entry_folder_name = Entry(root, width=17)
entry_folder_name.grid(row=6, column=1)
entry_folder_name.insert(INSERT, 'PRINTS-PROG-V')
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
entry_name_print = Entry(root, width=15)
entry_name_print.grid(row=9, column=1)
entry_url_print = Entry(root, width=30)
entry_url_print.grid(row=9, column=2)
#line 10
text_prints_prog = Button(root, text='RUN', width=10,  command=start_new_thread).grid(row=9, column=3, sticky='w')
label_space_row_10 = Label(root, text ='').grid(row=10, column=0)
#line 11
label_info_workink = Label(root, height=1, width=30, fg="white", bg ="red", text= 'Working. Please dont close the program')
label_space_row = Label(root, text ='').grid(row=11, column=0)
#label_info_workink.grid(row= 11, column=2)
#line 12
label_infos = Listbox(root, height=8, width=50, fg="blue4", bg ="gray80")
label_infos.grid(row= 12, column=1, columnspan=2, sticky='w')
button_zip_file = Button(root, text='Zip Files')
button_zip_file.grid(row=12, column=3)
#button_zip_file = Button(root, text='Zip Files', command=make_a_full_screenshot).grid(row=11, column=3)
#line 13
label_version_text = Label(root, text='version 2.2').grid(row= 13, column=0)

root.mainloop()
