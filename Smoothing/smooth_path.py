# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------


from math import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# ------------------------------------------------
# smooth coordinates
#

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.0000001):

    # Make a deep copy of path into newpath
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]


    #### ENTER CODE BELOW THIS LINE ###
    reached = False
    while reached == False:
        reached = True
        for i in range(len(newpath)):
            if i != 0 and i != (len(newpath) - 1):
                
                oldvalue = newpath[i][0]
                newpath[i][0] = newpath[i][0] + weight_data * (path[i][0] - newpath[i][0])
                newpath[i][0] = newpath[i][0] + weight_smooth * (newpath[i+1][0] + newpath[i-1][0] - 2 * newpath[i][0])
                difference = sqrt((oldvalue - newpath[i][0])**2)
                if difference > tolerance:
                    reached = False
                
                oldvalue = newpath[i][1]
                newpath[i][1] = newpath[i][1] + weight_data * (path[i][1] - newpath[i][1])
                newpath[i][1] = newpath[i][1] + weight_smooth * (newpath[i+1][1] + newpath[i-1][1] - 2 * newpath[i][1])
                
                difference = sqrt((oldvalue - newpath[i][1])**2)
                if difference > tolerance:
                    reached = False
    
    return newpath # Leave this line for the grader!

# feel free to leave this and the following lines if you want to print.
newpath = smooth(path)

# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'





