from abc import abstractmethod, abstractproperty
from typing import List

import asyncio

from .client import ClientObject

from ....repositories import HotdealRepository
from ....data import Source

class HotdealUpdaterBase:

    _client = ClientObject()

    @abstractproperty
    def _source(self) -> Source:
        raise NotImplementedError()
    
    @abstractproperty
    def _categories(self):
        raise NotImplementedError()

    async def update(self, repo: HotdealRepository):

        urls = await self._get_hotdeal_urls()
        hotdeals = asyncio.gather(*[self._get_hotdeal_from_url(url) for url in urls])

        for hotdeal in hotdeals:
            self._add_or_update(hotdeal, repo)

    async def _get_hotdeal_urls(self):
        pass
    
    async def _get_hotdeal_from_url(self, url):
        pass

    def _add_or_update(self, hotdeal, repo: HotdealRepository):
        _hotdeal = repo.new(**hotdeal.__dict__)

        if repo.exists(_hotdeal.id):
            repo.update(_hotdeal, ["is_blind", "is_done"])
        else:
            print("add")
            repo.add(_hotdeal)
        
        print(f"update complete id{_hotdeal.id}")

    def _create_hotdeal_id(self, code:str) -> str:
        '''
        Source별 핫딜 id 생성 함수

        :param code (str): 핫딜 고유 code

        :return id (str): 핫딜 고유 id(헤더_코드)
        '''
        return self._source.hotdeal_id_header + f"_{code}"