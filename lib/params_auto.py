import settings

# not sure if i'm allowed to use a .py parameter file but it's
# worth a try..
#######################################################################
# SpikeDetekt parameters
#######################################################################
# Name of the experiment (which will be the name of the output KWIK
# files)
experiment_name = settings.experiment_name

# Raw data files. These can be in .dat/.bin/any raw data format,
# or .kwd HDF5 KWIK format. You can pass a list of several files which
# will be processed sequentially.
raw_data_files = settings.raw_data_files

# Probe file describing geometry, channels, and adjacency graph in JSON
prb_file = settings.prb_file

# Bit depth of raw data
nbits = 16

# Multiplier from actual voltage to stored data
voltage_gain = 10.

# Raw data sampling rate, in Hz
sample_rate = settings.sample_rate

# Number of channels in the recording
nchannels = settings.nchannels


# ---------------------------------------------------------------------
# Raw data filtering and saving
# ---------------------------------------------------------------------
# Whether to save the .raw.kwd file if a non-HDF5 raw data format is used.
# This is needed to visualise the data in TraceView etc, and speeds up
# future runs of SpikeDetekt. If a .raw.kwd file is used as the input,
# it will never be overwritten.
#save_raw = True
# Whether to save the .high.kwd file with HPF data used for spike
# detection. This is processed using a Butterworth band-pass filter.
#save_high = False
# Bandpass filter low corner frequency
#filter_low = 500.
# Bandpass filter high corner frequency
#filter_high = 0.95 * .5 * sample_rate
# Order of Butterworth filter.
#filter_butter_order = 3
# Whether to save a .low.kwd file; this is processed using a Hamming
# window FIR filter, then subsampled 16x to save space when storing.
#save_low = False
# ---------------------------------------------------------------------
# Chunks
# ---------------------------------------------------------------------
# SpikeDetekt processes the raw data in chunks with small overlaps to
# catch spikes which would otherwise span two chunks. These options
# will change the default chunk size and overlap.
#chunk_size = int(1. * sample_rate) # 1 second
#chunk_overlap = int(.015 * sample_rate) # 15 ms
# ---------------------------------------------------------------------
# Threshold setting for spike detection
# ---------------------------------------------------------------------
# Change this to 'positive' to detect positive spikes.
detect_spikes = settings.detect_spikes
# SpikeDetekt takes a set of uniformly distributed chunks throughout
# the high-pass filtered data to estimate its standard deviation. These
# parameters select how many excerpts are used and how long each of them
# are.
#nexcerpts = 50
#excerpt_size = int(1. * sample_rate) # 1 second
# This is then used to calculate a base threshold which is multiplied
# by the two parameters below for the two-threshold detection process.
threshold_strong_std_factor = settings.threshold_strong_std_factor
threshold_weak_std_factor = settings.threshold_weak_std_factor
# ---------------------------------------------------------------------
# Spike extraction
# ---------------------------------------------------------------------
# The number of samples to extract before and after the centre of the
# spike for waveforms. Then, waveforms_nsamples is calculated using the
# formula: waveforms_nsamples = extract_s_before + extract_s_after
#extract_s_before = 16
#extract_s_after = 16
# ---------------------------------------------------------------------
# Features
# ---------------------------------------------------------------------
# Number of features (PCs) per channel.
#nfeatures_per_channel = 3
# The number of spikes used to determine the PCs
#pca_nwaveforms_max = 10000
# ---------------------------------------------------------------------
# Advanced
# ---------------------------------------------------------------------
# Number of samples to use in floodfill algorithm for spike detection
#connected_component_join_size = 1 # 1 sample
#connected_component_join_size = int(.00005 * sample_rate) # 0.05ms
# Waveform alignment
#weight_power = 2
# Whether to make the features array contiguous
#features_contiguous = True
#######################################################################
# KlustaKwik parameters (must be prefixed by KK_). Uncomment to override
# the defaults, which can be shown by running 'klustakwik' with no options
#######################################################################
# This causes KlustaKwik to perform clustering on a subset of spikes and
# estimate the assignment of the other spikes. This causes a speedup in
# computational time (by a rough factor of KK_Subset), though will not
# significantly decrease RAM usage. For long runs where you are unsure of
# the data quality, you can first use KK_Subset = 50 to check the
# clustering quality before performing a Subset 1 (all spikes) run.
#KK_Subset = 1
# The largest permitted number of clusters, so cluster splitting can produce
# no more than n clusters. Note: This must be set higher than MaskStarts.
#KK_MaxPossibleClusters = 1000
# Maximum number of iterations. ie. it won't try more than n iterations
# from any starting point.
#KK_MaxIter = 10000
# You can start with a chosen fixed number of clusters derived from the
# mask vectors, set by KK_MaskStarts.
#KK_MaskStarts = 500
# The number of iterations after which KlustaKwik first attempts to split
# existing clusters. KlustaKwik then splits every SplitEvery iterations.
#KK_SplitFirst = 20
# The number of iterations after which KlustaKwik attempts to split existing
# clusters. When using masked initializations, to save time due to excessive
# splitting, set SplitEvery to a large number, close to the number of distinct
# masks or the number of chosen starting masks.
#KK_SplitEvery = 40
# KlustaKwik uses penalties to reduce the number of clusters fit. The
# parameters PenaltyK and PenaltyKLogN are given positive values. The
# higher the values, the fewer clusters you obtain. Higher penalties
# discourage cluster splitting. PenaltyKLogN also increases penalty
# when there are more points. -PenaltyK 0 -PenaltyKLogN 1 is the
# default, corresponding to the "Bayesian Information Criterion".
# -PenaltyK 1 -PenaltyKLogN 0 corresponds to "Akaike's Information
# Criterion". This produces a larger number of clusters, and is
# recommended if you are find that clusters corresponding to different
# neurons are incorrectly merged.
#KK_PenaltyK = 0.
#KK_PenaltyKLogN = 1.
# Specifies a seed for the random number generator.
#KK_RandomSeed = 1
# The number of unmasked spikes on a certain channel needed to unmask that
# channel in the cluster. This prevents a single noisy spike, or coincident
# noise on adjacent channels from slowing down computation time.
#KK_PointsForClusterMask = 10
# Setting this saves a .temp.clu file every iteration. This slows the runtime
# down reasonably significantly for small runs with many iterations, but allows
# to recover where KlustaKwik left off; useful in case of large runs where you
# are not confident that the run will be uninterrupted.
#KK_SaveTempCluEveryIter = 0
# This is an integer N when, used in combination with the empty string
# for UseFeatures above, omits the last N features. This should always
# be used with KK_UseFeatures = ""
#KK_DropLastNFeatures = 0
# ---------------------------------------------------------------------
# Classic 'all channels unmasked always' mode
# ---------------------------------------------------------------------
# To use KlustaKwik in "unmasked" mode, set this to 0.
# This disables the use of the new `masked Expectation-Maximization'
# algorithm, and sets all the channels to be unmasked on all spikes.
#KK_UseDistributional = 1
# In classic mode, KlustaKwik starts from random cluster assignments,
# running a new random start for every integer between MinClusters and
# MaxClusters. For these values to take effect, MaskStarts must be set to 0.
#KK_MinClusters = 100
#KK_MaxClusters = 110
# By default, this is an empty string, which means 'use all features'.
# Or, you can you can specify a string with 1's for features you want to
# use, and 0's for features you don't want to use. In classic mode,
# you use this option to take out bad channels. In masked mode,
# you should instead take bad channels out from the .PRB file.
#KK_UseFeatures = ""
# ---------------------------------------------------------------------
# Advanced
# ---------------------------------------------------------------------
# The algorithm will be started n times for each initial cluster count
# between MinClusters and MaxClusters.
#KK_nStarts = 1
# Saves means and covariance matrices. Stops computation at each iteration.
# Manual input required for continuation.
#KK_SaveCovarianceMeans = 0
# Saves a .clu file with masks sorted lexicographically.
#KK_SaveSorted = 0
# Initialises using distinct derived binary masks. Use together with
# AssignToFirstClosestMask below.
#KK_UseMaskedInitialConditions = 0
# If starting with a number of clusters fewer than the number of distinct
# derived binary masks, it will assign the rest of the points to the cluster
# with the nearest mask.
#KK_AssignToFirstClosestMask = 0
# All log-likelihoods are recalculated every KK_FullStepEvery steps
# (see DistThresh).
#KK_FullStepEvery = 20
#KK_MinMaskOverlap = 0.
#KK_AlwaysSplitBimodal = 0
# ---------------------------------------------------------------------
# Debugging
# ---------------------------------------------------------------------
# Turns miscellaneous debugging information on.
#KK_Debug = 0
# Increasing this to 2 increases the amount of information logged to
# the console and the log.
#KK_Verbose = 1
# Outputs more debugging information.
#KK_DistDump = 0
# Time-saving parameter. If a point has log likelihood more than
# DistThresh worse for a given class than for the best class, the log
# likelihood for that class is not recalculated. This saves an awful lot
# of time.
#KK_DistThresh = 6.907755
# All log-likelihoods are recalculated if the fraction of instances
# changing class exceeds ChangedThresh (see DistThresh).
#KK_ChangedThresh = 0.05
# Produces .klg log file (default is yes, to switch off do -Log 0).
#KK_Log = 1
# Produces parameters and progress information on the console. Set to
# 0 to suppress output in batches.
#KK_Screen = 1
# Helps normalize covariance matrices.
#KK_PriorPoint = 1
# Outputs number of initial clusters.
#KK_SplitInfo = 1

#Diagnostic options
#-------------------
#diagnostics_path = '/home/tiago/Code/diagnostics.py'     # path to the diagnostics module
# diagnostics_time_samples = [0, 500, 1000]   # put here the time samples of the spikes you want to debug
# show_plots_as_they_arise = True #modify scale of plots using matplotlib
# save_graph_data = True   # save data in plots as a pickle file

