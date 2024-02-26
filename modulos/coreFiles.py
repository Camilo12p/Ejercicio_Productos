import os
import json

BASE = 'data/'
def checkFile(*params):
    if(os.path.isfile(BASE+params[0])):
        params[1].update(readFile(params[0]))
    else:
        createFile(params[0],params[1])

def readFile(*params):
    with open(BASE+params[0], 'r') as br:
        return json.load(br)

def createFile(*params):
    with open(BASE+params[0], 'w') as bw:
        json.dump(params[1],bw,indent=4)

def updateFile(*params):
    with open(BASE+params[0],'w+') as bw:
        bw.seek(0)
        json.dump(params[1],bw,indent=4)
