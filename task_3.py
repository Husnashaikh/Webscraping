# import json
# from task_1 import top_movie_list
# from task_2 import  group_by_year
# dec_arg=group_by_year(top_movie_list)
# def group_by_decade(movies):
#     moviedec={}
#     list1=[]
#     for index in movies:
#         mod=index%10
#         decade=index-mod
#         if decade not in list1:
#             list1.append(decade)
#     list1.sort()
#     for i in list1:
#         moviedec[i]=[]
#     for i in moviedec:
#         dec10=i+9
#         for x in movies:
#             if x <=dec10 and x>=i:
#                 for v in movies[x]:
#                     moviedec[i].append(v)
#     with open("3_task.json","w")as f:
#         json.dump(moviedec,f,indent=4)
#         return(moviedec)
# print(group_by_decade(dec_arg)) 
