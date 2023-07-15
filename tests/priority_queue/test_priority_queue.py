from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue({"qtd_linhas": 7})
    priority_queue.enqueue({"qtd_linhas": 6})
    priority_queue.enqueue({"qtd_linhas": 3})
    priority_queue.enqueue({"qtd_linhas": 2})
    assert priority_queue.dequeue() == {"qtd_linhas": 3}
    assert priority_queue.search(0) == {"qtd_linhas": 2}
    assert priority_queue.search(1) == {"qtd_linhas": 7}
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(4)
