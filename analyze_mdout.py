import os
import argparse

#Tell argparse to handle arguments
parser = argparse.ArgumentParser(description="This script analyzes a user provided mdout file and extracts total energy.")

#Tell argparse what arguments to expect
parser.add_argument("path", help="'path' is the file path for the file to be analyzed")

#Get arguments from the user
args = parser.parse_args()

#Get the pathname specified in the argument
filename = args.path

outfile = open(filename, 'r')
data = outfile.readlines()
outfile.close()
base_filename = filename.split('.')[0]
output_filename = F'{base_filename}_Etot.txt'
filehandle = open(output_filename, 'w+')

print(F'Writing output to {output_filename}')

etot = []
nstep = []
for line in data:
    split_line = line.split()
    ##if "NSTEP" in line:
        ##nstep.append(split_line[2])
    if "Etot" in line:
        etot.append(split_line[2])
        
etot = etot[:-2]
##nstep = nstep[:-2]

for energy in etot:
    filehandle.write(F"{energy}\n")
        
filehandle.close()

                