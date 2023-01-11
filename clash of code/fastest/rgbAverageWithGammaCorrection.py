def convert(a):
    return (a/255)**2

def revert(a):
    return math.sqrt(a)*255

first = list(map(lambda x: convert(int(x)),input().split()))
second = list(map(lambda x: convert(int(x)),input().split()))


avg = [(x+y)/2 for x, y in zip(first, second)]

print(*list(map(lambda x: round(revert(x)), avg)))
