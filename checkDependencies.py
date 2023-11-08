import importlib

def modules(modules:list):
	uninstalledModules = []
	

	for module in modules:
		tempImport = ''
		try:
			tempImport = importlib.import_module(module)
		except:
			uninstalledModules.append(module)

	return uninstalledModules


if __name__ == '__main__':
	modules(['numpy', 'pandas', 'pyyaml'])