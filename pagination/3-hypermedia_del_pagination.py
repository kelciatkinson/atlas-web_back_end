#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """Returns a dictionary containing hypermedia pagination information.
        """
        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        assert len(indexed_dataset) > 0

        if index is None:
            index = 0

        assert 0 <= index < len(self.dataset())

        if index >= total_items:
            return {}

        data = []
        current_index = index
        count = 0

        if current_index in indexed_dataset:
            data.append(indexed_dataset[current_index])
            count += 1
        current_index += 1

        if current_index < len(self.dataset()):
            next_index = current_index
        else:
            None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
