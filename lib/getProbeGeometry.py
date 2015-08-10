import Tkinter
import tkFileDialog


# this function uses tkinter to provide a file dialogue
# to get the .prb file for clustering

def getProbeGeometry():

    root = Tkinter.Tk()
    probePath = tkFileDialog.askopenfilename(parent=root,
                                        initialdir="/",
                                        title='Please select a probe geometry file',
                                        defaultextension='.prb')

    if len(probePath) == 0:
        print 'Error: no file selected'
        exit()

    return probePath
