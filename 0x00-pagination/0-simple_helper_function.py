#!/usr/bin/env python3
""" Provides the start and end index """


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
