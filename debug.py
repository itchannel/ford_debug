#!/usr/bin/env python

"""
Simple script to run the API
"""

import sys, os, logging, time
from fordpass_new import Vehicle

if __name__ == "__main__":

    if len(sys.argv) < 4:
        raise Exception('Must specify Username, Password and VIN as arguments, e.g. demo.py test@test.com password123 WX231231232')
    else:
        r = Vehicle(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) # Username, Password, VIN
        #r.requestUpdate() # Poll the car for an update
        print(r.status()) # Print the status of the car
