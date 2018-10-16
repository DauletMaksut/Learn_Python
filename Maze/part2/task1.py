# def appendAndDelete(s, t, k):
#     #bacis operation
#     s = s.strip()
#     t = t.strip()
#     if s == t:
#         print("strang")
#         return "Yes"
#     if k == 0:
#         return "No"
#     check = 0
#     while True:
#         if s in t:
#             if k - check == len(t) - len(s):
#                 print(k - check)
#                 # print(len(t) - len(s))
#                 return "Yes"
#         s = s[:-1]
#         check += 1
#         if check > k:
#             return "No"
# print(appendAndDelete("asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv", "bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv", 100))
# print(len("asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"))
print(int(345.999))