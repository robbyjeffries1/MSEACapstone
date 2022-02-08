"""
ECON 5763, Economic Analytics
Capstone Project
EDA

Written by: Robby Jeffries
Date written: 02-08-2022
"""

# Import libraries
import os
import json

# Set working directory
os.chdir('/Users/robbyjeffries/MSEACapstone')
print("Current working directory: {0}".format(os.getcwd()))


# Opening JSON file
with open('Data/AMAZON_FASHION_5.json', 'r') as f:
  data = f.read()
  
# Parse file
obj = json.loads(data)

# Show values
print("usd: " + str(obj['overall']))

