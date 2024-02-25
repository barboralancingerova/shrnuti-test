from rapper2 import *
from unittest.mock import Mock

def test_scitani() -> None: 
    mock = Mock()
    k = Wrapper2Kalkulator(mock)
    mock.plus.return_value = 10
    k.plus(4,6)
    mock.plus.return_value = 3
    k.plus(1,2)
    mock.multi.return_value = 25
    k.multi(5,5)

    mock.plus.return_value = 10
    assert k.memory() == ["plus 4 6 10", "plus 1 1 3", "multi 5 5 25"] # první výpočet projde, druhý ne



