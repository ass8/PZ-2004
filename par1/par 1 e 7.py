print("First liquid volume v1=")
v1 = input()
print('First liquid temperature t1=')
t1 = input()
print('Second liquid volume v2=')
v2 = input()
print('Second liquid temperature t2=')
t2 = input()
v=v1+v2
t=(v1*t1+v2*t2)/v
print('volume=',v,' temperature=',t)