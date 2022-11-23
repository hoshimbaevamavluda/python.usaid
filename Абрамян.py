# #begin 1
# def begin1(a):
#     return 4 * a
# P = begin1(4)
# print(P)
#
# #begin 2
# def begin1(a):
#     return a * a
# S = begin1(4)
# print(S)
#
# #begin 3
# def begin1(a, b):
#     S = a*b
#     P = 2*(a+b)
#     print(S, P)
# begin1(4, 5)
#
# #begin 4
# def begin4(d):
#     p = 3.14
#     return p * d
# S = begin4(4)
# print(S)

# #begin 5
# def begin5(a):
#     S = 6*(a**2)
#     V = a**3
#     print(S, V)
# begin5(4)

# #begin 6
# def begin6(a, b, c):
#     S = 2*(a*b + b*c + a*c)
#     V = a*b*c
#     print(S, V)
# begin6(4, 5, 1)

# #begin 7
# def begin7(R):
#     p = 3.14
#     S = p*R
#     V = 2*p*R
#     print(S, V)
# begin7(3)

# #begin 8 #найти среднее арифмет
# def begin8(a, b):
#     return (a+b)/2
# m = begin8(8, 1)
# print(m)

# #begin 9 #найти среднее геомет
# def begin9(a, b):
#     return (a+b) * (1/2)
# m = begin9(8, 1)
# print(m)

#begin10
# def begin10(a, b):
#     if a > 0 and b > 0:
#         return (a + b, \
#         a - b, \
#         (a**2)+(b**2), \
#         (a**2)//(b**2))
# s = begin10(4, 7)
# print(s)

#begin11
# def begin11(a, b):
#     if a > 0 and b > 0:
#         return (a + b, \
#         a - b, \
#         (a**2)+(b**2), \
#         (a**2)//(b**2))
# s = begin11(4, 7)
# print(s)

# #begin12
# def gipotenuza(a, b):
#      return ((a**2) + (b**2)) ** 0.5
# my_test = gipotenuza(4, 5)
# print(my_test)
#
# def perimetr(a, b):
#      return a + b
# my_test2 = perimetr(4, 5)
# print(my_test+my_test2)

#begin13
# def begin13(r1, r2):
#     if r1 > r2:
#         p = 3.14
#         s1 = p * (r1 ** 2)
#         s2 = p * (r2 ** 2)
#         s3 = s1 - s2
#         print(s1, s2, s3)
#     else:
#         print('r1<r2')
# begin13(6, 5)

# #begin14
# def begin14(L):
#     p = 3.14
#     r = L / (2 * p)
#     s = p * (r**2)
#     return r, s
# m = begin14(10)
# print(m)

# #begin15
# def begin15(S):
#     p = 3.14
#     D = 2*((S/p)**(1/2))
#     L = p * D
#     return D, L
# m = begin15(10)
# print(m)


#begin18
# def osi(a, b,c):
#      if c > a and c < b:
#           return abs(c-a)*abs(c-b)
#      else:
#           return "Error"
# my_test2 = osi(2, 5, 6)
# print(my_test2)

#begin34
# def begin34(a, x, b, y):
#      choco = a/x
#      iris = b/y
#      sootnoshenie = choco/iris
#      print("Шоколад:", choco)
#      print("Ирис:", iris)
#      print("Соотношение:", round(sootnoshenie, 2))
# begin34(2, 1, 5, 8)

#begin35
# def begin35(v, u, t1, t2):
#     if u < v:
#         s = v*t1+(v-u)*t2
#         return s
#     else:
#         return "u>v"
#
# p = begin35(5, 4, 8 ,1)
# print(p)

#begin36
# def begin36(v1, v2, t, s):
#     s1 = v1*t
#     s2 = v2*t
#     return s1 + s2 +s
#
# p = begin36(5, 4, 8 ,1)
# print(p)
#
#begin37
# def begin37(v1, v2, t, s):
#     s1 = v1*t
#     s2 = v2*t
#     return s - s1 + s2
#
# p = begin37(5, 4, 8 ,1)
# print(p)

