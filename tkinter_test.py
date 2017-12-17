# import the necessary packages
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import cv2
import imutils

def select_image():
    # grab a reference to the image panels
    global panelA, panelB
 
    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename()

    if len(path) > 0:
        bigrotated = cv2.imread(path)
        big = imutils.rotate(bigrotated, angle = 180)
        image = imutils.resize(big, width = 400)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        
    if panelA is None or panelB is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)
        panelB = Label(image=edged)
        panelB.image = edged
        panelB.pack(side="right", padx=10, pady=10)
 
	# otherwise, update the image panels
    else:
	# update the pannels
        panelA.configure(image=image)
        panelB.configure(image=edged)
        panelA.image = image
        panelB.image = edged
	
# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
 
# kick off the GUI
root.mainloop()
    
