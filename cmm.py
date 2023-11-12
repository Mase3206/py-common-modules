import subprocess, sys, os, argparse, yaml


# Initialize argparse
parser = argparse.ArgumentParser(description='Updater and installer for common packages used in many of my programs')
parser.add_argument('-i', type=str, help='Install package', metavar='package')
parser.add_argument('-u', action='store_true', help='Update all packages')
parser.add_argument('-r', type=str, help='Remove package', metavar='package')

args = parser.parse_args()
packageToInstall = args.i 	# str
doUpdate = bool(args.u)		# bool
packageToRemove = args.r 	# str


"""
# Required positional argument
parser.add_argument('pos_arg', type=int,
                    help='A required integer positional argument')

# Optional positional argument
parser.add_argument('opt_pos_arg', type=int, nargs='?',
                    help='An optional integer positional argument')

# Optional argument
parser.add_argument('--opt_arg', type=int,
                    help='An optional integer argument')

# Switch
parser.add_argument('--switch', action='store_true',
                    help='A boolean switch')
"""


# get os type
nt = (True if os.name == 'nt' else 'unix')


def fetchVersions():
	sys.stdout.flush()
	sys.stdout.write('Fetching versions file from GitHub...')
	# fetch versions file
	subprocess.call(
		['wget', 'https://raw.githubusercontent.com/Mase3206/py-common-modules/main/versions.yml'], 
		stdout=subprocess.DEVNULL,
		stderr=subprocess.DEVNULL
	)
	sys.stdout.write('\rFetching versions file from GitHub... done.\n')
	sys.stdout.flush()

	# open versions file, store to dict, then close
	with open('versions.yml', 'r') as f2:
		versions = yaml.safe_load(f2)
	# remove versions file
	os.remove('versions.yml')

	try:
		with open('installed.yml', 'r') as f1:
			installedVersions = yaml.safe_load(f1)
	except:
		f1 = open('installed.yml', 'w+')
		f1.close()

	if installedVersions == None:
		installedVersions = {}

	return versions, installedVersions


def saveInstalledVersions(newInstalledVersions):
	with open('installed.yml', 'w') as f3:
		yaml.safe_dump(newInstalledVersions, f3)


def update(module='all', quiet=False):
	toUpdate = []

	versions, installedVersions = fetchVersions()
	
	if module == 'all':
		# make a list of all out-of-date modules
		for mod in versions:
			if mod in list(installedVersions.keys()):
				if installedVersions[mod] < versions[mod]:
					toUpdate.append(mod)

	else:
		# if a specific module is passed, add only that one to toUpdate
		mod = module
		if installedVersions[mod] < versions[mod]:
			toUpdate.append(mod)
		
	if toUpdate == []:
		print('All modules are already up to date.') if not quiet else None
	else:
		print('Modules to update:') if quiet else None

		for mod in toUpdate:
			print(f'{mod}: {installedVersions[mod]} => {versions[mod]}')
		
		proceed = input('Proceed with update? [Y/n] ') if not quiet else 'y'
		if proceed == '' or proceed.lower() == 'y':
			# delete old modules
			for mod in toUpdate:
				print(f'Removing {mod}...') if not quiet else None
				os.remove(mod + '.py')
			# fetch updated modules
			for mod in toUpdate:
				print(f'Downloading and installing {mod}...') if not quiet else None
				subprocess.call(
					['wget', 'https://raw.githubusercontent.com/Mase3206/py-common-modules/main/' + mod + '.py'],
					stdout=subprocess.DEVNULL, 
					stderr=subprocess.DEVNULL
				)
				installedVersions[mod] = versions[mod]
			saveInstalledVersions(installedVersions)
			print('Update successful.') if not quiet else None
		else:
			print('Abort.') if not quiet else None


def install(module:str, quiet=False):
	versions, installedVersions = fetchVersions()
	installed = None

	# test if module is already installed. if so, set installed to True
	try:
		installedVersions[module]
		installed = True
	except:
		installed = False


	if installed == True:
		proceed = input('Module already installed. Would you like to try to update it? [Y/n] ') if not quiet else 'y'
		if proceed == '' or proceed.lower() == 'y':
			update(module)
		else:
			print(f'{module} not sent to updates. Exiting.') if not quiet else None
		del proceed
	else:
		try:
			proceed = input(f'Found {module} in GitHub repo. Would you like to install it? [Y/n] ') if not quiet else 'y'
			if proceed == '' or proceed.lower() == 'y':
				if not quiet:
					sys.stdout.flush()
					sys.stdout.write(f'Downloading {module}...')
				subprocess.call(
					['wget', 'https://raw.githubusercontent.com/Mase3206/py-common-modules/main/' + module + '.py'], 
					stdout=subprocess.DEVNULL, 
					stderr=subprocess.DEVNULL
				)
				del proceed
			else:
				exit('Abort.') if not quiet else None
				del proceed
		except:
			print(f'Fetching {module} failed. Verify that it exists.') if not quiet else None		#TODO: maybe list the installable modules?

		if not quiet:
			sys.stdout.write(f'\rDownloading {module}... done.\n')
			sys.stdout.write(f'Adding {module} to installed.yml...')
		installedVersions[module] = versions[module]
		saveInstalledVersions(installedVersions)
		if not quiet:
			sys.stdout.write(f'\rAdding {module} to installed.yml... done.\n')
			sys.stdout.flush()
			print(f'Successfully installed {module}.')

			


def remove(module:str):
	versions, installedVersions = fetchVersions()
	installed = None

	# test if module is already installed. if so, set installed to True
	try:
		installedVersions[module]
		installed = True
	except:
		installed = False

	if installed == False:
		print(f'{module} is not installed. Exiting.')
	elif installed == True:
		sys.stdout.flush()
		sys.stdout.write(f'Removing {module}...')
		try:
			os.remove(module + '.py')
			sys.stdout.write(f'\rRemoving {module}... done.\n')
		except:
			print(f'{module} not installed, but was found in installed.yml. Removing...')
		finally:
			sys.stdout.write(f'Removing {module} from installed.yml...')
			del installedVersions[module]
			saveInstalledVersions(installedVersions)
			sys.stdout.write(f'\rRemoving {module} from installed.yml... done.\n')
	else:
		raise RuntimeError('installed flag in remove() was not set to True or False.')
		

def installMultiple(modules:list, quiet=True):
	versions, installedVersions = fetchVersions()
	toInstall = []

	for module in modules:
		try:
			installedVersions[module]
			update(module)
		except:
			toInstall.append(module)

	# This function is meant to be called indirectly, so it defaults to quiet operation.
	# In fact, it can't even be loud, at the moment.	
	
	for module in toInstall:
		subprocess.call(
			['wget', 'https://raw.githubusercontent.com/Mase3206/py-common-modules/main/' + module + '.py'], 
			stdout=subprocess.DEVNULL, 
			stderr=subprocess.DEVNULL
		)
		installedVersions[module] = versions[module]
		saveInstalledVersions(installedVersions)





if doUpdate == True:
	update()

if packageToInstall != None:
	install(packageToInstall)

if packageToRemove != None:
	remove(packageToRemove)


while True:
	try:
		os.remove('wget-log*')
	except:
		break