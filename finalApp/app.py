import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import library

# theme variables
borderColor = "blue"
fillColor = "light blue"

# misc variables
selectedOptions = []
MAX_SIZE = (300, 300)
origImage = None
changedImg = None

#################################################################################################button commands

def SelectFile():
    path = filedialog.askopenfilename()
    if path:
        global origImage 
        origImage = Image.open(path)

        tempImg = origImage.copy()
        tempImg.thumbnail(MAX_SIZE)

        img1 = ImageTk.PhotoImage(tempImg)
        inImg.config(image= img1)
        inImg.image = img1
        inFileLabel.config(text=path)

def SaveFile():
    if changedImg:
        path = filedialog.asksaveasfilename(defaultextension=".png", title="save as")
        if path:
            changedImg.save(path)

def RunJobs():
    global changedImg 
    changedImg = origImage.copy()
    for op in selectedOptions:
        match op:
            case ("Bayer Filter",_):
                changedImg = library.bayer.BayerFilter(changedImg)

            case ("Demosaic", _):
                changedImg = library.bayer.Demosaic(changedImg)

            case ("Red-green color blindness", _):
                changedImg = library.blindsim.rg_sim(changedImg)

            case ("Yellow-blue color blindness", _):
                changedImg = library.blindsim.yb_sim(changedImg)

            case ("Gaussian blur", _):
                changedImg = library.blur.GausBlur(changedImg)

            case ("Greyscale",_):
                changedImg = library.greyScale.GreyScale(changedImg)
            
            case ("Invert",_):
                changedImg = library.inversion.Invert(changedImg)

            case ("Sepia",_):
                changedImg = library.sepia.Sepia(changedImg)

            case ("Sepia (ms)",_):
                changedImg = library.sepia.MSSepia(changedImg)

            case ("Vinegette",_):
                changedImg = library.vin.Vinegette(changedImg)

            case _:
                pass
    tempImg = changedImg.copy()
    tempImg.thumbnail(MAX_SIZE)
    img2 = ImageTk.PhotoImage(tempImg)
    outImg.config(image=img2)
    outImg.image = img2

def SelectJob(event):
    job = opsSelect.get()
    i = len(selectedOptions)
    newOp = tk.Label(selectedFrame, text=job, background=fillColor, cursor="hand2")
    newOp.grid(sticky="nsew")
    newOp.bind("<Button-1>", RemoveJob)
    selectedFrame.rowconfigure(i, weight=1)
    selectedOptions.append((job, newOp))
    ReGrid(selectedFrame)

def RemoveJob(event):
    toRemove = event.widget
    for op in selectedOptions:
        if op[1] == toRemove:
            selectedOptions.remove(op)
            break
    toRemove.destroy()
    ReGrid(selectedFrame)

def ReGrid(parent):
    i = 0
    for widget in parent.winfo_children():
        widget.grid(sticky="nsew", row=i)
        i+=1


#################################################################################################End button comands

#################################################################################################Create window
window = tk.Tk()

# ---------------------------------------------------------------Input Pane
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++make pane
inPane = tk.PanedWindow(window, background= borderColor)

# +++++++++++++++++++++++++++++++++++++++++++++++++++make widgets
inPaneFrame = tk.Frame(inPane, background= borderColor)

# section label
inImageLabel = tk.Label(inPaneFrame, text="Original Image", background= fillColor)
inImageLabel.grid(sticky="nsew")


# input image
tempImg = Image.open("./placeHolder.png")
tempImg.thumbnail(MAX_SIZE)
img1 = ImageTk.PhotoImage(tempImg)
inImg = tk.Label(inPaneFrame, image= img1, background= fillColor)
inImg.grid(sticky="nsew")


# filename
inFileLabel = tk.Label(inPaneFrame, text="No file selected", background= fillColor)
inFileLabel.grid(sticky="nsew")

# select file button
selectFileButton = tk.Button(inPaneFrame, text="Select File", background= fillColor, command= SelectFile)
selectFileButton.grid(sticky="nsew")

