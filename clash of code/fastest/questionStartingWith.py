# solved in 1m
question_prefix = input()
n = int(input())
x=True
for i in range(n):
    row = input()
    if row.startswith(question_prefix):print(row);x=False
if x:
    print("EMPTY")
