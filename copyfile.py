import os
lines = ['Hello','World', 'Welcome to Python.shiksha']
path = "E:/File_Operation/test.txt"
f=open(path,'w')
for i in lines:
    f.write(i+'\n')

# ===============================================================================
# dirName = "Test"
fileName ="file1.txt"

location = "E:\File_Operation"


filePath = os.path.join(location, fileName)

# dirPath = os.path.join(location, dirName)

os.remove(filePath)
print("File Succesfully Removed")

# os.remove(dirPath)
# print("Directory Succesfully Removed !")