# Copyright(C) 2023 InfiniFlow, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC, abstractmethod
import typing as tp
from typing import Literal, Optional, Type, Union
class Table(ABC):

    @abstractmethod
    def create_index(self, index_name: str, column_names: list[str], method_type: str, index_para_list: list[dict],
                     options=None):
        pass

    @abstractmethod
    def drop_index(self, index_name: str):
        pass

    @abstractmethod
    def insert(self, data: list[dict[str, tp.Union[str, int, float]]]):
        pass

    @abstractmethod
    def import_data(self, file_path: str, options=None):
        pass

    @abstractmethod
    def delete(self, condition):
        pass

    @abstractmethod
    def update(self, condition, data):
        pass

    from infinity.query import Query, InfinityQueryBuilder
    @abstractmethod
    def search(
            self,
            query: Optional[Union[str]] = None,
    ) -> InfinityQueryBuilder:
        raise NotImplementedError

    @abstractmethod
    def _execute_query(self, query: Query) -> list[dict]:
        pass