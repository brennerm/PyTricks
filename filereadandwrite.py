#! /usr/bin/env python3
"""
Simple implementation for read/writing tasks using local files.
"""

# Example: Reading numerical values from 
# data file for calculations and writing
# the result to a new file.
with open("YOUR_INPUT_FILE.TXT", 'r') as input_file:
  input_array = input_file.read()
  input_array = [float(n) for n in input_array.split()]
  output_array = []
  
  # Code for calculations using input_array values 
  # here. Results are stored in output_array.
  
with open("YOUR_OUTPUT_FILE.TXT", 'w') as output_file:
  # Example code for outputting "x, y" values to text file.
  # Need to convert numerical data to string in order to 
  # write to file.
  output_string = ""
  for index in range(0, len(output_array)-1):
    output_string += " ".join([str(output_array[index]), str(output_array[index+1]), "\n"])
  output_file.write(output_string)
  
