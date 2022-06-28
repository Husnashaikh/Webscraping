import json
from task_1 import top_movie_list
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i['year']
        if year not in years:
            years.append(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        year=i["year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append([i])
    with open("2_task.json","w")as f:
        json.dump(movie_dict,f,indent=4)
        return movie_dict
print(group_by_year(top_movie_list))