#!/usr/bin/env python3
"""
Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range from a given page and page size.
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)