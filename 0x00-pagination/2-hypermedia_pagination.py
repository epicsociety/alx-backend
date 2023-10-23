#!/usr/bin/env python3
""" Gets data for provided page and page_size """


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a list give the page and page size
        parameters:
        page: int
        page_size: int
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        self.data_size = len(self.dataset())
        if start >= self.data_size or end > self.data_size:
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dict with data, pages size ,previous and next page
        and total pages
        parameters:
        page: int
        page_size: int
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil((self.data_size / page_size))
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> tuple:
    """
    Return the start and end index of a page
    parameters:
    page:
    page_size:
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
