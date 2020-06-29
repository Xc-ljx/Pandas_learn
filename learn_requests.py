import requests
from bs4 import BeautifulSoup
import json

class Douban:
    def __init__(self):
        self.URL = "https://movie.douban.com/top250"
        self.starnum = []
        for start_num in range(0,251):
            self.starnum.append(start_num)
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    def get_top250(self):
        for start in self.starnum:
            start = str(start)
            html = requests.get(self.URL,headers=self.header,params={'start':start})
            soup = BeautifulSoup(html.text,'html.parser')
            name = soup.select('#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)')
            for name in name:
                print(name.get_text())
                #file_name = 'Top250.json'
            # with open(file_name,'w') as f_obj:
            #     for name in name:
            #         f_obj.dump(str(name.get_text()),f_obj)






if __name__ == "__main__":
    cls = Douban()
    cls.get_top250()
