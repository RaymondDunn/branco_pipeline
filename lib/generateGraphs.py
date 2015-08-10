import numpy as np
import matplotlib as plt
from scipy import stats

DEBUG = True


def plotRaster(clustaArray=[]):

    if (len(clustaArray) < 1):
        print 'Nothing to plot!'
    else:
        # create list of times that maps to each spike
        p_sptimes = []
        for a in clustaArray:
            for b in a.spike_samples:
                p_sptimes.append(b)
        sptimes = np.array(p_sptimes)

        p_clusters = []
        for c in clustaArray:
            for d in c.id_of_spike:
                p_clusters.append(c.id_of_clusta)
        clusters = np.array(p_clusters)

        # dynamically generate cluster list
        clusterList = []
        for a in clustaArray:
            clusterList.append(a.id_of_clusta)
        # plot raster for all clusters

        # nclusters = 20

        # #for n in range(nclusters):
        timesList = []
        for n in clusterList:
            # if n<>9:
            ctimes = sptimes[clusters == n]
            timesList.append(ctimes)
            plt.plot(ctimes, np.ones(len(ctimes))*n, '|')
        plt.show()


def plotHistogram(clustaArray=[]):
    if (len(clustaArray) < 1):
        print 'Nothing to plot!'
    else:
        # create list of times that maps to each spike
        p_sptimes = []
        for a in clustaArray:
            for b in a.spike_samples:
                p_sptimes.append(b)
        sptimes = np.array(p_sptimes)

        p_clusters = []
        for c in clustaArray:
            for d in c.id_of_spike:
                p_clusters.append(c.id_of_clusta)
        clusters = np.array(p_clusters)

        # dynamically generate cluster list
        clusterList = []
        for a in clustaArray:
            clusterList.append(a.id_of_clusta)

        # plot raster for all clusters
        # nclusters = 20

        # #for n in range(nclusters):
        timesList = []
        for n in clusterList:
            # if n<>9:
            ctimes = sptimes[clusters == n]
            timesList.append(ctimes)
            # plt.plot(ctimes, np.ones(len(ctimes))*n, '|')
        # plt.show()

        # plot frequency in Hz over time
        dt = 1/30000.  # in seconds
        binSize = 1  # in seconds
        binSizeSamples = round(binSize/dt)
        recLen = np.max(sptimes)
        nbins = round(recLen/binSizeSamples)

        binCount = []
        cluster = 3
        for b in np.arange(0, nbins-1):
            n = np.sum((timesList[cluster] > b*binSizeSamples) &
                       (timesList[cluster] < (b+1)*binSizeSamples))
            binCount.append(n/binSize)  # makes Hz

        plt.plot(binCount)
        plt.ylim([0, 20])
        plt.show()


def plotWaveforms(clustaArray=[]):
    if (len(clustaArray) < 1):
            print 'Nothing to plot!'
    else:
        clustaToPlot = int(raw_input('Please enter the cluster id to plot: '))

        i = 0
        while i < len(clustaArray):
            if clustaToPlot == clustaArray[i].id_of_clusta:
                j = 0
                while j < len(clustaArray[i].waveforms):
                    k = 0
                    while k < len(clustaArray[i].waveforms[j]):
                        plt.plot([k], [clustaArray[i].waveforms[j][k]], 'ro')
                        k = k + 1
                    j = j + 1
            i = i + 1
        plt.show()


def plotAverageWaveforms(clustaArray=[]):
    if (len(clustaArray) < 1):
        print 'Nothing to plot!'
    else:
        avgList = [[]]  # for lists inside loop
        errList = [[]]

        i = 0
        while i < len(clustaArray):
            # for every clusta we'll need a new list of averages
            avgList.append([])
            errList.append([])
            # reverse matrix orientation
            np_waveforms = np.array(clustaArray[i].waveforms).swapaxes(0, 1)
            j = 0
            if DEBUG and j < (np_waveforms.size/np_waveforms[0].size):
                print '--np_waveforms[j].size is', np_waveforms[j].size
            # size divided by number of spikes gives you number of samples
            # zero here is dummy
            while j < (np_waveforms.size/np_waveforms[0].size):
                # average along the sample axis
                avg = np_waveforms[j].mean()
                sem = stats.sem(np_waveforms[j])
                if DEBUG:
                    print '--avg computed for sample', j, 'is', avg
                    print '--values were:', np_waveforms[j]
                    print '--calculated error values is', sem
                # plot sample vs mean
                avgList[i].append(avg)
                errList[i].append(sem)
                j = j + 1
            i = i + 1
        # alg adds one too many lists...so we need to delete the last object
        avgList.pop()
        errList.pop()

        if DEBUG: 
            print '--samples to be plotted: ',
            a = 0
            while a < len(avgList):
                print avgList[a],
                a = a + 1


        # initialize list for x values
        i = 0
        numSamples = []
        while i < len(clustaArray[0].waveforms[0]):
            numSamples.append(i)
            i = i + 1

        # plot, add some customization for prettiness
        i = 0
        while i < len(avgList):
            if DEBUG:
                print 'avgList size is:', len(avgList)

            if DEBUG:
                print 'Plotting item i which is', np.arange(20).size, 'by', len(avgList[i])

            plt.plot(numSamples, avgList[i], linestyle='-', markersize=5)
            plt.errorbar(numSamples, avgList[i], yerr=errList[i])
            i = i + 1

        # plt.legend()
        plt.show()

        # plt.legend([goodClustersList], loc='lower left')


def generateProbeGeometryGraph():

    print
