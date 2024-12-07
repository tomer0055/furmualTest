import csv;
from array import array
import os;
from dot import dot;
from graph import graph;
from optimalRoute import optimalRoute;



def write_to_csv(filename, layoutLeft, layoutRight, optimalRoute):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y', 'relativePos'])
        for d in layoutLeft:
            writer.writerow([d.x, d.y, d.relativePos])
        for d in layoutRight:
            writer.writerow([d.x, d.y, d.relativePos])
        for d in optimalRoute:
            writer.writerow([d.x, d.y, d.relativePos])
    print(f"Data written to {filename}")

defaultAddress = "BrandsHatchLayout.csv"
print("Chose if you want to read from the default file(File that was given) or from a new file")
print ("The default file is BrandsHatchLayout.csv")
print("1. Default file")
print("2. New file")
choice = input("Enter your choice: ")
if choice == "2":
    address = input("Enter the address of the file: ")
    defaultAddress = address
if choice != "1" and choice != "2":
    print("Invalid choice")
    exit()
if(os.path.exists(defaultAddress) == False):
    print("Invalid address")
    exit()



with open(defaultAddress, 'r') as layout:
    reader = csv.reader(layout)
    header = next(reader)
    layoutLeft = []
    layoutRight = []
    
    for row in reader:
        if row[0] == "" or row[1] == "" or row[2] == "":
            continue  # Skip rows with empty values
        try:
            d = dot(row[0], row[1], row[2])
            if d.relativePos == "left":
                layoutLeft.append(d)
            else:
                layoutRight.append(d)
        except ValueError:
            print(f"Skipping row with invalid data: {row}")  
            
    # connect the last point with the first point
    layoutLeft.append(dot(layoutLeft[0].x, layoutLeft[0].y, layoutLeft[0].relativePos))
    layoutRight.append(dot(layoutRight[0].x, layoutRight[0].y, layoutRight[0].relativePos))
    
    
    optimal = optimalRoute(layoutLeft, layoutRight)
    g = graph(layoutLeft, layoutRight,optimal.smooth_route())
    g.draw()
    write_to_csv("output.csv", layoutLeft, layoutRight, optimal.smooth_route())
        
        
        
        
        
        

        
    
       
