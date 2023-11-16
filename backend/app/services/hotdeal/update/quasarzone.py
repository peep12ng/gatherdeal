from bs4 import BeautifulSoup
import re

from .base import HotdealUpdaterBase

from ....data import Source
from ....utils.class_from_args import class_from_args
from ....entity import Hotdeal

class QuasarzoneUpdater(HotdealUpdaterBase):

    _source = Source.quasarzone
    _categories = ["PC/하드웨어", "노트북/모바일", "가전/TV"]

    async def _get_hotdeal_urls(self):

        hotdeal_urls = []
        
        board_urls = [f"https://quasarzone.com/bbs/qb_saleinfo?page=1&category={category}" for category in self._categories]

        boards = await self._client.get_many(board_urls)

        for board in boards:
            bs = BeautifulSoup(board, "html.parser")
            heads = bs.find("tbody").find_all("tr")

            for head in heads:
                code = re.search('views/(.+?)?category', head.select_one("a.subject-link").attrs["href"]).group(1)[:-1]
                hotdeal_urls.append(f"https://quasarzone.com/bbs/qb_saleinfo/views/{code}")
        
        return hotdeal_urls
    
    async def _get_hotdeal_from_url(self, url):

        r = await self._client.get(url)
        bs = BeautifulSoup(r, "html.parser")

        d = {}

        d["code"] = url.split("views/")[-1]
        d["id"] = self._create_hotdeal_id(d["code"])
        d["source_link"] = url

        if "블라인드 처리된 글입니다" in str(bs):
            return None
        else:
            d["is_blind"] = False

            d["title"] = bs.find("title").text.split(" >")[0]

            info_table = bs.select_one("table.market-info-view-table")
            info_trs = info_table.find_all("tr")

            d["original_price"] = float(re.sub(r'[^0-9.]', '', info_trs[2].find("span").text))
            d["price_to_krw"] = 0
            d["currency_type"] = info_trs[2].find("span").text.split("(")[1][:3]
            d["store_link"] = info_trs[0].find("a").text

            if "종료" in bs.select_one("h1.title").text:
                d["is_done"] = True
            else:
                d["is_done"] = False

        return class_from_args(Hotdeal, d)