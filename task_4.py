from bs4 import BeautifulSoup
import requests 
import json
# from task_1 import top_movie_list
# def scrap_movie_details(movie_urt):
#     page=requests.get(movie_urt)
#     soup=BeautifulSoup(page.text,'html.parser')
#     title=soup.find('div',class_='col mod col-center-right col-full-xs mop-main-column')


def scrap_movie_details(movie_url):
    page=requests.get(movie_url)
    # print(page)
    soup=BeautifulSoup(page.text,'html.parser')
    # print(sour)
    title=soup.find('div',class_="col mob col-center-right col-full-xs mop-main-column")
    # Title = title.find('div',class_ = "thumbnail-scoreboard-wrap").h1.get_text()
    # print(Title)
    title1=title.find('div',class_="thumbnail-scoreboard-wrap")
    # print(title1)
    poster=title1.find('img',class_="posterImage js-lazyLoad")
    poster1=poster['src']
    # print(poster1)
    name=title1.find('h1',class_="scoreboard__title").get_text()
    # print(name)
    info=soup.find('div',class_="panel-body content_body")
    genre=info.find('div',class_="meta-value genre").get_text().split()
    # print(genre) 
    sub_title=info.find_all('li',class_="meta-row clearfix")
    # print(sub_title)
    m_info=info.find('div',class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    # print(m_info)
    one_dict={}
    one_dict['Name']=name
    for i in sub_title:
        # print(i)
        key=i.find('div',class_="meta-label subtle").get_text().replace(":","")     
        value=i.find('div',class_="meta-value").get_text().replace(" ","").replace("\n","").strip()
        one_dict[key]=value
    # print(one_dict)
    time=int(one_dict['Runtime'][0])*60
    time=time+int(one_dict['Runtime'][2:-1])
    # print(time)
    one_dict['Runtime']=str(time)+'m'
    one_dict['Poster_image_url']=poster1
    one_dict['Movie_info']=m_info
    one_dict['Genre']=genre
    # pprint(one_dict)   
    with open ("4_task.json","w")as f:
        json.dump(one_dict,f,indent=4)
        return one_dict   
print(scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018"))