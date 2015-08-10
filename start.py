from lib import convertNexFile
from lib import runSpikesort
from lib import generateRawTraces
from lib import generateFilteredTraces
from lib import convertKwik
import settings as s

# this should be run in ipython...

# modules:

# get a directory

# convert from nex to dat
#   how much to cut off
#   channel list *
#   file naming
# convertNexFile.convertNexFile()

# probe geometry
#     channel list
#     dead channels
#     graph


# detekt and klusta .dat
#     parameters
#     file names
#     dead channels *
# runSpikesort.runSpikesort()

# extract to hdf5
#     interact with user for waveforms
#     get metadata
#     also have raw traces
# convertKwik.convertKwik()

# other
#     generate raw/filtered traces before sorting

# main wrapper
def main():
    beginPipeline()


def beginPipeline():
    if s.GENERATE_RAW_TRACE_HDF5:
        generateRawTraces.generateRawTraces()
    if s.GENERATE_FILTERED_TRACE_HDF5:
        generateFilteredTraces.generateFilteredTraces()
    if s.CONVERT_NEX_FILES:
        convertNexFile.convertNexFile()
    if s.RUN_AUTO_CLUSTERING:
        runSpikesort.runSpikesort()
    if s.CONVERT_KWIK_TO_HDF5:
        convertKwik.convertKwik()


if __name__ == '__main__':
    main()
