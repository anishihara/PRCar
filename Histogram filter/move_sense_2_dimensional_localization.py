colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

def sense(p,Z):
    q = [[0.0 for j in range(len(colors[i]))] for i in range(len(colors))]
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            hit = (Z == colors[i][j])
            q[i][j]=(hit*sensor_right + (1-hit)*(1-sensor_right))*p[i][j]
    s = sum(sum(q[i]) for i in range(len(q)))
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            q[i][j] = q[i][j]/s
    return q

def move(p,U):
    q = [[0.0 for j in range(len(colors[i]))] for i in range(len(colors))]
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            q[i][j] = (1-p_move) * p[i][j]
            q[i][j] += p_move * p[ (i-U[0]) % len(colors) ][ (j-U[1]) % len(colors[i]) ]
    return q

def initialize_world():
    n = len(colors)*len(colors[0])
    probability = 1.0/n
    q = [[probability for j in range(len(colors[i]))] for i in range(len(colors))]
    return q

p = []

p = initialize_world()

for i in range(len(motions)):
    p = move(p,motions[i])
    p = sense(p,measurements[i])


#Your probability array must be printed 
#with the following code.

show(p)




