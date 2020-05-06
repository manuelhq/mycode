#!/usr/bin/env python3
#import shell tools 
import shutil

import os

#selects directory
os.chdir("/home/student/mycode/")

#copy file A to file B
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy entire directory notice /end creates folder dir
shutil.copytree("5g_research/", "5g_research_backup/")


