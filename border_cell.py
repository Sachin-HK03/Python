# testcase = int(input())
# row = int(input())
# col = int(input())
# counter=0
# for i in range(row):
#     for j in range(col):
#         if i == '#':
#             counter +=1
#         print(counter)

t=int(input())
for i in range(t):
    row,column = map(int, input().split())
    counterlist = []
    for r in range(row):
        counter = 0
        for i in input():
            if i == '#':
                counter+=1
                counterlist.append(counter)
            print(max(counterlist))
            for _ in range(int(input())):
                n, m = map(int, input().split())
                lst = []
                for i in range(n):
                    row = input()
                    lst.append(row.count('#'))
                print(max(lst))


