import numpy as np
from neo import io
import settings


def convertNexFile():

    # Set debug
    DEBUG = True

    filedir = settings.datadir + '/'
    basename = 'SE-CSC-RAW-Ch'
    # analogInput = settings.analogInput
    saveFilename = settings.saveFilename
    chnList = settings.chnList
    availableChannels = settings.availableChannels
    start = settings.sampleRate * settings.start

    # check available channels and channel list for discrepancies
    # will catch extra channels
    if len(set(chnList).symmetric_difference(set(availableChannels))) > 0:
        print '--Warning! the chnList and availableChannels do not match'
        if DEBUG:
            print '--chnList ', chnList
            print '--availableChannels ', availableChannels
        # have the option of cascading back and correcting chn list
        # and probe geometry and params but low priority now

    if DEBUG:
        print '--filedir ', filedir

    rawData = []
    for chn in chnList:
        fname = basename + str(chn) + '_.nex'
        print 'converting', fname, '.....'
        try:
            r = io.NeuroExplorerIO(filename=(filedir + fname))
            seg = r.read_segment(lazy=False, cascade=True)
            rawData.append(np.array(seg.analogsignals[0])*5.0)
        except IOError:
            print 'File', fname, 'not found'

    flatRawData = np.array(rawData)

    # setting end of conversion. take number of elements along given index
    if settings.end < 1:
        end = flatRawData[0].size - 1
    else:
        end = settings.sampleRate * settings.end
    flatRawData = flatRawData[:, start:end]

    flatRawData = flatRawData.transpose()

    saveFilename = saveFilename + '.dat'
    flatRawData.astype('int16').tofile(filedir+saveFilename)
