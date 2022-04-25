# Copyright 2020-present, Mayo Clinic Department of Neurology
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import os
import numpy as np

from copy import deepcopy
from shutil import rmtree

import unittest
from unittest import TestCase

from best.signal import *

basedir = os.path.abspath(os.path.dirname(__file__))

class TestSignal(TestCase):
    def test_import(self):
        print("Testing import 'from best.signal'")


if __name__ == '__main__':
    unittest.main()
