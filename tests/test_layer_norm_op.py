# Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
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


class TestLayerNormOp(OpTest):
    def setUp(self):
        self.op_type = 'layer_norm'
        X = np.random.random((11, 5)).astype('float32')
        mean_var_shape = (X.shape[0],)
        self.inputs = {'X': X,
                       'Bias': np.full((5,), 0.5, dtype=np.float32),
                       'Scale': np.full((5,), 1.1, dtype=np.float32)
                       }
        self.outputs = {'Y': np.zeros_like(X),
                        'Mean': np.zeros(mean_var_shape, dtype=np.float32),
                        'Variance': np.zeros(mean_var_shape, dtype=np.float32)
                        }
        self.attrs = {'begin_norm_axis': 1, 'epsilon': np.array(0.001, dtype=np.float32)}

    def test_check_output(self):
        self.check_output()


class TestLayerNormRank3Op(OpTest):
    def setUp(self):
        self.op_type = 'layer_norm'
        X = np.random.random((11, 3, 5)).astype('float32')
        mean_var_shape = (X.shape[0] * X.shape[1],)
        self.inputs = {'X': X,
                       'Bias': np.full((5,), 0.5, dtype=np.float32),
                       'Scale': np.full((5,), 1.1, dtype=np.float32)
                       }
        self.outputs = {'Y': np.zeros_like(X),
                        'Mean': np.zeros(mean_var_shape, dtype=np.float32),
                        'Variance': np.zeros(mean_var_shape, dtype=np.float32)
                        }
        self.attrs = {'begin_norm_axis': 2, 'epsilon': np.array(0.001, dtype=np.float32)}

    def test_check_output(self):
        self.check_output()


if __name__ == '__main__':
    unittest.main()
