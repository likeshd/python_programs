##Convert an integer into decimals
# import decimal
# integer = 10
# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))

## Converting an string of Integers into Decimals
# import decimal
# string = "122345"
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string)))

##Reversing a string using an Extended Slicing Technique
# s1 = "Python Programming"
# w = s1.lower()
# print(w)
# print(w[::-1])

##Count vowels
# vowel = ['a','e','i','o', 'u']
# word = "programming"
# count = 0
# for ch in word:
#     if ch in vowel:
#         count = count + 1
# print(count)

# ##counting the number of occurances of a character in string
# word = "programming"
# d = {}
# for ch in word:
#     if ch in d:
#         d[ch] = d[ch] + 1
#     else:
#         d[ch] = 1
# print(d)

##Fibonacci Series
# fib = [0,1]
# n = 5
# for i in range(5):
#     fib.append(fib[-1]+ fib[-2])
# print(fib)
# v=",".join(str(e) for e in fib)
# print(v)

##the Max number in List
# l1 = [4,56,78,2,5,48,69,94,7,8]
# max = 0
# for num in l1:
#     if num > max:
#         max = num
# print(max)

## Finding middle element in list
# l1 = [4,56,78,2,5,48,69,94,7,8]
# l2 = sorted(l1)
# print(l2)
# m = len(l2)/2
# print(m)
# print(l2[int(m)])

##Coverting list into a string

# s = "P Y H T O N"
# x = s.split(" ")
# print(x)
# n = "".join(x)
# print(n)
# print(n.split())

## counting spaces in string
st = "P r ogram in g"
print(st.count(" "))




