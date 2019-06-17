# def is_palindrome_v3(s):
#     """ (str) -> bool

#     Return True if and only if s is a palindrome.

#     >>> is_palindrome_v3('noon')
#     True
#     >>> is_palindrome_v3('racecar')
#     True
#     >>> is_palindrome_v3('dented')
#     False
#     """

#     # for i in range(len(s) // 2):
#     #     if s[i] != s[len(s) - i - 1]:
#     #         return False

#     # for i in range(len(s) // 2):
#     #     if s[i] != s[len(s) - i]:
#     #         return False

#     # j = len(s) - 1
#     # for i in range(len(s) // 2):
#     #     if s[i] != s[j - i]:
#     #         return False

#     for i in range(len(s) // 2 + 1):
#         if s[i] != s[len(s) - i - 1]:
#             return False

#     return True

#     return True


# print(is_palindrome_v3("n"))  # True
# print(is_palindrome_v3("oo"))  # True
# print(is_palindrome_v3("noon"))  # True
# print(is_palindrome_v3("racecar"))  # True
# print(is_palindrome_v3("dented"))  # False


# def is_anagram(s1, s2):
#     """ (str, str) -> bool

#     Return True if and only if s1 is an anagram of s2.

#     >>> is_anagram("silent", "listen")
#     True
#     >>> is_anagram("bear", "breach")
#     False
#     """

#     # create lists of both and sort them
#     # l1 = list(s1).sort()
#     # l2 = list(s2).sort()
#     # return l1 == l2


# print(is_anagram("silent", "listen"))
# print(is_anagram("bear", "breach"))


# def count_startswith(L, ch):
#     """ (list of str, str) -> int

#     Precondition: the length of each item in L is >= 1, and len(ch) == 1

#     Return the number of strings in L that begin with ch.

#     >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
#     2
#     """

#     # count = 0
#     # for item in L:
#     #     if item.startswith(ch):
#     #         count = count + 1
#     # return count

#     # startswith = L[:]
#     # for item in L:
#     #     if item.startswith(ch):
#     #         startswith.remove(item)
#     # return len(L) - len(startswith)

#     # startswith = L[:]
#     # for item in L:
#     #     if not item.startswith(ch):
#     #         startswith.remove(item)
#     # return len(L)

#     count = 0
#     for item in L:
#         if item.startswith(ch):
#             count = count + 1
#             return count
#         else:
#             return count


# print(count_startswith(["rumba", "salsa", "samba"], "s"))

