world_map = """5 4
5 5 5 5 5
5 4 4 4 5
5 3 2 1 5
5 5 5 5 5"""

#X,Y=map(int,input().split())
X=5
Y=4
world=[list(map(int,l.split())) for l in world_map.splitlines()[1:]]
visited=[[False]*len(l) for l in world]

print(visited)    
