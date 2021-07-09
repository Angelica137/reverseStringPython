from scripts.reverseString import reverse


def test_reverse_returns_reversed_string():
    assert reverse("123") == "321"


def test_reverse_returns_reversed_string_superlong():
    assert reverse("super duper long") == "gnol repud repus"
