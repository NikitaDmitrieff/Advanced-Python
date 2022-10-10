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

    # TODO: Complete this function
    return []


def example_fill():
    image = load_image("data/bar.txt")

    print("Before filling:")
    show_image(image)

    image = fill(image=image, seed_point=(7, 3))

    print("-" * 25)
    print("After filling:")
    show_image(image)


if __name__ == '__main__':
    example_fill()

