import subprocess, sys, os, argparse

osFamily = os.system('windows' if os.name == 'nt' else 'unix')

# try to open version file stored in system

