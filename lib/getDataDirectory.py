import Tkinter
import tkFileDialog


# this function uses tkinter to provide a file dialogue
# to get the data directory processing
def getDataDirectory():

    root = Tkinter.Tk()
    datadir = tkFileDialog.askdirectory(parent=root,
                                        initialdir="/",
                                        title='Please select a data directory')

    if len(datadir) == 0:
        print 'Error: no file selected'
        exit()

    return datadir
