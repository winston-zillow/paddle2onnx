#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import numpy as np
from op_test import OpTest


class TestLookupTableOp(OpTest):
    def setUp(self):
        self.op_type = "lookup_table"
        self.init_embedding()
        self.inputs = {'W': self.emb, 'Ids': np.array([1]).astype("int64")}
        self.outputs = {'Out': np.zeros((1, 4), dtype=np.float32)}

    def init_embedding(self):
        self.emb = np.array([
            [1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3],
            [4, 4, 4, 4]
        ], dtype=np.float32)

    def test_check_output(self):
        self.check_output()


class TestLookupTableRank2Op(TestLookupTableOp):
    def setUp(self):
        self.op_type = "lookup_table"
        self.init_embedding()
        self.inputs = {'W': self.emb, 'Ids': np.array([[1], [2]]).astype("int64")}
        self.outputs = {'Out': np.zeros((2, 4), dtype=np.float32)}

    def test_check_output(self):
        self.check_output()


if __name__ == '__main__':
    unittest.main()