import os

script_path = os.path.dirname(os.path.abspath(__file__))  # Current file path
file_path = os.path.join(script_path, 'sample_file')  # Creating the file path

'''
file = open('/sample.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()
'''

with open(file_path, 'w') as file:
    file.write('chai aur python')
