from functools import reduce

def _print(lst, m = 4):
    l = len(lst)
    #m = l / 12
    s = ""
    for i in range(l):
        if i % m == 0 and i != 0 :
            s += "  "
        s+= lst[i]
    print(s)

def PC_1(_key):     #list 
    pc_talbe = [
        57,    49,  41,    33,     25,  17,     9,
        1,     58,  50,    42,     34,  26,     18,
        10,    2,   59,    51,     43,  35,     27,
        19,    11,  3,     60,     52,  44,     36,
        63,    55,  47,    39,     31,  23,     15,
        7,     62,  54,    46,     38,  30,     22,
        14,    6,   61,    53,     45,  37,     29,
        21,    13,  5,     28,     20,  12,     4
    ]
    
    pc_1 = reduce(lambda x,y: x + [_key[y-1]], pc_talbe, [])
    return pc_1

def C_D(pc_1):
    l_CD = []
    l_CD.append([pc_1[:28],pc_1[28:]])  # C_0 D_0

    d_shifts = {
        "1": 1,         "2": 1,         "3": 2,         "4": 2,
        "5": 2,         "6": 2,         "7": 2,         "8": 2,
        "9": 1,         "10": 2,        "11": 2,        "12": 2,
        "13": 2,        "14": 2,        "15": 2,        "16": 1 
    }
    for i in range(1,17):
        C = [*l_CD[i - 1][0]]
        D = [*l_CD[i - 1][1]]
        for j in range(d_shifts[str(i)]):
            C.append(C.pop(0))
            D.append(D.pop(0))
        l_CD.append([C,D])
    return l_CD
def KEYS(C_Ds):         # list [[..]]
    keys = []
    pc2_table = [
        14, 17, 11, 24, 1,  5,
        3,  28, 15, 6,  21, 10,
        23, 19, 12, 4,  26, 8,
        16, 7,  27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]
    for i in range(1,17):
        CD = C_Ds[i][0] + C_Ds[i][1]
        key = reduce(lambda x, y: x + [CD[y-1]] ,pc2_table, [])
        keys.append(key)
    return keys
def IP(_mes):
    ip_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9,  1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    return reduce(lambda x, y: x + [_mes[y-1]] ,ip_table, [])
def expend_R(R):
    e_table = [
        32, 1,  2 , 3,  4,  5, 
        4,  5,  6 , 7,  8,  9,
        8,  9,  10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]
    return reduce(lambda x, y: x + [R[y-1]] ,e_table, [])
def XOR(a,b):
    ab= zip(a,b)
    return reduce(lambda x,y: x + [str(int(y[0]) ^ int(y[1]))], ab, [])

def P_B(B):
    pb_table = [
        16, 7,  20, 21, 29, 12, 28, 17,
        1,  15, 23, 26, 5,  18, 31, 10,
        2,  8,  24, 14, 32, 27, 3,  9,
        19, 13, 30, 6,  22, 11, 4,  25
    ]
    return reduce(lambda x,y: x + [B[y-1]], pb_table, [])
def re_IP(m):
    re_ip_table=[
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9,  49, 17, 57, 25
    ]
    return reduce(lambda x,y: x + [m[y-1]], re_ip_table, [])

def S1(B1):
    s1_table = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]
    id_1 = int(B1[0]) * 2 + int(B1[5])
    id_2 = int(B1[1]) * 8 + int(B1[2]) * 4 + int(B1[3]) * 2 + int(B1[4])
    return list(format(s1_table[id_1][id_2],'04b'))        

def S2(B2):
    s2_table = [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ]
    id_1 = int(B2[0]) * 2 + int(B2[5])
    id_2 = int(B2[1]) * 8 + int(B2[2]) * 4 + int(B2[3]) * 2 + int(B2[4])
    return list(format(s2_table[id_1][id_2],'04b'))       

def S3(B3):
    s3_table = [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ]
    id_1 = int(B3[0]) * 2 + int(B3[5])
    id_2 = int(B3[1]) * 8 + int(B3[2]) * 4 + int(B3[3]) * 2 + int(B3[4])
    return list(format(s3_table[id_1][id_2],'04b'))       
def S4(B4):
    s4_table = [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ]
    id_1 = int(B4[0]) * 2 + int(B4[5])
    id_2 = int(B4[1]) * 8 + int(B4[2]) * 4 + int(B4[3]) * 2 + int(B4[4])
    return list(format(s4_table[id_1][id_2],'04b'))       
