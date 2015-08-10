import Tkinter
import tkFileDialog


# this function uses tkinter to provide a file dialogue
# to get the .prb file for clustering

def getParameterFile():

    root = Tkinter.Tk()
    paramsPath = tkFileDialog.askopenfilename(parent=root,
                                              initialdir="/",
                                              title='Please select a parameter file',
                                              defaultextension='.prb')

    if len(paramsPath) == 0:
        print 'Error: no file selected'
        exit()

    return paramsPath
