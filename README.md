# branco_pipeline
Note that for clustering with Klustakwik, current build doesn't automatically launch klusta but instead it must be done manually (I may later include a bash script that does it all for you, but seeing as klustasuite will soon be deprecated I won't fully add it to the functionality of the program). 
Instead of Klustakwik, the program assumes some functionality in the API that isn't yet released (as of August 18th 2015).

# Dependencies:
Phy
Neo

# Installation Instructions:
Using an anaconda build of python, create a new virtual environment. Download and install dependencies (Phy and Neo, which in turn may have their own dependencies...)

# Execution Instructions:
Run python start.py just like you would in NeuroDAQ to begin the process. The program contains several modules relevant to the pipeline process, which can be turned on or off by changing the value of the relevant boolean variable in settings.py to True or False. These modules execute serially

# settings.py
This file contains all of the relevant parameters for the pipeline. Modify them from within this file. There are many more parameters that can be modified, but the most common ones are listed.