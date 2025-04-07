from bs4 import BeautifulSoup
import requests

class MusicService:
    def __init__(self):
        self.url = "https://www.melon.com/chart/index.htm"
        self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://www.melon.com/"
}

    def get_melon_chart(self):
        soup = BeautifulSoup(requests.get(self.url, headers=self.headers).text, "html.parser")
        title_tags = soup.select("div.ellipsis.rank01 > span > a")
        artist_tags = soup.select("div.ellipsis.rank02 > a")

        result = []
        for rank, (title_tag, artist_tag) in enumerate(zip(title_tags, artist_tags), start=1):
            result.append({
                "rank": rank,
                "title": title_tag.text.strip(),
                "artist": artist_tag.text.strip()
            })
        return result
    

        #list = soup.find_all("div", class_="ellipsis rank01")
        #for item in list:
        #    print(item.text)
        #return soup




