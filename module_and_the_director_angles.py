import math
cs=int(input("What dimension is the vector in? \n>> "))
vector=[]
for i in range(1,cs+1):
  v=float(input(f"v{i}\n>>"))
  vector.append(v)
mod=0
for e in vector:
  mod += e ** 2
mod=(mod)**(1/2)
angd=[]
for e in vector:
  alpha=e/mod
  angs = math.degrees(math.acos(alpha))
  angd.append(angs)
display(f'The modulus of the vector {vector} is {mod}')
display( f'and its angles are the following {angd}')
