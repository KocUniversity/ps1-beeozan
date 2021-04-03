n, B = list(map(int, input().strip().split()))
T = 0

# your code here

h = 0
mysum = 0

def f_t (x):
  global mysum
  for i in range(1, n+1):
    if i%2 == 0:
      mysum += (2**i + 1)**(n-i)
    elif i%2 == 1:
      mysum += (3**i + 1)**(n-i)
  return mysum * x

while T < 10000 and h < B:
  T += 1
  mysum = 0
  h = f_t (T)

if T == 10000: 
  T = -1

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)