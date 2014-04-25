# author: Somsubhra Bairi (201101056)

# Draws an image of chessboard and saves it
# Image is saved in out.jpg

# Python imports
from PIL import Image
import webbrowser


# The main function
def main():
    # Create a new image of size 800x800
    img = Image.new('RGB', (800, 800), "black")

    # Load the pixels
    pixels = img.load()

    # The output filename
    filename = "out.jpg"

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

    # Open the image in image browser
    webbrowser.open(filename)

# Run the main function
if __name__ == '__main__':
    main()