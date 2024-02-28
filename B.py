# ============================================================================
# Authors: Joana Pires & Manuel Santos
# Date: 28/02/2024
# ============================================================================
# -> Run
# python3 B.py
# ============================================================================

# === Reading from file
# Open file
# file = open('B.txt', 'r')

# Read Lines
# Lines = file.readlines()
# file.close()
# # print(Lines)

# === Reading from stdin (input())
Lines1 = input()
Lines1 = Lines1.split(" ")
# print(Lines)
Lines2 = input()
Lines2 = Lines2.split(" ")

# ===== Process first line
N = int(Lines1[0])
if N < 1 or N > 1000:
    exit()
# print("Largura:" +  str(N))
S = int(Lines1[1])
if S < 1 or S > 1000:
    exit()
# print("Sysufu:" +  str(S))
if N < S:
    exit()

# ===== Process second line
mountain = Lines2
# print(mountain)
# print(type(mountain[0]))
max_M = max(mountain)
if int(max_M) < 1 or int(max_M) > 1e6:
    exit()

for i in range(0, len(mountain)-1):
    if int(mountain[i]) == int(mountain[i+1]):
        exit()

# ===== Calculate
idx = S-1

# == Pontas
ponta = False
if S == 1:
    idx +=1
    ponta = True
if S == N:
    idx -=1
    ponta = True   

# == Cumes e Vales
if ponta == False and (int(mountain[idx-1]) < int(mountain[idx]) and int(mountain[idx+1]) < int(mountain[idx])) or (int(mountain[idx-1]) > int(mountain[idx]) and int(mountain[idx+1]) > int(mountain[idx])):
    print(int(0))
    exit()

# print(mountain)

while(True):
    # == Esquerda
    if int(mountain[idx-1]) < int(mountain[idx]):
        idx -= 1
        # print('left')
    elif int(mountain[idx+1]) < int(mountain[idx]):
        idx += 1
        # print('right')
    else:
        print(int(abs(idx - S + 1)))
        exit()