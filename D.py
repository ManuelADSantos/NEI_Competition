# S = input()
# if len(S) <1 or len(S) > 30:
#     exit()

# M = input()
# if len(M) != 1:
#     exit()

x = "BBAC"
print(2**int(len(x)-1))

hypo = ["X" for letter in range(2**int(len(x)-1))]
print(hypo)

# while len(x) > 1:
#     print(x)
#     new_x = x[1:len(x)]
#     print(new_x)
#     sample = x[0:2]
#     print(sample)

#     # if 
#     break