# to find and replace plugin name in wordpress plugin boilerplate

# two command line args must be given
# A.) path to plugin folder
# B.) name of plugin with spaces, example 'super awesome plugin'

import os
import sys

pluginFolderPath = sys.argv[1]
pluginName = sys.argv[2]

if not pluginFolderPath:
    print('Must provide a path argument')
    sys.exit(0)

if not pluginName:
    print('Must provide plugin name')
    sys.exit(0)


# arg should be a string with spaces 'my plugin name'
def getThingsToReplace(plugin_name):
    things_to_replace = {
        "plugin-name": 'proxy-network-pro',
        "plugin_name": "proxy_network_pro",
        "Plugin_Name": "Proxy_Network_Pro",
        "PLUGIN_NAME_": "PROXY_NETWORK_PRO_",
    }

    things_to_replace['plugin-name'] = plugin_name.lower().replace(' ', '-')
    things_to_replace['plugin_name'] = plugin_name.lower().replace(' ', '_')
    things_to_replace['Plugin_Name'] = plugin_name.lower().title().replace(' ', '_')
    things_to_replace['PLUGIN_NAME'] = plugin_name.upper().replace(' ', '_')

    return things_to_replace



things_to_replace = getThingsToReplace(pluginName)

for dname, dirs, files in os.walk(pluginFolderPath):

    for originalFileName in files:

        fpath = os.path.join(dname, originalFileName)
        newName = originalFileName
        newFpath = fpath

        # if a search term is in a file name, replace it
        for searchTerm, replacement in things_to_replace.items():
            if searchTerm in originalFileName:
                newName = originalFileName.replace(searchTerm, replacement)
                newFpath = os.path.join(dname, newName)
                os.rename(fpath, newFpath)
                break


        contents = ''
        with open(newFpath) as f:
            contents = f.read()
            for searchTerm, replacement in things_to_replace.items():
                if searchTerm in contents:
                    contents = contents.replace(searchTerm, replacement)
            
        with open(newFpath, "w") as f:
            f.write(contents)


