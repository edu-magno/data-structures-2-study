from processors.priority_queue import priority_queue
from processors.w1_functions import *


def test_enqueue():
    result = enqueue(priority_queue, ('Roberto', 3))
    expected = {'no_urgency': [], 'low_urgency': [],
                'urgency': ['Roberto'], 'high_urgency': [], 'emergency': ['Ana', 'Carlos']}

    assert expected == result


def test_dequeue():
    result = dequeue(priority_queue)
    expected = ({'no_urgency': [], 'low_urgency': [], 'urgency': [
                'Roberto'], 'high_urgency': [], 'emergency': ['Carlos']}, 'Ana')

    assert expected == result
