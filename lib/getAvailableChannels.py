import glob
import os
import re

# this function looks through the datadir and returns a list
# of all of the channels within the list.
# this function also returns the file name of the analog input, or
# an empty string


def getAvailableChannels(datadir=''):

    # set debug
    DEBUG = False

    if DEBUG:
        print '-- datadir is ', datadir

    if len(datadir) == 0:
        print '--Error in getAvailableChannels. Something went wrong'

    availableChannels = []
    analogInput = ''
    datadir = datadir + '/'

    # set analog input
    analogInput = glob.glob(datadir + "Analog Input*.nex")

    # if multiple files with same file format, only set first one
    if len(analogInput) > 0:
        print '--Setting analog input to,', analogInput[0]
        analogInput = os.path.basename(analogInput[0])

    if DEBUG:
        print '--analog input is ', analogInput

    # get list of strings
    answer = []
    endPaths = glob.glob(datadir + "SE-CSC-RAW-Ch*.nex")

    answer += endPaths
    # turn list of strings to ints
    for s in answer:
        availableChannels.append(int(re.search(r'\d+', os.path.basename(s)).group()))
        if DEBUG:
            print '--s is', s

    if DEBUG:
        print '--availableChannels ', availableChannels

    # check for returning something valid
    # if (len(availableChannels) == 0) or (len(analogInput) == 0):
    if len(availableChannels) == 0:
        print '--error in getAvailableChannels():'
        exit()

    return availableChannels, analogInput
