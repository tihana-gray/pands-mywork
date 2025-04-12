# Writing a function that will read in a dict object from file
# Author: Tihana Gray

import json
FILENAME ="testdict.json"

def readDict():
    # this will throw an error if the file does

    not exit
    # it should readly just return an empty dict
    # we can do this later
    with open(FILENAME) as f:
        return json.load(f)

# test the function
somedict = readDict()
print(somedict)