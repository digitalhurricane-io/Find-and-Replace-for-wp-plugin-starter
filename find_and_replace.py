# to find and replace plugin name in wordpress plugin boilerplate

import os
import sys

if not sys.argv[1]:
    print('Must provide a path argument')
    sys.exit(0)

things_to_replace = {
    "plugin-name": 'proxy-network-pro',
    "plugin_name": "proxy_network_pro",
    "Plugin_Name": "Proxy_Network_Pro",
    "PLUGIN_NAME_": "PROXY_NETWORK_PRO_",
}

for dname, dirs, files in os.walk(sys.argv[1]):

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
