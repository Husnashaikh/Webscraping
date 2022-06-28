# from array import array
import json
def movie_directed():
    a=open("5task.json","r")
    b=json.load(a)
    list=[]
    for i in b:
        if i["original language"]not in list:
            list.append(i["original language"])
    ar={}
    list1=[]
    for k  in list:
        i=0
        coun=0
        while i<len(b):
            if k==b[i]["original language"]:
                coun=coun+1
            i=i+1
        ar.update({k:coun})
    list1.append(ar)
    with open("6_task.json","w")as f:
        json.dump(ar,f,indent=4)
    return ar
movie_directed()