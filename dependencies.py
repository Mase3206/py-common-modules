import importlib, subprocess, argparse

parser = argparse.ArgumentParser(description='Python pip package dependency checker and satisfier')
parser.add_argument('os', type=str, help='Operating system family of this device (valid: macos, linux, windows)')
parser.add_argument('packages', type=list, help='List of packages in valid Python form')

args = parser.parse_args()
packages = args.packages 	# list
os = args.os				# str


if os not in ['macos', 'linux', 'windows']:
	raise ValueError(f'OS name "{os}" is not valid. Valid OS families are macos, linux, and windows.')


def check(modules:list):
	uninstalledModules = []
	
	for module in modules:
		tempImport = ''
		try:
			tempImport = importlib.import_module(module)
		except:
			uninstalledModules.append(module)

	return uninstalledModules


def installRequired(notInstalledModules:list, opsys:str):
	command = ['python', '-m', 'pip', 'install'] + notInstalledModules
	
	if opsys == 'macos':
		command[0] = 'python3'

	subprocess.Popen(command)


installRequired(check(packages), os)


if __name__ == '__main__':
	check(['numpy', 'pandas', 'pyyaml'])