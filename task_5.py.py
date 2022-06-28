from task_1 import top_movie_list
import json
from bs4 import BeautifulSoup
import requests
list4=[]
for i in top_movie_list[:100]:
    url=i['movie URL']
    def get_movie_list_details(movies):
        x=requests.get(movies)
        soup=BeautifulSoup(x.text,"html.parser")
        movie_find_2=soup.find("ul",class_="content-meta info")
        # print(movie_find_2)
        movie_find_3=movie_find_2.find_all("li",class_="meta-row clearfix")
        # print(movie_find_3)
        my_dict={}
        for i in movie_find_3:
            alldata=i.find("div",class_="meta-label subtle").get_text().strip()[:-1]
            allvalue=i.find("div",class_="meta-value").get_text().strip().replace(" ","").replace("\n","").replace("\u00a0","")
            my_dict["name"]=soup.find('h1').text
            # print(alldata)
            my_dict[alldata]=allvalue
        list4.append(my_dict)
        # print(my_dict)
        with open("5_task.json","w")as f:
                json.dump(list4,f,indent=4)
        return list4
    get_movie_list_details(url)

