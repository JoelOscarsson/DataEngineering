from print_joke import get_random_reaction


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert isinstance(reaction, str)


def test_get_random_reaction_repeats():
    # Write a test that checks that multiple calls to get_random_reaction()
    # doesn't give you the same reaction every time
    pass 


# Come up with a test of your own and implement it here.