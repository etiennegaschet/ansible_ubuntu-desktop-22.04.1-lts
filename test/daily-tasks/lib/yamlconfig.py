#!/usr/bin/env python

import sys
import yaml

# ########################
# yaml config functions:
# ########################

def getFromString(sYmlConfig):
    try:
        ymlConfig = yaml.safe_load(sYmlConfig)
    except:
        sys.exit('  -> error when trying to parse yaml config.')

    return ymlConfig


def getFromFile(ymlFile):
    print('- loading config from file ' + ymlFile + '...')

    ymlFileContent = None

    try:
        oFile = open(ymlFile)
        ymlFileContent = oFile.read()
        oFile.close()
    except:
        sys.exit('  -> error: cannot access config file ' + ymlFile)

    return getFromString(ymlFileContent)

