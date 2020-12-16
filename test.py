# Import libraries
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, required=True)
args = parser.parse_args()
# Creating dataset 
np.random.seed(2000) 
data = np.random.normal(50, 20, 220) 
fig = plt.figure(figsize =(10, 9)) 
# Creating plot 
plt.boxplot(data) 
# show plot 
plt.savefig(args.filename)