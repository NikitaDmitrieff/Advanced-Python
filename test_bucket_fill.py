from bucket_fill import fill
from bucket_fill import load_image
from bucket_fill import show_image

def test_pattern():
    """ 
    Main testing functions which initiates all four tests 
    present and prints messages.
    """

    print("\nTesting the fill function...\n")

    test_normal_functionning()
    test_incorrect_input_type()
    test_seed_pixel_already_black()

    print("\n...end of testing.\n")

    pass

def test_seed_pixel_already_black():
    """Tests the case where a pixel given is already coloured.
    The fill function should display a ValueError.
    """
    
    image = load_image("data/test_cases.txt")
    seed_point = (4, 21)

    try:
        fill(image, seed_point)
        print("test_seed_pixel_already_black ...... failed")
    except ValueError:
        print("test_seed_pixel_already_black ...... passed")

def test_incorrect_input_type():
    """Tests the case where a seed point given is given in an incorrect
    format.
        - Test 1 : as a tuple of string
        - Test 2 : as a tuple of float
        - Test 3 : as a list of int
    """

    image = load_image("data/test_cases.txt")
    seed_point = ("2", "3")

    try:
        fill(image, seed_point)
        print("test_incorrect_input_type str ...... failed")
    except ValueError:
        print("test_incorrect_input_type str ...... passed")

    image = load_image("data/test_cases.txt")
    seed_point = (2.0, 3.0)

    try:
        fill(image, seed_point)
        print("test_incorrect_input_type float .... failed")
    except ValueError:
        print("test_incorrect_input_type float .... passed")

    image = load_image("data/test_cases.txt")
    seed_point = [2, 3]

    try:
        fill(image, seed_point)
        print("test_incorrect_input_type list ..... failed")
    except ValueError:
        print("test_incorrect_input_type list ..... passed")

def test_normal_functionning():
    """ Tests the bucket_fill function by comparing to a test of known result

0 0 0 0 0 0
1 0 1 1 1 0
0 1 0 0 0 1
0 0 1 1 1 0
0 0 0 0 0 0

    Using three different seed_points to colour the three different areas
    of the above figure, the test_pattern() function checks for various cases.
    """

    image = load_image("data/test_cases.txt")

    seed_point_1 = (22, 13)
    seed_point_2 = (7, 15)
    seed_point_3 = (5, 2)

    expected_results = []

    expected_results.append(load_image("data/test_1.txt"))
    expected_results.append(load_image("data/test_2.txt"))
    expected_results.append(load_image("data/test_3.txt"))

    results = []

    results.append(fill(image, seed_point_1))

    image = load_image("data/test_cases.txt")
    results.append(fill(image, seed_point_2))

    image = load_image("data/test_cases.txt")
    results.append(fill(image, seed_point_3))

    if results == expected_results:
        print("test_normal_functionning ........... passed")

    else:
        print("test_normal_functionning ........... failed")


if __name__ == '__main__':
    test_pattern()
