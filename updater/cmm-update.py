import subprocess, sys, os, argparse, platform

# find OS family
osFamily = platform.system()


# make function to test if a specific file path exists by opening it as binary read only
def exists(filePath):
	try:
		file = open(filePath, 'br')
		del file
		return True
	except:
		return False


# set paths based on OS family
execPath = ''
infoPath = ''
if osFamily == 'Darwin':
	execPath = '/usr/local/bin/cmm'
	infoPath = '/usr/local/var/cmm/info.yml'
elif osFamily == 'Linux':
	execPath = '/usr/local/bin/cmm'
	infoPath = '/usr/local/var/cmm/info.yml'
elif osFamily == 'Windows':
	#execPath = ''
	#infoPath = ''
	raise NotImplementedError(f'Windows support is still in development.')
else:
	raise NotImplementedError(f'"{osFamily}" is currently not supported.')


os.makedirs(os.path.dirname(infoPath), exist_ok=True)


execExists = exists(execPath)
infoExists = exists(infoPath)