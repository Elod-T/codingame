import math


inputs = sorted(map(int, input().split()))

print(math.ceil(sum(inputs)/len(inputs)) if len(inputs)%2 == 0 else inputs[int((len(inputs)+1)/2)-1])
