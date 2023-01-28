"""
 Definition to calculate absolute path to project root on any machine.
Store this path in a variable to make it accessible throughout the project
"""
import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
print(ROOT_DIR)