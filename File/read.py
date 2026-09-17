#f = open("File/file.txt", "r")
#data =f.read()
# data2 = f.readline()
#print(data)
# print(data2)
#print(type(data))
#f.close()

with open('File/file.txt','r') as f:
    data =f.read()
    print(data)
    