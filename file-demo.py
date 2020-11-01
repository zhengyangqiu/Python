#file object

# f=open("mbox.txt","r+")


# use context management

with open("mbox.txt","r") as rf:
    with open("test.txt","w") as wf:
        for line in rf:
            wf.write(line)



    # size_to_read=100
    #
    # f_content=f.read(size_to_read)
    #
    # while len(f_content)>0:
    #     print(f_content,end="")
    #     f_content=f.read(size_to_read)
    #     # f.seek(0) return to the first 0

# with open("mbox2.txt","w") as f2:#create a new  file
#     f2.write("hello world")







    # for line in f:# working with large file, can deal with memory issues
    #     print(line,end="")

    # f_content=f.readline()#grape the first line of file
    # print(f_content,end="")
    # f_content=f.readline()#grape the second line of file
    # print(f_content,end="")







# print(f.name)
# print(f.mode)


#
# f.close()
