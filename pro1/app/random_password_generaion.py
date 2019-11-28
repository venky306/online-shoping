# # import string
# # import random
# #
# # def randomPassword(charecters):
# #     letters = string.ascii_letters
# #     password = ''
# #     for x in range(charecters):
# #         password+=random.choice(letters)
# #     return password
# #
# #
# indo='1001001'
# name='vishnu toys'
# contact='7396668356'
# email='vishnu.vardhan924@gmail.com'
# mp=str(int(indo)+len(name))
# mp=contact[0]+mp+contact[-1]
# mp=email[0]+mp[:int(len(mp)/2)]+email[5]+mp[int(len(mp)/2):]+email[4]
# print(mp)