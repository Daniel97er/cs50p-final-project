from project import (inclusion_exclusion_procedure, permutation_with_repetition,
                     variation_with_repetition, variation_without_repetition)


def main():
    # Main function

    # Check inclusion_exclusion_procedure()
    test_inclusion_exclusion_procedure()
    test_inclusion_exclusion_procedure2()

    # Check permutation_with_repetition()
    test_permutation_with_repetition()
    test_permutation_with_repetition2()

    # Check variation_with_repetition()
    test_variation_with_repetition()
    test_variation_with_repetition2()

    # Check variation_without_repetition()
    test_variation_without_repetition()
    test_variation_without_repetition2()



def test_inclusion_exclusion_procedure(monkeypatch):
    # Check inclusion_exclusion_procedure()

    # Simulate user inputs
    inputs = iter(["1", "1,2,3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = inclusion_exclusion_procedure()
    # Get results
    assert result[0] == {'1', '2', '3'}
    assert result[1] == 3


def test_inclusion_exclusion_procedure2(monkeypatch):
    # Check inclusion_exclusion_procedure()

    # Simulate user inputs
    inputs = iter(["3", "1,2,3", "2,A,4", "A,1,7"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = inclusion_exclusion_procedure()
    # Get results
    assert result[0] == {'1', '2', '3', '4', '7', 'A'}
    assert result[1] == 6


def test_permutation_with_repetition(monkeypatch):
    # Check permutation_with_repetition()

    # Simulate user inputs
    inputs = iter(["1,2,3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = permutation_with_repetition()
    # Get results
    assert result[0] == [['1', '2', '3'], ['1', '3', '2'], ['2', '1', '3'],
                         ['2', '3', '1'], ['3', '1', '2'], ['3', '2', '1']]
    assert result[1] == 6


def test_permutation_with_repetition2(monkeypatch):
    # Check permutation_with_repetition()

    # Simulate user inputs
    inputs = iter(["A,3,?,S"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = permutation_with_repetition()
    # Get results
    assert result[0] == [['A', '3', '?', 'S'], ['A', '3', 'S', '?'], ['A', '?', '3', 'S'],
                         ['A', '?', 'S', '3'], ['A', 'S', '3', '?'], ['A', 'S', '?', '3'],
                         ['3', 'A', '?', 'S'], ['3', 'A', 'S', '?'], ['3', '?', 'A', 'S'],
                         ['3', '?', 'S', 'A'], ['3', 'S', 'A', '?'], ['3', 'S', '?', 'A'],
                         ['?', 'A', '3', 'S'], ['?', 'A', 'S', '3'], ['?', '3', 'A', 'S'],
                         ['?', '3', 'S', 'A'], ['?', 'S', 'A', '3'], ['?', 'S', '3', 'A'],
                         ['S', 'A', '3', '?'], ['S', 'A', '?', '3'], ['S', '3', 'A', '?'],
                         ['S', '3', '?', 'A'], ['S', '?', 'A', '3'], ['S', '?', '3', 'A']]
    assert result[1] == 24


def test_variation_with_repetition(monkeypatch):
    # Check variation_with_repetition

    # Simulate user inputs
    inputs = iter(["1,A,A", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = variation_with_repetition()
    # Get results
    assert result[0] == [['1', 'A'], ['A', '1'], ['A', 'A']]
    assert result[1] == 3


def test_variation_with_repetition2(monkeypatch):
    # Check variation_with_repetition

    # Simulate user inputs
    inputs = iter(["1,2,3", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = variation_with_repetition()
    # Get results
    assert result[0] == [['1'], ['2'], ['3']]
    assert result[1] == 3


def test_variation_without_repetition(monkeypatch):
    # Check variation_without_repetition

    # Simulate user inputs
    inputs = iter(["1,2,A", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = variation_without_repetition()
    # Get results
    assert result[0] == [['A', 'A', 'A'], ['A', 'A', '2'], ['A', 'A', '1'], ['A', '2', 'A'],
                         ['A', '2', '2'], ['A', '2', '1'], ['A', '1', 'A'], ['A', '1', '2'],
                         ['A', '1', '1'], ['2', 'A', 'A'], ['2', 'A', '2'], ['2', 'A', '1'],
                         ['2', '2', 'A'], ['2', '2', '2'], ['2', '2', '1'], ['2', '1', 'A'],
                         ['2', '1', '2'], ['2', '1', '1'], ['1', 'A', 'A'], ['1', 'A', '2'],
                         ['1', 'A', '1'], ['1', '2', 'A'], ['1', '2', '2'], ['1', '2', '1'],
                         ['1', '1', 'A'], ['1', '1', '2'], ['1', '1', '1']]
    assert result[1] == 27


def test_variation_without_repetition2(monkeypatch):
    # Check variation_with_repetition

    # Simulate user inputs
    inputs = iter(["1,2,3", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    # Run function
    result = variation_without_repetition()
    # Get results
    assert result[0] == [['3'], ['2'], ['1']]
    assert result[1] == 3