def S5(B5):
    s5_table = [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ]
    id_1 = int(B5[0]) * 2 + int(B5[5])
    id_2 = int(B5[1]) * 8 + int(B5[2]) * 4 + int(B5[3]) * 2 + int(B5[4])
    return list(format(s5_table[id_1][id_2],'04b'))       
def S6(B6):
    s6_table = [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ]
    id_1 = int(B6[0]) * 2 + int(B6[5])
    id_2 = int(B6[1]) * 8 + int(B6[2]) * 4 + int(B6[3]) * 2 + int(B6[4])
    return list(format(s6_table[id_1][id_2],'04b'))       
def S7(B7):
    s7_table = [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ]
    id_1 = int(B7[0]) * 2 + int(B7[5])
    id_2 = int(B7[1]) * 8 + int(B7[2]) * 4 + int(B7[3]) * 2 + int(B7[4])
    return list(format(s7_table[id_1][id_2],'04b'))       

def S8(B8):
    s8_table = [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
    id_1 = int(B8[0]) * 2 + int(B8[5])
    id_2 = int(B8[1]) * 8 + int(B8[2]) * 4 + int(B8[3]) * 2 + int(B8[4])
    return list(format(s8_table[id_1][id_2],'04b'))       
def S_boxes(xor_exp):
    return S1(xor_exp[:6]) + S2(xor_exp[6:12]) + S3(xor_exp[12:18]) + S4(xor_exp[18:24]) + S5(xor_exp[24:30]) + S6(xor_exp[30:36]) + S7(xor_exp[36:42]) + S8(xor_exp[42:])
def func(R_pre,K):
    e_R_pre = expend_R(R_pre)
    xor_exp = XOR(e_R_pre,K)
    s_boxes = S_boxes(xor_exp)
    return P_B(s_boxes)


def encrypt_DES(M, K):       # list of bits
    kplus = PC_1(K)
    C_Ds = C_D(kplus)
    keys = KEYS(C_Ds)
    ip_mess = IP(M)
    L_pre = ip_mess[:32]
    R_pre = ip_mess[32:]
    for i in range(0,16):
        L = R_pre
        R = XOR(L_pre,func(R_pre,keys[i]))
        L_pre = L
        R_pre = R
    return re_IP(R_pre + L_pre)







mes = """0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101
1110 1111"""
key = """ 00010011 00110100 01010111 01111001 10011011 10111100 11011111
11110001"""
# for c in mes:
#     if c is not " ":
#         _mes.append(c)
_mes = reduce(lambda x,y: x + [y] if y == "0" or y == "1" else x,list(mes),[])
_key = reduce(lambda x,y: x + [y] if y == "0" or y == "1" else x,list(key),[])

ciphertext =  encrypt_DES(_mes,_key)
_print(ciphertext)


#pc_1 = PC_1(_key)
#_print(pc_1,7)
#C_Ds = C_D(pc_1)
#_print(C_Ds[0][0])
#_print(C_Ds[0][1])
#keys = KEYS(C_Ds)
#_print(keys[0])    #key1
#_print(keys[1])
#_print(keys[2])
#_print(keys[3])
#_print(keys[4])
#ip = IP(_mes)
#_print(ip[:32])
#_print(ip[32:])
#e_R_0 = expend_R(ip[32:])
#_print(e_R_0)
# A = XOR(e_R_0,keys[0])
# _print(A,6)
# s1 =  S1(A[:6])
# s2 =  S2(A[6:12])
# s3 =  S3(A[12:18])
# s4 =  S4(A[18:24])
# s5 =  S5(A[24:30])
# s6 =  S6(A[30:36])
# s7 =  S7(A[36:42])
# s8 =  S8(A[42:])
# _print(s1)
# _print(s2)
# _print(s3)
# _print(s4)
# _print(s5)
# _print(s6)
# _print(s7)
# _print(s8)
#b = "0000 1100 0010 0001 0110 1101 0101 0000"
#_b = reduce(lambda x,y: x + [y] if y == "0" or y == "1" else x,list(b),[])
#pb = P_B(_b)
#_print(pb)
#R_1 = XOR(pb,ip[:32])
#_print(R_1)
#ciper = re_IP(R_1 + ip[32:])
#_print(ciper)