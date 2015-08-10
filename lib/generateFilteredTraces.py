import h5py
import numpy as np
from neo import io
import settings


def generateFilteredTraces():

    # Set debug
    DEBUG = True

    filedir = settings.datadir + '/'
    basename = 'SE-CSC-SPIKE-Ch'
    analogInput = settings.analogInput
    saveFilename = settings.saveFilename
    saveFilename = saveFilename + '_SPIKE.hdf5'
    chnList = settings.chnList
    availableChannels = settings.availableChannels

    # check available channels and channel list for discrepancies
    # will catch extra channels
    if len(set(chnList).symmetric_difference(set(availableChannels))) > 0:
        print '--Warning! the chnList and availableChannels do not match'
        if DEBUG:
            print '--chnList ', chnList
            print '--availableChannels ', availableChannels
        # have the option of cascading back and correcting chn list
        # and probe geometry and params but low priority now

    # Get raw data from all channels
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

    # Get analog input with frame starts
    try:
        fname = analogInput
        if DEBUG:
            print '--analogInput ', fname
        r = io.NeuroExplorerIO(filename=(filedir + fname))
        seg = r.read_segment(lazy=False, cascade=True)
        rawData.append(np.array(seg.analogsignals[0])*5.0)
    except IOError:
        print 'File', fname, 'not found'

    flatRawData = np.array(rawData)
    flatRawData = flatRawData.transpose()
    data = flatRawData

    # Save to .hdf5 file
    dt = 1/30000.
    f = h5py.File(filedir+saveFilename, 'w')
    root = f['/']
    chn = root.create_group('channels')
    for trace in range(data.shape[1]):
        dset = chn.create_dataset('channel_'+str(trace), data=data[:, trace])
        dset.attrs['dt'] = dt
    f.close()
