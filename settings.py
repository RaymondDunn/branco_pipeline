from lib import getAvailableChannels
from lib import getDataDirectory
from lib import getProbeGeometry
from lib import getParameterFile
import os

# TODO:
# Params_auto.prm or params_auto.py? Can either of these work?
# Readme.txt
# See convertKwik.py...
# Generate probe geometry graph?
# Automatically generate channel list based on probe file selected
# Automatically edit probe geometry and .nex file conversion
#   using items in deadChnList. Subtract those file conversion and
#   their indexed location in probe geometry
# Clustering with Phy vs clustering with Klustakwik --> run module
#   from bash script that then switches environments to run klusta


#######################################################################
# program-level settings
#######################################################################

# Set the functions that you want the program to run
GENERATE_RAW_TRACE_HDF5 = True
GENERATE_FILTERED_TRACE_HDF5 = False
CONVERT_NEX_FILES = True
RUN_AUTO_CLUSTERING = True
CONVERT_KWIK_TO_HDF5 = False  # relatively untested

# Set to false if you want to hardcode all directory names
PROMPT_USER_FOR_FILES = True

# directory of data files (must end with '/')
datadir = ''
if PROMPT_USER_FOR_FILES:
    datadir = getDataDirectory.getDataDirectory()


#######################################################################
# # conversion of raw data for clustering -- see convertNexFile.py
#######################################################################
saveFilename = 'rawdata'
chnList = [14, 15, 1, 2, 12, 13, 3, 4, 10, 11, 5, 6, 8, 9, 7]
# chnList = [12, 2, 14, 4, 6, 3, 8, 1, 10, 7, 5, 11, 9, 15, 13]  # second generate of probes

availableChannels, analogInput = getAvailableChannels.getAvailableChannels(datadir=datadir)
sampleRate = 30000
start = 1   # starts at 1 second in (to get rid of junk)
end = 0    # second number to stop recording. value < 1 defaults to convert all


#######################################################################
# probe geometry
#######################################################################
probePath = ''
if PROMPT_USER_FOR_FILES:
    probePath = getProbeGeometry.getProbeGeometry()

deadChnList = []


#######################################################################
# SpikeDetekt and KlustaKwik Parameters
# params here are for general purposes. For thoroughly editing params,
# specify params file
#######################################################################
paramsPath = os.getcwd() + '/lib/' + 'params_auto.py'
# if PROMPT_USER_FOR_FILES:
#     paramsPath = getParameterFile.getParameterFile()
# paramsPath = ''

# Parameters passed into automatic parameter file
# for a more comprehensive list of parameters, specify a parameter file
# in paramsPath
experiment_name = 'test_data'
experiment_file_extension = '.kwik' 
experiment_data_file = experiment_name + experiment_file_extension
raw_data_files = saveFilename+'.dat'
prb_file = probePath
sample_rate = sampleRate
nchannels = len(chnList)
threshold_strong_std_factor = 4.5
threshold_weak_std_factor = 2
detect_spikes = 'negative'
