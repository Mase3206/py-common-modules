import importlib, subprocess, argparse, sys

global packageName, moduleName, specialModules

specialModules = {	
	# package name : module name
	"pyyaml": "yaml"
}


def special(packageName):
	if package in list(specialModules.keys()):
		moduleName = specialModules[packageName]
	else:
		moduleName = package

	return moduleName


def check(module):
	installed = None
	
	try:
		tempImport = importlib.import_module(module)
		installed = True
		del tempImport
	except:
		installed = False

	return installed


def installRequired(os:str, package:str):
	command = ['python', '-m', 'pip', 'install', package]
	
	if os == 'macos':
		command[0] = 'python3'

	subprocess.call(command)


# This code will only run if the program is called directly, because it all depends on command line arguments.

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Python pip package dependency checker and satisfier')
	parser.add_argument('os', type=str, help='Operating system family of this device (valid: macos, linux, windows)')
	parser.add_argument('packages', type=str, help='Name of single package')

	args = parser.parse_args()
	package = args.packages 	# str
	os = args.os				# str

	if os not in ['macos', 'linux', 'windows']:
		raise ValueError(f'OS name "{os}" is not valid. Valid OS families are macos, linux, and windows.')
	
	module = special(package)
	if check(module):
		print(f'Module "{module}" from package "{package}" is already installed.')
	else:
		sys.stdout.flush()
		sys.stdout.write(f'Module "{module}" from package "{package}" is not installed. Installing via pip...')
		installRequired(os, package)
		sys.stdout.write(f'\rModule "{module}" from package "{package}" is not installed. Installing via pip... done.')