inPaneFrame.rowconfigure(0, weight=2)
inPaneFrame.rowconfigure(1, weight=4)
inPaneFrame.rowconfigure(2, weight=1)
inPaneFrame.rowconfigure(3, weight=2)
inPaneFrame.columnconfigure(0, weight=1)

# ++++++++++++++++++++++++++++++++++++++++++++++++++finalize pane
inPane.grid(column=0, sticky="nsew")
inPane.rowconfigure(0, weight=1)
inPane.columnconfigure(0, weight=1)

inPane.add(inPaneFrame)

# ---------------------------------------------------------------End Input Pane

# ---------------------------------------------------------------Options Pane
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++make pane
opsPane = tk.PanedWindow(window, background= borderColor)

# +++++++++++++++++++++++++++++++++++++++++++++++++++make widgets
opsFrame = tk.Frame(opsPane, background= fillColor)

# section label
opsLabel = tk.Label(opsFrame, text= "Options", background= fillColor)
opsLabel.grid(sticky="nsew")

# option options
style = ttk.Style()
style.configure("box.TCombobox", background= fillColor)
opsSelect = ttk.Combobox(opsFrame, style="box.TCombobox")
opsSelect.state(["readonly"])
opsSelect['values'] = ("Bayer Filter", "Demosaic",
                       "Red-green color blindness", "Yellow-blue color blindness",
                       "Gaussian blur", 
                       "Greyscale",
                       "Invert",
                       "Sepia",
                       "Sepia (ms)",
                       "Vinegette")
opsSelect.grid(sticky="ew")
opsSelect.bind("<<ComboboxSelected>>", SelectJob)


# selected options list
selectedFrame = tk.Frame(opsFrame, background= fillColor)
selectedFrame.columnconfigure(0, weight=1)
selectedFrame.grid(sticky="nsew")

# run options list
sendButton = tk.Button(opsFrame, text= "Send", background= fillColor, command=RunJobs)
sendButton.grid(sticky="nsew")

# ++++++++++++++++++++++++++++++++++++++++++++++++++finalize pane
opsFrame.rowconfigure(0, weight=2)
opsFrame.rowconfigure(1, weight=2)
opsFrame.rowconfigure(2, weight=4)
opsFrame.rowconfigure(3, weight=2)
opsFrame.columnconfigure(0, weight=1)

opsPane.grid(column=1, row=0, sticky="nsew")
opsPane.rowconfigure(0, weight=1)
opsPane.add(opsFrame)

# ---------------------------------------------------------------End Options Pane

# ---------------------------------------------------------------Output Pane
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++make pane
outPane = tk.PanedWindow(window, background= borderColor)

# +++++++++++++++++++++++++++++++++++++++++++++++++++make widgets
outFrame = tk.Frame(outPane, background= fillColor)

# section label
outLabel = tk.Label(outFrame, text= "Altered Image", background= fillColor)
outLabel.grid(sticky="nsew")

# output image

tempImg = Image.open("./placeHolder.png")
tempImg.thumbnail(MAX_SIZE)
img2 = ImageTk.PhotoImage(tempImg)
outImg = tk.Label(outFrame, image= img2, background= fillColor)
outImg.grid(sticky="nsew")

outSpacer = tk.Label(outFrame, text="Generated Image", background= fillColor)
outSpacer.grid(sticky="nsew")

# save file button
saveButton = tk.Button(outFrame, text= "Save Image", background= fillColor, command=SaveFile)
saveButton.grid(sticky="nsew")

# ++++++++++++++++++++++++++++++++++++++++++++++++++finalize pane
outFrame.rowconfigure(0, weight=2)
outFrame.rowconfigure(1, weight=4)
outFrame.rowconfigure(2, weight=1)
outFrame.rowconfigure(3, weight=2)
outFrame.columnconfigure(0, weight=1)

outPane.grid(column=2, row=0, sticky="nsew")
outPane.rowconfigure(0, weight=1)

outPane.add(outFrame)

# ---------------------------------------------------------------End Output Pane

window.columnconfigure(0, weight=3)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=3)

#################################################################################################End Create window

window.mainloop()

