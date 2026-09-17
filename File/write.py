f = open("File/file.txt",'a')
f.write(" ")
f.close()

with open('File/file2.txt','w') as f:
    f.write("This is to delete")

