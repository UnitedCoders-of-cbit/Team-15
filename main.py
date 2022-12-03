

from tkinter import *
from tkinter import filedialog
import fpdf
import cv2
import numpy as np
import pytesseract as pytesseract

from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image, ImageTk
from pytesseract import pytesseract


def browseFiles():
    py = r"*.png *.jpg *jpeg"
    global result
    #fileselect = filedialog.askopenfilename(initialdir="/pictures", title="Select a File", filetypes=(("images", py),("all files", "*.*")))
    #fileselect=filedialog.askopenfile(initialdir = "\\",title = "Select file",filetypes = (("jpeg files",".jpg"),("all files",".*")))
    #print(filename)
    #fileselect="smp.jpg"
    #if fileselect == "":
        #return
    fileselect="smp.jpg"
    key="python"
    img = cv2.imread(fileselect)
    print(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite("removed_noise.png", img)
    cv2.imwrite(fileselect, img)
    result = pytesseract.image_to_string(Image.open(fileselect))
    global str1
    l = list(result.split("\n"))
    f=open("text.txt","a")
    for i in range(len(l)):
        f.write(l[i])
    f.write("\n")

    f.close()
    f=open("text.txt","r")
    for line in f:
        str1=""
        if key in line:
            str1=line
        else:
            str1="no records found"
    label_file_explorer.configure(text=str1)



def pdf():
    global result
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write(5, result)
    pdf.ln()
    pdf.output("Result.pdf")
window = Tk()
window.title('File Explorer')
bg = PhotoImage(file="bg.png")
canvas1 = Canvas(window, width=400,
                 height=400)

canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")
window.geometry("700x350")
reg_info = Label(window, text="Naive way to extract", width='35', height='5',
                 font=("Droid Sans Mono italic", 12, "bold"), fg="light grey", bg='black')
reg_info.place(x=680, y=150, anchor='center')
window.config(background="white")
lg=PhotoImage(file="logo.png")
label1=Label(window,image=lg,width=200,height=75)
label1.place(x=1,y=1)
label_file_explorer = Label(window,
                            text="See the input Here", font=("Droid Sans Mono", 10, "bold"),
                            width=60, height=12,
                            fg="black",bg="lightgrey")

label_file_explorer.place(x=450, y=250)

button_explore = Button(window,
                        text="Submit", fg="white", bg="black", font=("Droid Sans Mono italic", 10, "bold"), width=10,command=browseFiles
                        )
button_explore.place(x=470, y=500)


button1 = Button(window,
                 text="convert text to pdf", fg="white", bg="black", font=("Droid Sans Mono italic", 10, "bold"), width=15,
                 command=pdf)
button1.place(x=780, y=500)


window.mainloop()



# In[ ]:



