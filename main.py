import os
import numpy as np

def is_float(element):
	try:
		float(element)
		return True
	except ValueError:
		return False

def readFile(id): # reads in each file and returns a list with the data
	fileName = "cellData/" + id + ".txt"
	with open(fileName) as f:
		lines = f.readlines()
	return lines

files = []
for file in os.listdir("cellData"): # reading names of all files
	if file != '.DS_Store':
		files.append(file[:-4])

def combineFiles(currID, data): # recursive function to combine cells in lineage
	for lines in readFile(currID): # read in current file
			data += [lines.split()]
	children = []
	exit = True
	for file in files: # find children
		if file.split("_")[1] == currID.split("_")[2]:
			children.append(file)
			exit = False
	for child in children: # recurse on children
		files.remove(child)
		return combineFiles(child, list(data))
	if exit == True: # at leaf node
		return data

files = ['0_62_62', '1_62_74', '2_74_84', '3_84_92', '4_92_129', '5_129_137', '6_137_157', '7_157_167', '8_167_280', '9_280_288', '10_288_310']
root = files[0]
files.remove(root)
datas = combineFiles(root, []) # data of selected cell lineage

# Display Header:
header = datas[0]
print("Variables to choose from: ")
print(header)
print()

# Variable Selection:
xVar = input("X-Variable: ")
xRow = header.index(xVar)
yVar = input("Y-Variable: ")
yRow = header.index(yVar)
zVar = input("Z-Variable: ")
zRow = header.index(zVar)

# Data Selection:
x = [row[xRow] for row in datas]
x = [num for num in x if is_float(num)]
y = [row[yRow] for row in datas]
y = [num for num in y if is_float(num)]
z = [row[zRow] for row in datas]
z = [num for num in z if is_float(num)]

# Convert Data from str to int:
xs = []
ys = []
zs = []

for val in x:
	xs.append(float(val))
for val in y:
	ys.append(float(val))
for val in z:
	zs.append(float(val))

x = np.array(xs)
y = np.array(ys)
z = np.array(zs)

# Plotting Variables:
from matplotlib import pyplot as plt

plt.xlabel(xVar)
plt.ylabel(yVar)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.scatter(x, y, c=z, cmap='viridis')
cbar = plt.colorbar()
for t in cbar.ax.get_yticklabels():
  t.set_fontsize(12)

plt.savefig("mygraphs.png")
