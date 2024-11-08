import requests
from tqdm import tqdm
import json

url = 'https://bff-service.rtbf.be/oaos/v1.5/pages/en-continu?_page={}&_limit=100'

articles_all_data = []
article_info_list = []
baselinks = []
titles_themes = {}

def create_all_links():
    for i in range(1, 151):
        baselinks.append(url.format(i))
    return baselinks

def get_all_data(create_all_links):
    for link in tqdm(create_all_links):
        response = requests.get(link)
        data = response.json()
        articles = data.get('data', {}).get('articles', [])
        articles_all_data.extend(articles)
    return articles_all_data

def get_article_info(articles_all_data):
    for article in articles_all_data:
        article_info = {
            "id": article.get("id"),
            "slug": article.get("slug"),
            "title": article.get("title"),
            "Theme": article.get("dossierLabel"),
            "Summary": article.get("summary"),
            "ReadingTime": article.get("readingTime"),
            "Link" : 'https://www.rtbf.be/article/{}'.format((article.get("slug") + '-' + str(article.get("id"))))}
        article_info_list.append(article_info)
    return article_info_list

def get_titles_themes(article_all_data):
    for article in article_all_data:
        titles_themes[article.get('title')] = article.get('dossierLabel')
    return titles_themes

def replace_accented_characters(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    
    for article in data:
        
        if 'title' in article:
            article['title'] = article['title'].replace('\u00e9', 'e').replace('\u00e8', 'e')
        
        
        if 'Theme' in article:
            article['Theme'] = article['Theme'].replace('\u00e9', 'e').replace('\u00e8', 'e')

    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    create_all_links()
    get_all_data(baselinks)
    get_article_info(articles_all_data)
    get_titles_themes(articles_all_data)
    with open('articles_info.json', 'w') as f:
        json.dump(article_info_list, f, indent=4)
    with open('titles_themes.json', 'w') as f:
        json.dump(titles_themes, f, indent=4)
    replace_accented_characters('articles_info.json')

if __name__ == '__main__':
    main()