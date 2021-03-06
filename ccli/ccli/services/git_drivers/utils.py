#------------------------------------------------------------------------------#
# Copyright (c) 2014 Los Alamos National Security, LLC
# All rights reserved.
#------------------------------------------------------------------------------#

import os
import shutil
import tempfile
import argparse
import json
import subprocess
#from sh import cd
#from sh import git
#from sh import tar
#from sh import xf
from collections import OrderedDict

#------------------------------------------------------------------------------#
# Context manager.
#------------------------------------------------------------------------------#

#class cd:
#    """Context manager for changing the current working directory"""
#
#    def __init__(self, newPath):
#        self.newPath = os.path.expanduser(newPath)
#    # __init__
#
#    def __enter__(self):
#        self.savedPath = os.getcwd()
#        os.chdir(self.newPath)
#    # __enter__
#
#    def __exit__(self, etype, value, traceback):
#        os.chdir(self.savedPath)
#    # __exit__
#
# class cd

#------------------------------------------------------------------------------#
# Clone a repository in mirroring mode.
#------------------------------------------------------------------------------#

def clone_mirror(src, directory, args):

    if(args.debug or args.verbose):
        print "Cloning source repository", \
            src, "into", directory
    # if

    subprocess.call(["git", "clone", "--mirror", src, directory])

# clone_mirror

#------------------------------------------------------------------------------#
# Push a repository in mirroring mode.
#------------------------------------------------------------------------------#

def push_mirror(dest, directory, args):

    if(args.debug or args.verbose):
        print "Pushing into", dest, "from", directory
    # if

    subprocess.call(["git", "push", "--mirror", dest], cwd=directory)

# push_mirror

#------------------------------------------------------------------------------#
# Create a tar archive suitable for transfer to red network
#------------------------------------------------------------------------------#

def create_archive(src, directory, archive_name, args):

    if(args.debug or args.verbose):
        print "Creating tar archive ", archive_name, "from", src
    # if

    # clone the mirror
    clone_mirror(src, directory, args)

    # create archive
    subprocess.call(["tar", "cvjf", archive_name, directory])

# create_archive

#------------------------------------------------------------------------------#
# Expand a tar archive
#------------------------------------------------------------------------------#

def expand_archive(directory, archive_name, dest, args):

    if(args.debug or args.verbose):
        print "Expanding tar archive ", archive_name, "to", directory
    # if

    subprocess.call(["tar", "xvjf", archive_name, "--strip-components=2"],
        cwd=directory)

    push_mirror(dest, directory, args)

# expand_archive

#------------------------------------------------------------------------------#
# Transfer a file to the red network
#------------------------------------------------------------------------------#

def transfer_file(directory, filename, args):

    if(args.debug or args.verbose):
        print "Transferring", filename, "to the red network"
    # if

# transfer_file

#------------------------------------------------------------------------------#
# Formatting options for emacs and vim.
# vim: set tabstop=4 shiftwidth=4 expandtab :
#------------------------------------------------------------------------------#
