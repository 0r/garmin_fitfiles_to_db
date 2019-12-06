# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:12:19 2019
@author: SALMAN
salmah2@unlv.nevada.edu
place this script in a folder with fit files 
this script will convert .fit -> .csv
=============================================
this script can only convert the fit files inside the activity folder
linux instructions:
pip3 install fitparser
python3 convert_fit_to_csv.py

@edited by flyindutche 
hyu3@wpi.edu
"""

from fitparse import FitFile
import re
import csv
import glob
for filename in glob.glob('*.FIT'):
    fitfile = FitFile(filename)
    z = []
    headers = []
    for record in fitfile.get_messages('record'):
        x = []
        y = []
        for record_data in record:
            if(record_data.name == "timestamp"):
                datetime =  re.findall('\d+', str(record_data.value) )
                y.append('year')
                y.append('month')
                y.append('day')
                y.append('hour')
                y.append('min')
                y.append('sec')
                for split in datetime:
                    x.append(split)
            else:
                x.append(record_data.value)
                y.append(record_data.name)
        z.append(x)
        headers = y
    print(z)
    with open(filename+'.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(z)
