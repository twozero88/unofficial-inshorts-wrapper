import requests
from requests import exceptions
import json

def fetchNews(category,number,lang='en'):
    result={}
    categories=['top_stories','trending','all_news']
    result['category']=category
    if number>1000:
        result['data']=""
        result['success']="False"
        result['error']="You are being too greedy.No more than 1000 items at a time."
    if category in categories:
        url="https://inshorts.com/api/"+lang+"/news?category="+category+"&max_limit="+str(number)+"&include_card_data=true"
    else:
        result['data']=""
        result['success'] = 'False'
        result['error'] = 'Invalid Category'
        return result
    try:
        heads={
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36",
        }
        resp=requests.get(url,timeout=5,headers=heads)
    except exceptions.ReadTimeout:
        result['data']=""
        result['success'] = 'False'
        result['error'] = 'Time out'
        return result 
    if resp.status_code!=200:
        result['data']=""
        result['success'] = 'False'
        result['error'] = "No valid response from inshorts."
        return result
    newsitems=[]
    for item in resp.json()['data']['news_list']:
        newsitem={}
        newsitem['id']=item['news_obj']['hash_id']
        try:
            newsitem['tags']=[x for x in item['news_obj']['catgory_names']]
        except:
            pass
        newsitem['image']=item['news_obj']['image_url']
        newsitem['title']=item['news_obj']['title']
        newsitem['short']=item['news_obj']['content']
        newsitem['timestamp']=item['news_obj']['created_at']
        newsitem['author']=item['news_obj']['author_name']
        newsitem['source']=item['news_obj']['source_url']
        newsitems.append(newsitem)
    result['data'] = newsitems
    return result

def fetchFromCategroy(category,pageNumber,lang='en'):
    result={}
    categories=['india','business','politics','sports','technology','startups','entertainment','hatke','international','automobile','science','travel','miscellaneous','fashion']
    result['category']=category
    if category in categories:
        url="https://inshorts.com/api/"+lang+"/search/trending_topics/"+category+"?page="+str(pageNumber)+"&type=CUSTOM_CATEGORY"
    else:
        result['data']=""
        result['success'] = 'False'
        result['error'] = 'Invalid Category'
        return result
    try:
        heads={
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36",
        }
        resp=requests.get(url,timeout=5,headers=heads)
    except exceptions.ReadTimeout:
        result['data']=""
        result['success'] = 'False'
        result['error'] = 'Time out'
        return result 
    if resp.status_code!=200:
        result['data']=""
        result['success'] = 'False'
        result['error'] = "No valid response from inshorts."
        return result
    newsitems=[]
    for item in resp.json()['data']['news_list']:
        newsitem={}
        newsitem['id']=item['news_obj']['hash_id']
        try:
            newsitem['tags']=[x for x in item['news_obj']['catgory_names']]
        except:
            pass
        newsitem['image']=item['news_obj']['image_url']
        newsitem['title']=item['news_obj']['title']
        newsitem['short']=item['news_obj']['content']
        newsitem['timestamp']=item['news_obj']['created_at']
        newsitem['author']=item['news_obj']['author_name']
        newsitem['source']=item['news_obj']['source_url']
        newsitems.append(newsitem)
    result['total_page'] = resp.json()['data']['total_page']
    result['data'] = newsitems
    return result
