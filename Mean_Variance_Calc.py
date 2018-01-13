import csv

# A dictionary to keep the x, y, z of every tag
data = {}

# A dictionary to keep the mean of each marker
mean_map = {}

# A dictionary to keep the variance of each marker
variance_map = {}

def read_data():
	# Read in the data file
        csvDataFile = open('AR_Marker_Pose.csv')
        csvReader = csv.reader(csvDataFile)
	
	# Put in the poses of every tag
	for row in csvReader:
		listOfPose = []
		if row[0] in data.keys():
			temp = data.get(row[0])
			temp.append([float(row[1]), float(row[2]), float(row[3])])
			data[row[0]] = temp
		else:
			data[row[0]] = [float(row[1]), float(row[2]), float(row[3])]			

def mean():
        # Calculate the mean of each marker's x, y, z
        # Sum of variable / total
        for key in data:
                x_mean = 0.0
                y_mean = 0.0
                z_mean = 0.0
                i = 0
		size = len(key)
                while i < size:
                        x_mean += float(key[i][0])
                        y_mean += float(key[i][1])
                        z_mean += float(key[i][2])
                        i += 1
                x_mean  /= size
                y_mean  /= size 
                z_mean  /= size
                pose = [x_mean, y_mean, z_mean]
                
                # Store in the dictionary
                mean_map[row[0]] = pose

def variance():
        # Calculate the variance of each marker's x, y, z
        # Sum of (variable - mean)^2 / total - 1
        for key in data:
        	x_variance = 0.0
        	y_variance = 0.0
        	z_variance = 0.0
        	i = 0
		size = len(key)
        	while i < size:
                	x_variance += (float(key[i][0]) - mean_map[key[0]][0]) ** 2
                	y_variance += (float(key[i][1]) - mean_map[key[0]][1]) ** 2
                	z_variance += (float(key[i][2]) - mean_map[key[0]][2]) ** 2
                	i += 3
        	x_variance  /= size - 1
        	y_variance  /= size - 1
        	z_variance  /= size - 1
        	pose = [x_variance, y_variance, z_variance]

        	# Store in the dictionary
        	variance_map[key[0]] = pose

if __name__ == '__main__':
	
	read_data()
	print(data)