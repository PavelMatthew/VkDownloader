import vk_api
import requests 
from tkinter import*
import ctypes
import os, glob

root = Tk()
e_id = Entry(root)
e_num_photos = Entry(root)


def delete_all_from_downlaod():

    dir = 'downloaded'
    for file in os.scandir(dir):
        os.remove(file.path)
        
    pass



def readfile():

    with open('token.txt') as f:
        token = f.read()

    
    return token

   
def click():
    
    delete_all_from_downlaod()
    
    links = []
    my_token = readfile()
    session = vk_api.VkApi(token = my_token)
    vk = session.get_api()

    
    photos = vk.messages.getHistoryAttachments(peer_id = int(e_id.get()),media_type = "photo",count=int(e_num_photos.get()), preserve_order=1)


    
    sep1 = "'type': 'r'"
    sep2 = "'url': '"
    sep3 ="'}"
    numImage = 1
    parts1 = str(photos)


    for i in range(int(e_num_photos.get())):
    

    
        ourstr1 = parts1.partition(sep1)

        parts2 = ourstr1[2]
        ourstr2 =parts2.partition(sep2)


        parts3 = ourstr2[2]
        ourstr3 =parts3.partition(sep3)
        
        links.append(ourstr3[0])

        parts1= ourstr3[1]+ourstr3[2]
        
        print(links[i]+'\n')
        img_data = requests.get(links[i], verify = False).content
        with open('downloaded/'+str(numImage)+'.jpeg', 'wb+') as handler:
            handler.write(img_data)
            numImage=numImage+1
            
        root.quit()
    pass

def appwindow():
    
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    

    root.title("VkDownloader")
    root.geometry("250x70")
    root.eval('tk::PlaceWindow . center')
    
    e_id.pack()
    e_num_photos.pack()
    
    



#my_token = 'vk1.a._QZK8NMLQlfB3lToRHBL_h-rlnMhBdeRbT--ulE-u7Pf3iVYZ77Fs-ND5vvYVyoRqDa_B0ySAU9jEZyhdjRCorl7B8QaEtVa9T_lHlFYHVWdkVbihm9qYBsBXadw9BRHAjEsynqCsenkvjlO0QQ5xNvmiVp8u49WMV70n0-LiwaaXYDRVaGOTWPX7xSHQvR4eM7-pdAtywaIQM27Sutozw' 

    button = Button(root, text = "Загрузить",command=click)
    button.pack()
    root.mainloop()
    pass




if __name__ == '__main__':

        appwindow()
    

