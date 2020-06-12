"""
This module has functions associated with analyzing the geometry of a molecule.
"""


import numpy
import os
import argparse #Allows you to generalize the file to use the program on, handles arguments

def calculate_distance(coords1, coords2): #think of the simplest imputs
    """
    Calculate the distance between 2 atoms, using paramenters that define one list of atomic xyz
    coordinates [xcoor, ycoor, zcoor]. Each parameters makes it 1D array.
    """
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(atom_distance, min_input=0, max_input=1.5):
    #How to write documentation to help the user
    """
    Check if a distance is a bond on a minimum and maximum length.
    Inputs: distance, min_input, max_input
    Return: True or False
    """
    if atom_distance > min_input and atom_distance <= max_input:
        return True
    else:
        return False
    
if __name__ == "__main__": #Tells Python this is the main part of the code
    
    #Executing Argparse functions
    parser = argparse.ArgumentParser(description="This script analyzes a user provided xyz file and outputs all the bonds.")
    parser.add_argument("xyz_file", help="'xyz_file' is the file path for the xyz file to analyze")
    args = parser.parse_args()

    file_location = args.xyz_file
    xyz_file = numpy.genfromtxt(fname=file_location, dtype='unicode', skip_header = 2)
    symbols = xyz_file[:, 0]
    coordinates = xyz_file[:, 1:]
    coordinates = coordinates.astype(numpy.float)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                distance = calculate_distance(coordinates[num1], coordinates[num2])
                if bond_check(distance) is True: #Modification is in this line
                    print(F' {symbols[num1]} to {symbols[num2]} : {distance: .3f}')