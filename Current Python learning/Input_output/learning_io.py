"""write mode"""
# ok = open("lilly.txt", 'w')
# ok.write("mereko toh ye acche se samajh mein aagaya")
# ok.close()
"""append mode"""
# ok = open("lilly.txt", 'a')
# ok.write("mereko toh ye acche se samajh mein aagaya\n")
# ok.close()
"""number of characters"""
# ok = open("lilly.txt", 'w')     # as write mode
# a = ok.write("mereko toh ye acche se samajh mein aagaya\n")
# print(a)
# ok.close()
"""handle read and write both"""
# ok = open("lilly.txt", 'r+')     # as write mode
# print(ok.read())
# number = 0
# a = ok.write("mereko toh ye acche se samajh mein aagaya \n")
# print(a)
# ok.close()
"""handle read and write both"""
# ok = open("lilly.txt", 'r')
# print(ok.tell())
# print(ok.readline())
# print(ok.tell())
# print(ok.readline())
# print(ok.tell())
# ok.close()

# with open("states.txt", 'r') as merifile:
#     a = merifile.read(10)
#     print(a)
#
# ok = open("lilly.txt", 'r')
# print(ok.read())
# ok.close()




