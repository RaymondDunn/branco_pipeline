import numpy as np
import h5py
from phy.io import KwikModel
import settings

# TODO:
# Program description
# Make resulting hdf5 better
# Use groups = "good" as criteria for appending to goodChannels (not '2')


# # global macro for debug
# DEBUG = True
# if DEBUG:
#     print '--Debug mode on'


class Clusta():

    def __init__(self, clustaID=None, spikeID=None, spikeTime=None,
                 waveformChannel=None, spikeSamplesToAdd=None,
                 waveformsToAdd=None):
        if clustaID is None:
            self.id_of_clusta = -1
        else:
            self.id_of_clusta = clustaID

        if spikeID is None:
            self.id_of_spike = []
        else:
            self.id_of_spike.append(spikeID)

        if spikeTime is None:
            self.time_of_spike = []
        else:
            self.time_of_spike.append(spikeTime)

        if waveformChannel is None:
            self.channel_for_waveforms = -1
        else:
            self.channel_for_waveforms = waveformChannel

        if spikeSamplesToAdd is None:
            self.spike_samples = []
        else:
            self.spike_samples.append(spikeSamplesToAdd)

        if waveformsToAdd is None:
            self.waveforms = []
        else:
            self.waveforms.append(waveformsToAdd)

    def reset(self):
        self.id_of_clusta = -1
        self.id_of_spike = []
        self.time_of_spike = []
        self.sample_times = []
        self.waveform = []
        self.channel_for_waveforms = -1

    def setClusterChannel(self):
        try:
            print 'Please input the channel you would like to analyze for cluster:', self.id_of_clusta
            channel = int(raw_input('Channel:'))
        except ValueError:
            print "Not a number"
        self.channel_for_waveforms = channel


def fillClustaArrayPhy(model):

    # Set debug
    DEBUG = True

    clustaArray = []

    goodClustersList = []
    i = 0
    while i < model.cluster_ids.size:
        # if a given cluster is in model.ids
        if model.cluster_groups[model.cluster_ids[i]] == 2: # TODO should change this to "good"
            if DEBUG:
                print '--adding', model.cluster_ids[i], 'to clustaArray'
            clustaID = model.cluster_ids[i]
            goodClustersList.append(clustaID)
            clusta = Clusta(clustaID)
            clusta.setClusterChannel()
            clustaArray.append(clusta)

            if DEBUG:
                print '--current clustaArray:'
                for z in clustaArray:
                    print '--', z.id_of_clusta
        i = i + 1

    i = 0
    # iterate through all spikes
    while i < model.spike_ids.size:
        # if spike belongs to good cluster
        if model.spike_clusters[i] in goodClustersList:
            # iterate clusta array to find correct clusta to update with
            # spike properties
            j = 0
            while j < len(clustaArray):
                # if the array cluster id = the model cluster id
                if clustaArray[j].id_of_clusta == model.spike_clusters[i]:
                    clustaArray[j].id_of_spike.append(i)
                    clustaArray[j].time_of_spike.append(model.spike_times[i, ])
                    clustaArray[j].spike_samples.append(model.spike_samples[i, ])
                    if DEBUG:
                        print '--appending', model.waveforms[i].swapaxes(1, 2)[0, clustaArray[j].channel_for_waveforms].size, 'spike samples to clusta:', clustaArray[j].id_of_clusta, 'for spike:', i
                    clustaArray[j].waveforms.append(model.waveforms[i].swapaxes(1, 2)[0, clustaArray[j].channel_for_waveforms])
                j = j + 1

        i = i + 1

    return clustaArray

def generateHDF5Phy(model):
    # This function calls fillFlustaArrayPhy to produce
    # an array of clusta objects, which it then uses
    # to fill an HDF5 dataset for analysis in neurodaq (e.g. plotting, avg waveforms etc)

    clustaArray = fillClustaArrayPhy(model)

    # create hdf5 file
    saveFile = model.kwik_path[:-5] + '.hdf5'
    f = h5py.File(saveFile, 'w')

    # store metadata
    m = f.create_group('/recording/metadata')
    for a in model.metadata:
        if DEBUG:
            print '--Appending metadata...'
        # m.create_dataset(name=a, data=model.metadata[a])
        # instead create group...and create a dataset named the dataset value
        n = m.create_group(a)
        n.create_dataset(name=str(model.metadata[a]), shape=(2,)) # might be broken here?

    # store data in clustaArray structure
    for a in clustaArray:
        c = f.create_group('/recording/'+str(a.id_of_clusta))

        # append other data
        c.create_dataset(name='spike_number', data=np.array(a.id_of_spike))
        c.create_dataset(name='spikes_times',data=np.array(a.time_of_spike))
        c.create_dataset(name='samples', data=np.array(a.spike_samples))

        # create group for waveform data
        w = c.create_group('waveforms')
        if DEBUG:
            print '--Appending channel_analyzed'
        w.create_dataset(name='channel_analyzed', data=np.array(a.channel_for_waveforms))

        # store waves points of each spike
        spike_waves = np.array(a.waveforms)
        i = 1
        for spike in spike_waves:
            w.create_dataset(name=str(i), data=spike)
            i = i + 1

    f.close()


# def fillClustaArrayHDF5(filePath=''):
def convertKwik(kwikPath=''):

    # make better file access...
    # if (len(kwikPath) == 0):
    #     kwikPath = raw_input('Please enter the path of the .kwik file: ')

    kwikPath = settings.datadir + '/' + settings.experiment_data_file
    model = KwikModel(kwikPath)
    generateHDF5Phy(model)
