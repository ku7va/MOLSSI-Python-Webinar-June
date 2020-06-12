import os
import glob 
import argparse
import numpy

parser = argparse.ArgumentParser(description="This script analyzes a user provided mdout file and outputs all the bonds.")
parser.add_argument("mdout_file", help="'mdout_file' is the file path for the xyz file to analyze")
args = parser.parse_args()

file_location = args.mdout_file
data_file = os.path.join('data', '03_Prod.mdout')

filehandle = open('homeworkdata3.txt', 'w+')
outfile = open(data_file, 'r')
data = outfile.readlines()
outfile.close()

for line in data:
    if "NSTEP" in line:
        nstep_line = line
        cat = nstep_line.split()
        nstep = float(cat[2])
    if "Etot" in line:
        energy_line = line
        words = energy_line.split()
        energy = float(words[2])
        filehandle.write(F'{nstep} \t {energy: .4f} \n')
filehandle.close()

                