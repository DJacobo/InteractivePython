# cd "C:\Users\Daniel\Documents\Python Scripts\InteractivePython"
# pytest test_IP_Ch1_13_LogicGateConnector.py

import unittest, builtins

from IP_Ch1_13_LogicGate import *
from IP_Ch1_13_Connector import *
from unittest.mock import patch

class logicGateTest(unittest.TestCase):
    def setUp(self):
        self.testTrue = 1
        self.testFalse = 0
    
    
    def test_OrGate_true(self):
        orGate = OrGate('orTrue')
        user_input = [
            1,
            1
        ]

        # with patch('builtins.input', side_effect=user_input):
        with patch('builtins.input', lambda: user_input):
            self.assertTrue(orGate.getOutput)