#integer1
# def integer1(L):
#     return L//100
# m = integer1(300)
# print(m)
#
#integer2
# def integer2(M):
#     return M//1000
# m = integer2(4000)
# print(m)
#
#integer3
# def integer3(M):
#     return M//1024
# m = integer3(4000)
# print(m)
#
#integer11
# def integer11(M):
#     a1 = M//100
#     a2 = M%10
#     a3 = (M%100)//10
#     return (a1+a2+a3, a1*a2*a3)
# m = integer11(123)
# print(m)

#integer20
# def integer20(M):
#     return M//3600
# m = integer20(4000)
# print(m)

#integer24
# def integer24(M):
#     return M%7

# m = [
#     'воскресенье'
#     'понедельник'
#     'dnjh'
# ]

# print(integer24(40))
# print(m[integer24])

#integer29
# def integer29(A,B,C):
#     a = A//C
#     b = B//C
#     return (a*b)
# m = integer29(12, 5, 2)
# print(m)

#integer30
# def integer30(N):
#     if N % 100 == 0:
#         return (N//100)
#     else:
#         return ((N//100)+1)
# m = integer30(1901)
# print(m)

#boolean1
# def boolean1(A):
#     if A>0:
#         return "Число А яв-ся положительным"
#     else:
#         return "Число А яв-ся отрицательным"
# m = boolean1(1)
# print(m)

#boolean2
# def boolean2(A):
#     if A%2:
#         return "Число А яв-ся нечетным"
#     else:
#         return "Число А яв-ся четным"
# m = boolean2(11)
# print(m)

#boolean3
# def boolean3(A):
#     if A%2==0:
#         return "Число А яв-ся четным"
#     else:
#         return "Число А яв-ся нечетным"
# m = boolean3(99)
# print(m)

#boolean4
# def boolean4(A, B):
#     if A>2 and B<=3:
#         return "Справедливы неравенства"
#     else:
#         return "Ошибка"
# m = boolean4(99, 2)
# print(m)

#boolean5
# def boolean5(A, B):
#     if A>=0 and B<-2:
#         return "Справедливы неравенства"
#     else:
#         return "Ошибка"
# m = boolean5(99, -1)
# print(m)

#boolean6
# def boolean6(A, B, C):
#     if A < B < C:
#         return "Справедливы неравенства"
#     else:
#         return "Ошибка"
# m = boolean6(1, 9, 10)
# print(m)

#boolean7
# def boolean7(A,B,C):
#     if A<=B<=C:
#         return "Число B находится между числами А и С"
#     else:
#         return 'Не находится'
# m = boolean7(7, 10, 9)
# print(m)

#boolean8
# def boolean8(A,B):
#     if A%2>0 and B%2>0:
#         print('A И B нечетное')
# boolean8(7, 10)
#
#boolean9
# def boolean9(A,B):
#     if A%2>0 and B%2>0:
#         print('A И B нечетное')
#         if A%2>0 or B%2>0:
#             print('Ровно одно из A И B нечетное')
# boolean9(7, 10)

#boolean10
# def boolean10(A,B):
#     if A % 2 > 0 or B % 2 > 0:
#         print('1 но из A И B нечетное')
#     else:
#         print("четное")
# boolean10(4, 10)

#boolean11
# def boolean11(A,B):
#     if A % 2 == 0 and B % 2 == 0:
#         print('1 вая четность')
#     else:
#         print("нечетное")
# boolean11(2, 7)

#boolean12
# def boolean12(A,B,C):
#     if A > 0 and B > 0 and C > 0:
#         print('положительное')
#     else:
#         print("отрицательное")
# boolean12( 2,  7, - 1)

#boolean13
# def boolean13(A,B,C):
#     if A > 0 or B > 0 or C > 0:
#         print('1 но положительное')
#     else:
#         print("отрицательное")
# boolean13(- 2, - 7, -1)

