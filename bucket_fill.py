""" Coursework 1: Bucket Fill
"""

def load_image(filename):
    """ Load image from file made of 0 (unfilled pixels) and 1 (boundary pixels) and 2 (filled pixel)

    Example of content of filename:

0 0 0 0 1 1 0 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 1 0 0 1 0 1 1 0
1 1 0 0 1 0 1 0 1 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 1 0 1 0 0 1 0 1 1
0 1 1 0 1 1 0 1 1 0
0 0 1 1 0 0 1 1 0 0
0 0 0 0 1 1 0 0 0 0

    Args:
        filename (str) : path to file containing the image representation

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel
               2 represents a filled pixel
    """

    image = []
    with open(filename) as imagefile:
        for line in imagefile:
            if line.strip():
                row = list(map(int, line.strip().split()))
                image.append(row)
    return image


def stringify_image(image):
    """ Convert image representation into a human-friendly string representation

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)

    Returns:
        str : a human-friendly string representation of the image
    """
    
    if image is None:
        return ""

    # The variable "mapping" defines how to display each type of pixel.
    mapping = {
        0: " ",
        1: "*",
        2: "0"
    }

    image_str = ""
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n"
    for row in image:
        image_str += "| "
        for pixel in row:
            image_str += mapping.get(pixel, "?") + " "
        image_str += "|"
        image_str += "\n"
    if image:
        image_str += "+ " + "- " * len(image[0]) + "+\n" 
        
    return image_str


def show_image(image):
    """ Show image in terminal

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
    """
    print(stringify_image(image))


def fill(image, seed_point):
    """ Fill the image from seed point to boundary

    the image should remain unchanged if:
    - the seed_point has a non-integer coordinate
    - the seed_point is on a boundary pixel
    - the seed_point is outside of the image

    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) : a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel, and
               2 represents a filled pixel
    """

    check_conditions(image, seed_point)

    left_to_check = []
    left_to_check = check_neighbours(image, list(seed_point), left_to_check)

    while len(left_to_check) > 0:
        for empty_pixel in left_to_check:
            check_neighbours(image, empty_pixel, left_to_check)

    return image


def check_neighbours(image, seed_pixel, left_to_check):
    """ Colours the pixel and looks for other pixels to colour next and later check their neighbours

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
        seed_pixel (list) : 2-element list representing the (row, col) coordinates of the seed point to start filling
        left_to_check (list) : list of coordinates left to colour and check the neighbours for

    Returns:
        list : coordinates left to colour and check neighbours for, now updated
    """
   
    neighbours = gather_neighbours(image, seed_pixel) #List of neighbours
    colour_blank_pixel(image, seed_pixel) #Colour the pixel    

    if seed_pixel in left_to_check:
        left_to_check.remove(seed_pixel)

    for neighbour in neighbours:
        if check_if_outofbonds(image, neighbour) and check_if_coloured(image, neighbour) and neighbour not in left_to_check:
            left_to_check.append(neighbour)

    return left_to_check
    

def gather_neighbours(image, seed_pixel):
    """ Gathers the coordinates of the neighbouring pixels for a given pixel
    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
        seed_pixel (list) : 2-element list representing the (row, col) coordinates of the seed point to start filling

    Returns:
        list : coordinates of neighbouring pixels for the given seed_pixel
    """

    left = [seed_pixel[0] - 1, seed_pixel[1]]
    right = [seed_pixel[0] + 1, seed_pixel[1]]
    up = [seed_pixel[0], seed_pixel[1] - 1]
    down = [seed_pixel[0], seed_pixel[1] + 1]

    neighbours = [left, right, up, down]

    return neighbours

def check_conditions(image, seed_pixel):
    """ Verifies that the coordinates of the seed point are:
            - integers
            - not borders
            - within the image size
            - seed point not a coloured pixel

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
        seed_pixel (list) : 2-element list representing the (row, col) coordinates of the seed point to start filling
    """

    if type(seed_pixel[0]) != int or type(seed_pixel[1]) != int or type(seed_pixel) != tuple:
        raise ValueError("Coordinates must be integers not {type(seed_pixel[0])}")
    elif 0 == seed_pixel[0] or seed_pixel[0] == len(image[0]) - 1 or 0 == seed_pixel[1] or seed_pixel[0] == len(image) - 1:
        raise ValueError("Seed point should not be on a boundary pixel")
    elif not (check_if_outofbonds(image, seed_pixel)):
        raise ValueError("Seed point is outside of the image")
    elif check_if_coloured(image, seed_pixel) == False:
        raise ValueError("Seed point given is a coloured pixel: ", seed_pixel)
	
    return

def check_if_outofbonds(image, seed_pixel):
    """ Verifies that the seed pixel is inside the image
    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
        seed_pixel (list) : 2-element list representing the (row, col) coordinates of the seed point to start filling

    Returns:
        bool 
    """

    return 0 <= seed_pixel[0] <= len(image[0]) - 1 and 0 <= seed_pixel[1] <= len(image) - 1

def check_if_coloured(image, seed_pixel):
    """ Verifies that the seed pixel is inside the image
    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
        pixel (list) : 2-element list representing the (row, col) coordinates of the seed point to start filling

    Returns:
        bool 
    """

    return image[seed_pixel[0]][seed_pixel[1]] == 0

def colour_blank_pixel(image, pixel):
    """ Verifies that the seed pixel is inside the image
    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
        pixel (list) : 2-element list representing the (row, col) coordinates of the seed point to start filling

    Returns:
        list: list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel), with the pixel desired now filled
    """

    assert check_if_coloured(image, pixel), f"Attempted to colour a black pixel located at {pixel}"
    image[pixel[0]][pixel[1]] = 2
    
    return image

def example_fill():
    image = load_image("data/snake.txt")

    print("Before filling:")
    show_image(image)

    image = fill(image=image, seed_point=(10, 1))

    print("-" * 25)
    print("After filling:")
    show_image(image)

if __name__ == '__main__':
    example_fill()

