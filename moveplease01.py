#!/usr/bin/env python3

#grab the tools
import shutil

import os

#define working dir
os.chdir('/home/student/mycode/')

#use the move tool under shutil

shutil.move('raynor.obj', 'ceph_storage/')

#user input for renaming 
xname = input('What is the new name for kerrigan.obj? ')

#what happens after rename
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


