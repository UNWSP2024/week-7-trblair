# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
import math
def coordinatemath():
    coord1=int(input("Input the x coordinate of the first set: "))
    coord2=int(input("Input the y coordinate of the first set: "))
    coord3=int(input("Input the z coordinate of the first set: "))
    firstpoint=(coord1,coord2,coord3)
    coord1=int(input("Input the x coordinate of the second set: "))
    coord2=int(input("Input the y coordinate of the second set: "))
    coord3=int(input("Input the z coordinate of the second set: "))
    secondpoint=(coord1,coord2,coord3)
    distance= math.sqrt((secondpoint[0]-firstpoint[0])^2 + (secondpoint[1]-firstpoint[1])^2 + (secondpoint[2]-firstpoint[2])^2)
    print(distance)
coordinatemath()
