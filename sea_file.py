import os
import os.path

def quick(file_name):
    main_dir=[r"C:\Users\pratiksha shetty\Desktop",r"C:\Users\pratiksha shetty\Downloads"]
    path_list=[]
    for cur_dir in main_dir:
        file_list = os.listdir(cur_dir)
        f=file_name.lower()
        for j in file_list:
            if os.path.isdir(cur_dir+"\\"+j):
                try:
                    path_list+=op(cur_dir+"\\"+j,f)
                except:
                    pass
            if j.lower().find(f)!=-1:
                temp=cur_dir+"\\"+j
                path_list.append(temp)
    path_list = [x for x in path_list if x != []]
    path_list = Remove(path_list)
    return path_list
        
     

def file_op(file_name):
    cur_dir = os.getcwd()
    path_list=[]
    while True:
        file_list = os.listdir(cur_dir)
        parent_dir = os.path.dirname(cur_dir)
        i=0
        f=file_name.lower()
        for j in file_list:
            if os.path.isdir(cur_dir+"\\"+j):
                try:
                    path_list+=op(cur_dir+"\\"+j,f)
                except:
                    pass
            if j.lower().find(f)!=-1:
                temp=cur_dir+"\\"+j
                path_list.append(temp)
        if cur_dir == parent_dir: 
            break
        else:
            cur_dir = parent_dir
    path_list = [x for x in path_list if x != []]
    path_list = Remove(path_list)
    return path_list

def op(temp,f):
    path_list2=[]
    file_list2 = os.listdir(temp)
    for j in file_list2:
        if os.path.isdir(temp+"\\"+j):
            try:
                path_list2+=op(temp+"\\"+j,f)
            except:
                pass
        if j.lower().find(f)!=-1:
            temp2=temp+"\\"+j
            path_list2.append(temp2)
    return path_list2

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        num1=os.path.normpath(num)
        if num1 not in final_list: 
            final_list.append(num1) 
    return final_list 





    
# i=1
# s=quick("jarvis")
# print()
# print("Search results total: "+str(len(s)))
# print()
# for a in s:
#     print(str(i)+".]     "+a)
#     i+=1


# j=len(s)
# path=s[j-3]
# print(path)
# os.path.abspath("path")
# os.startfile(path)
