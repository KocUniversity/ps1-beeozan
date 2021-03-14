n, B = list(map(int, input().strip().split()))
T = 0

# your code here

mysum = 0
min_value = 0
max_value = 10000
result = 0
T2 = 0

def f_t (x):
  global mysum
  for i in range(1, n+1):
    if i%2 == 0:
      mysum += (2**i + 1)**(n-i)
    elif i%2 == 1:
      mysum += (3**i + 1)**(n-i)
  return mysum * x

eps = 1e-5

while result < B:
  mysum = 0
  T2 = (min_value + max_value)/2
  result = f_t(T2)    
  
  while B < result: 
    max_value = T2
    T2 = (T2 + min_value)/2
    mysum = 0
    result = f_t(T2)
    if result-B < eps:
      T = int(T2) + 1 
      break
    
  if result < B:
    min_value = T2
    if T2 == 10000:
      T = -1
      break
  elif result == B: 
    T = int(T2) + 1
  
# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)
