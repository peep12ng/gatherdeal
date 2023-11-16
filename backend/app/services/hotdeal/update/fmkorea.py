from bs4 import BeautifulSoup
import re

from .base import HotdealUpdaterBase

from ....entity import Hotdeal
from ....data import Source
from ....utils.class_from_args import class_from_args

class FmkoreaUpdater(HotdealUpdaterBase):

    _source = Source.fmkorea
    _categories = ["1254381811", "1196845148"] # ["PC제품", "가전제품"]

    async def _get_hotdeal_urls(self):

        hotdeal_urls = []

        board_urls = [f"https://www.fmkorea.com/index.php?mid=hotdeal&category={category}" for category in self._categories]

        boards = await self._client.get_many(board_urls)

        for board in boards:
            bs = BeautifulSoup(board, "html.parser")
            heads = bs.find("div", "fm_best_widget _bd_pc").find_all("div", "li")

            for head in heads:
                code = re.search("document_srl=(.+?)&listStyle", head.select_one("a").attrs["href"]).group(1)
                hotdeal_urls.append(f"https://www.fmkorea.com/{code}")
        
        return hotdeal_urls
    
    async def _get_hotdeal_from_url(self, url):
        
        r = await self._client.get(url)
        bs = BeautifulSoup(r, "html.parser")

        d = {}
        d["code"] = url.split("com/")[-1]
        d["id"] = self._create_hotdeal_id(d["code"])
        d["source_link"] = url

        info_table = bs.find("table", "hotdeal_table")
        info_trs = info_table.find_all("tr")

        price = info_trs[3].find("td").text

        d["title"] = info_trs[2].find("td").text
        d["original_price"] = float(re.sub(r'[^0-9.]', '', price))
        d["price_to_krw"] = 0
        d["currency_type"] = "KRW" if "원" in price or "," in price else "USD"
        d["store_link"] = info_trs[0].find("td").text

        if "종료된" in bs:
            d["is_done"] = True
        else:
            d["is_done"] = False
        
        d["is_blind"] = False

        return class_from_args(Hotdeal, d)