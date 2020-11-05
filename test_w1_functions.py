from processors.priority_queue import priority_queue
from processors.w1_functions import *


def test_enqueue():
    result = enqueue(priority_queue, ('Roberto', 2))
    expected = {'no_urgency': [], 'low_urgency': ['Roberto'],
                'urgency': [], 'high_urgency': [], 'emergency': []}

    assert expected == result
