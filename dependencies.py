import importlib, subprocess, argparse

parser = argparse.ArgumentParser(description='Python pip package dependency checker and satisfier')
parser.add_argument('os', type=str, help='Operating system family of this device (valid: macos, linux, windows)')
parser.add_argument('packages', type=str, help='Name of single package')

args = parser.parse_args()
package = args.packages 	# str
os = args.os				# str

specialModules = {	
	# package name : module name
	"pyyaml": "yaml"
}

global packageName, moduleName

packageName = ''
moduleName = ''



if os not in ['macos', 'linux', 'windows']:
	raise ValueError(f'OS name "{os}" is not valid. Valid OS families are macos, linux, and windows.')


def special():
	global packageName, moduleName
	if package in list(specialModules.keys()):
		packageName = package
		moduleName = specialModules[package]
	else:
		packageName = moduleName = package


def check():
	installed = None
	
	try:
		tempImport = importlib.import_module(moduleName)
		installed = True
		del tempImport
	except:
		installed = False

	return installed


def installRequired(opsys:str):
	command = ['python', '-m', 'pip', 'install', packageName]
	
	if opsys == 'macos':
		command[0] = 'python3'

	subprocess.call(command)

special()
if not check():
	installRequired(os)
