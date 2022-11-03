#!/usr/bin/env python

import sys
import getpass
from lib import yamlconfig

# ########################
# config loading functions:
# ########################

def load(oConfig, sConfigFile):
    oConfig = yamlconfig.getFromFile(sConfigFile)

    if not (oConfig is None):
        if 'files' in oConfig:
            for configFileId in oConfig['files']:
                oSpecificConfig = None
                filePath = oConfig['files'][configFileId]['path']
                fileIsEncrypted = oConfig['files'][configFileId]['encrypted']
                if not fileIsEncrypted:
                    filePath = oConfig['files'][configFileId]['path']
                    oSpecificConfig = yamlconfig.getFromFile(filePath)
                else:
                    password = ''
                    try:
                        password = getpass.getpass(prompt='password needed for encrypted file:')
                    except Exception as error:
                        print('ERROR', error)
                    else:
                        print('Password entered:', password)
                    # filePath = oConfig['files'][configFileId]['path']
                    # oSpecificConfig = yamlconfig.getFromFile(filePath)
                oConfig[configFileId] = oSpecificConfig
        else:
            sys.exit('config: impossible to find "files" entry in config')

    return oConfig

