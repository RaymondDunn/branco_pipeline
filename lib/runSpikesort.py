import subprocess
import settings

# this function calls two command line programs built into phy
# the first takes care of automatic sorting, and the second
# prompts manual sorting. This will cause the experiment data file to
# be editted and sorted into the appropriate bins


def runSpikesort():

    # deprecated
    # subprocess.call(["klusta", settings.paramsPath])
    subprocess.call(["phy", "spikesort", settings.paramsPath])
    # subprocess.call("klustaviewa")
    subprocess.call(["phy", "cluster-manual", settings.experiment_data_file])
