from numpy import array, zeros, argmin, inf,empty
from collections import deque

def 2DDW(x,y,dist):
    """
    Computes 2-dimensional Dynamic Warping of two images.
    :param 2D-array x: N1*M1 array
    :param 2D-array y: N2*M2 array
    :param func dist: distance used as cost measure
     Returns the minimum distance, the cost matrix, the accumulated cost matrix, and the wrap path.
    """
    assert len(x)
    assert len(y)
    N1,M1=x.shape
    N2,M2=y.shape
    D = zeros((N1,M1,N2,M2))
    for i in Calculation_Order(N1,M1,N2,M2):
        '''
        cost1 =DTW(R1, R2)+DTW(C1, C2), where R1 is the i1-th row
        in image I1 from column 1 through column i1, C1 is the j1-
        th column in image I2 from row 1 through row j1. 
        '''
        D[i[0],i[1],i[2],i[3]]

def Calculation_Order(N1,M1,N2,M2):
    max_value=(N1,M1,N2,M2)
    Queue = deque()
    Stage_List = deque()
    Current_Stage = (N1,M1,N2,M2)
    Queue.append(Current_Stage)
    while len(Queue) != 0:
        Current_Stage = Q.pop()
        Stage_List.appendleft(Current_Stage)
        for i in previous_stage(Current_Stage):
            #Verify that the boundaries are inside of both images
            if verify_boundaries(i,max_value):
                if i not in Queue: 
                    Queue.append(i)
    return Stage_List

def verify_boundaries(stage,max_value):
    for i in range(len(stage):
        if stage[i] < 0 or stage[i] > max_value[i]:
            return False
    return True
                    

def traceback(D):
    """
    Calculate the path that contains the optimal locations
    D is the cost matrix
    """

    return array(p),array(q)

def previous_stage(stage):
    previous = []
    for i in [-1,0]:
        for j in [-1,0]:
            for k in [-1,0]:
                for l in [-1,0]:
                    previous.append( (stage[0]+i,stage[1]+j,stage[2]+k,stage[3]+l))
    return previous
