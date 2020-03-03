#!/usr/bin/python3

#import additional code to complete our task
import shutil
import os

#move into the working directory
os.chdir("/home/student/mycode/")

#copy file a to file b
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy directory A to directory B, will create directory B if it does not exist
shutil.copytree("5g_research/", "5g_research_backup")

