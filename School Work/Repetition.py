# import time
# print("Number?")
# a = int(input())
# sum = 0
# counts = 1
# while counts < a+1 :
#     print(sum, "+", counts, "= ", end=" ")
#     sum = sum + counts
#     counts += 1
#     print(sum)
n = int(input("What number: "))
rep = n - 1
end = n
while rep != 1:
    print(end, "*", rep, "=", end=" ")
    end = end * (rep)
    rep -= 1
    print(end)
else:
    print("Finish Calculating, Answer=", end)
