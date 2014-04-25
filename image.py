# author: Somsubhra Bairi (201101056)

# Draws an image of chessboard and saves it
# Also applies an emboss filter to it and saves it
# Images are saved in out.jpg and out1.jpg

# Python imports
from PIL import Image
from PIL import ImageFilter
import webbrowser


# The main function
def main():
    # Create a new image of size 800x800
    img = Image.new('RGB', (800, 800), "black")

    # Load the pixels
    pixels = img.load()

    # The output filename
    filename = "out.jpg"

    # The second output image filename
    filename1 = "out1.jpg"

    # Iterate through rows of image
    for i in range(img.size[0]):
        row = int(i / 100)

        # Iterate through the columns of image
        for j in range(img.size[1]):
            col = int(j / 100)

            # Draw the pixel white based on its location to create a chessboard
            if col % 2 == 0 and row % 2 == 0 or col % 2 != 0 and row % 2 != 0:
                pixels[i, j] = (255, 255, 255)

    # Save the image
    img.save(filename)

    # Apply emboss filter
    img1 = img.filter(ImageFilter.EMBOSS)

    # Save the embossed image
    img1.save(filename1)

    # Open embossed image in image browser
    webbrowser.open(filename1)

    # Open the image in image browser
    webbrowser.open(filename)

# Run the main function
if __name__ == '__main__':
    main()