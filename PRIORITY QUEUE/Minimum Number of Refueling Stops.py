from heapq import *
def minRefuelStops(target,startfuel,stations):
    currentfuel=startfuel
    stops=0
    max_heap=[]
    
    for station in stations:
        position=station[0]
        fuel=station[1]
        
        while currentfuel < position:
            if len(max_heap)==0:
                return -1
            max_fuel=heappop(max_heap)
            currentfuel +=(-max_fuel)
            stops +=1
        heappush(max_heap,-fuel)
    
    while currentfuel<target:
        if len(max_heap)==0:
            return -1
        max_fuel=heappop(max_heap)
        currentfuel +=(-max_fuel)
        stops +=1
    return stops
target=120
startfuel=10
stations=[[10,60],[20,30],[30,30],[60,40]]
ans=minRefuelStops(target,startfuel,stations)
print(ans)
     