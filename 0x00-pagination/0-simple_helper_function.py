#!/usr/bin/env python3
"""
index_range that takes two interger args,page 
and size
"""
from typing import tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    page numbers are one indexed first page is page one
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
