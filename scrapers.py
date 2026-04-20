import requests
import feedparser
from bs4 import BeautifulSoup
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def clean_summary(text):
    if not text: return ""
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text(separator=' ', strip=True)
    if len(clean_text) > 150:
        match = re.split(r'([。！？])', clean_text)
        short_text = ""
        for i in range(0, len(match)-1, 2):
            short_text += match[i] + match[i+1]
            if len(short_text) >= 80: break
        return short_text.strip() if short_text else clean_text[:150] + "..."
    return clean_text

def scrape_yahoo():
    results = []
    try:
        feed = feedparser.parse('https://tw.news.yahoo.com/rss/stock')
        for entry in feed.entries[:30]:
            results.append({'source': 'Yahoo股市', 'title': entry.title, 'summary': entry.get('summary', ''), 'link': entry.get('link', '')})
    except: pass
    return results

def scrape_cnyes():
    results = []
    try:
        url = 'https://api.cnyes.com/media/api/v1/newslist/category/tw_stock?limit=30'
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()
        for item in data.get('items', {}).get('data', []):
            news_id = item.get('newsId', '')
            results.append({
                'source': '鉅亨網',
                'title': item.get('title', ''),
                'summary': item.get('summary', ''),
                'link': f"https://news.cnyes.com/news/id/{news_id}" if news_id else ""
            })
    except: pass
    return results

def scrape_udn():
    results = []
    try:
        feed = feedparser.parse('https://money.udn.com/rssfeed/news/1001/5590/5607?ch=money')
        for entry in feed.entries[:20]:
            results.append({'source': '經濟日報', 'title': entry.title, 'summary': entry.get('summary', ''), 'link': entry.get('link', '')})
    except: pass
    return results

def scrape_moneydj():
    results = []
    try:
        url = 'https://www.moneydj.com/KMDJ/news/newsreallist.aspx?a=mb010000'
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        rows = soup.select('table.forumgrid tr')
        for row in rows:
            a_tag = row.select_one('td a')
            if a_tag:
                title = a_tag.get_text(strip=True)
                link = a_tag.get('href', '')
                if link and not link.startswith('http'): link = 'https://www.moneydj.com' + link
                if title: results.append({'source': 'MoneyDJ', 'title': title, 'summary': '', 'link': link})
    except: pass
    return results[:20]

def scrape_wantgoo():
    results = []
    try:
        url = 'https://www.wantgoo.com/news/category/stock/taiwan'
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.select('h3')
        for item in items:
            title = item.get_text(strip=True)
            a_tag = item.find_parent('a')
            link = a_tag.get('href', '') if a_tag else ""
            if link and not link.startswith('http'): link = 'https://www.wantgoo.com' + link
            if title and len(title)>5: results.append({'source': '玩股網', 'title': title, 'summary': '', 'link': link})
    except: pass
    return results[:20]

def get_all_news():
    news = []
    news.extend(scrape_yahoo())
    news.extend(scrape_cnyes())
    news.extend(scrape_udn())
    news.extend(scrape_moneydj()) 
    news.extend(scrape_wantgoo())
    for n in news: n['summary'] = clean_summary(n.get('summary', ''))
    return news
