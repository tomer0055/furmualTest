import csv;
from array import array;
from dot import dot;
from graph import graph;
from opotimalRoute import optimalRoute;



with open('BrandsHatchLayout.csv', 'r') as layout:
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
    g.draw();    

        
        
    
       
