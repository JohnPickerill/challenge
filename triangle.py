from etimer import exec_timer

@exec_timer    
def get_triangle(filnam):
    with open(filnam, 'r') as f: 
        lines = f.read().split('\n')
    triangle = []
    for line in lines:
        try:
            triangle.append(map(int,line.strip().split(' ')))        
        except ValueError:
            print "invalid input line : <{0}>".format(line)
    return triangle 
       
@exec_timer
def cost(tri):
    costBelow = tri.pop()
    while (len(tri) > 0):
        row = tri.pop()
        costBelow = [max(v+costBelow[i],v+costBelow[i+1]) for i,v in enumerate(row) ]   
    return costBelow[0]      

def testCost():  
    tri = get_triangle('triangle_fixture.txt')
    assert cost(tri) == 202
 
     
