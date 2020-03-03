#!/usr/bin/python3

import shutil
import os

#set working directory
os.chdir('/home/student/mycode/')

#move raynor.obj to ceph_storage dir
shutil.move('raynor.obj', 'ceph_storage')

#specify new name for kerrigan.obj
xname = input('What is the new name for kerrigan.obj?')

#change name of kerrigan.obj to input specified for xname in previous function
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


