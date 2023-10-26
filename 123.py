# from functools import lru_cache
# import sys
# k=0
# for a1 in "АРБУЗ":
#     for a2 in "АРБУЗ":
#         for a3 in "АРБУЗ":
#             for a4 in "АРБУЗ":
#                 for a5 in "АРБУЗ":
#                     for a6 in "АРБУЗ":
#                         s=a1+a2+a3+a4+a5+a6
#                         if s.count('А')==3 and 'АА' in s and 'ААА' not in s:
#                             k+=1
# print(k)

# sys.setrecursionlimit(10000000)
# @lru_cache(None)
# def f(n):
#     if n >= 10000:
#        return n
#     if n % 2 == 0:
#         return f(n + 2) - 3
#     if n % 2 != 0:
#         return f(n + 2) + 1
# for i in range(10000,94,-1):
#     f(i)
#
# print(f(94)-f(80))
# f=open("C:\\Users\\student\\Downloads\\17_4367.txt")
# s=f.readlines()
# f.close()
# s=[int(x) for x in s]
# k=0
# mn= min([x for x in s if x%8==0 and x!=8])
# k=0
# p=tuple(1000000000000000)
# for i in range(len(s)-1):
#     if s[i]%mn==0 and s[i+1]%mn==0:
#         k+=1
#         print(s[i],s[i+1])
# nomer 1
# def f(a, p):
#     if (a>=88) and (p==3):
#         return True
#     if (a>=88) and (p==2):
#         return False
#     if (a<88) and (p==3):
#         return False
#     if p%2==1:
#         return f(a+1,p+1) and f(a+4,p+1) and f(a*3, p+1)
#     if p%2==0:
#         return f(a+1,p+1) or f(a+4,p+1) or f(a*3, p+1)
# for s in range(1,88):
#     if f(s,1)==True:
#         print(s)
# nomer 2
# def f(a, p):
#     if (a>=88) and (p==4):
#         return True
#     if (a>=88) and (p==3):
#         return False
#     if (a<88) and (p==4):
#         return False
#     if p%2==0: # vanya
#         return f(a+1,p+1) and f(a+4,p+1) and f(a*3, p+1)
#     if p%2==1: # petro
#         return f(a+1,p+1) or f(a+4,p+1) or f(a*3, p+1)
# for s in range(1,88):
#     if f(s,1)==True:
#         print(s)
# nomer 3
# def f(a, p):
#     if (a>=88) and (p==3 or p==5):  #v1 ili 2
#         return True
#     if (a>=88) and (p==2 or p==4):  # p1 ili 2
#         return False
#     if (a<88) and (p==5):  #v2 ili proigr
#         return False
#     if p%2==1: # petya
#         return f(a+1,p+1) and f(a+4,p+1) and f(a*3, p+1)
#     if p%2==0: # vanya
#         return f(a+1,p+1) or f(a+4,p+1) or f(a*3, p+1)
# for s in range(1,88):
#     if f(s,1)==True:
#         print(s)
# print('1 ЗАДАНИЕ')
# def f1(a,b, p):
#     if (a+b>=77) and (p==3): # petya
#         return True
#     if (a+b>=77) and (p==2): # ivan
#         return False
#     if (a+b<77) and (p==3):  # petro
#         return False
#     if p%2==1: # petr
#         return f1(a+1,b,p+1) or f1(a*2,b, p+1) or f1(a, b+1, p+1)  or f1(a, b*2, p+1)
#     if p%2==0: # vanya
#         return f1(a+1,b,p+1) or f1(a*2,b, p+1) or f1(a, b+1, p+1)  or f1(a, b*2, p+1)
# for s in range(1,77):
#     if f1(7,s,1)==True:
#         print(s)
#         break
#
# # nomer 2
# print('2 ЗАДАНИЕ')
# def f2(a,b, p):
#     if (a+b>=77) and (p==4): # petya
#         return True
#     if (a+b>=77) and (p==3): # ivan
#         return False
#     if (a+b<77) and (p==4):  # petro
#         return False
#     if p%2==0: # v
#         return f2(a+1,b,p+1) and f2(a*2,b, p+1) and f2(a, b+1, p+1)  and f2(a, b*2, p+1)
#     if p%2==1: # p
#         return f2(a+1,b,p+1) or f2(a*2,b, p+1) or f2(a, b+1, p+1)  or f2(a, b*2, p+1)
# for s in range(1,77):
#     if f2(7,s,1)==True:
#         print(s)
#
# # nomer 3
# print('3 ЗАДАНИЕ')
# def f3(a,b, p):
#     if (a+b>=77) and (p==3 or p==5): # petya
#         return True
#     if (a+b>=77) and (p==2 or p==4): # ivan
#         return False
#     if (a+b<77) and (p==5):  # petro
#         return False
#     if p%2==1: # v
#         return f3(a+1,b,p+1) and f3(a*2,b, p+1) and f3(a, b+1, p+1)  and f3(a, b*2, p+1)
#     if p%2==0: # p
#         return f3(a+1,b,p+1) or f3(a*2,b, p+1) or f3(a, b+1, p+1)  or f3(a, b*2, p+1)
# for s in range(1,77):
#     if f3(7,s,1)==True:
#         print(s)
# for el in '0123456789AB':
#   s = int('919' + x + '55747', 12) + int('18' + x + 'A551' + x + '', 12) + int('57' + x + 'A1716', 12) + int('8A' + x + '29', 12) + int('6' + x + '6AA3', 12) + int('A3B778' + x + '', 12)
#   if s % 11 == 0:
#       print(x, s // 11)
# def f(x,y,a):
#     return (x + y <= 54) or (y <= x + 3) or (y >= a)
# k = 0
# for a in range(10000):
#     if all(f(x,y,a) == 1 for x in range(1, 1000) for y in range(1, 1000)):
#         k += 1
# print(k)
#10
# """
# s='3'*6 + '4'*75
# while ('35' in s) or ('355' in s) or ('3444' in s):
#     if ('35' in s):
#         s=s.replace('35','4',1)
#     else:
#         if ('355' in s):
#             s = s.replace('355', '4', 1)
#         else:
#             s = s.replace('3444', '3', 1)
# print(s)"""
# #перевод в десятичную из любой: пример с 7 системой счисления
# # n = int('5342',7) перведет 5342 из 7 всегда в 10
# #перевод из десятичной в любую другую < 10
# """
# n=1782628 #десятичное число
# q= 5 #система счисления
# s=''
# while n>0:
#     c=str(n%q)
#     s=c+s
#     n=n//q
# print(s) #переведенное число"""
# 14 zadanie
# for x in range(80):
#     n= (3*(80**3)+ x*(80**2) + 7 * 80 ** 1 + 5) + (80 **3 + 4 * 80**2 + x*80)
#     if n%17==0:
#         print(x, n//17)
# for A in range(1,1000):
#     f=1
#     for x in range(1,1000):
#         if ((x%6==0)<=(x%10!=0)) or (x+A>121):
#             pass
#         else:
#             f=0
#             break
#     if f==1:
#         print(A)
# print('24 ЗАДАНИЕ')
# f=open("C:\\Users\\student\\Downloads\\24_4643.txt")
# s=f.readline()
# f.close()
# i=0
# k=0
# mx=0
# while i<(len(s)-2):
#     if (s[i] in ('12')) and (s[i+1] in ('12')) and (s[i+2] in ('AB')):
#         k+=1
#         mx=max(mx,k)
#         i+=3
#     else:
#         k=0
#         i+=1
# print(mx)
# print('25 ЗАДАНИЕ')
# from fnmatch import fnmatch
# for x in range(123890,12399890+1):
#     if fnmatch(str(x),('123*890')) == True:
#         if x%27==0:
#             print(x,x//27)
# print('26 ЗАДАНИЕ')
# f=open("C:\\Users\\student\\Downloads\\26_4938.txt")
# s=f.readlines()
# f.close()
# l,n=map(int, s.pop(0).split())
# s=[ list(map(int,x.split()))  for x in s]
# t0=0
# k=0
# t=[]
# s.sort(key=lambda x: x[1])
# for time in s:
#     start, end= time
#     if start>=t0:
#         k+=1
#         t.append(time)
#         t0=end
#
# from math import ceil
# print(t[-1])
# print(k)
# print('27 ЗАДАНИЕ')
# f=open("C:\\Users\\student\\Downloads\\27A_4721.txt")
# # f=open('test')
# s=f.readlines()
# f.close()
# n,v,m=map(int,s.pop(0).split())
# a=[ list(map(int,x.split()))  for x in s]
# Ni=sorted([x[0] for x in a])
# A=[[0, 0] for i in range(max(Ni)+1)]
# for x in a:
#     ind, probirka = x
#     A[ind]=[probirka,ceil(probirka/v)]
# mx_prob=0
# kont=0
# for i in Ni:
#     if i<m:
#       if sum([x[0] for x in A[0:i+m+1]]) > mx_prob:
#           mx_prob=sum([x[0] for x in A[0:i+m+1]])
#           kont=sum([x[1] for x in A[0:i+m+1]])
#     else:
#         if sum([x[0] for x in A[i-m:i + m + 1]]) > mx_prob:
#            mx_prob = sum([x[0] for x in A[i - m:i + m + 1]])
#            kont = sum([x[1] for x in A[i - m:i + m + 1]])
# print(mx_prob,kont)

