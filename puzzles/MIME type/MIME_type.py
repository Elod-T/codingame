# 100%
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

table = dict()
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    table[ext.lower()] = mt
for i in range(q):
    *fname, ext = input().lower().split(".")  # One file name per line.
    print(table[ext] if ext in table and len(fname) > 0 else "UNKNOWN")
