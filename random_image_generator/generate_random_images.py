import random
import os
from tqdm import tqdm
img_history = []


def generate_random_image(file_path):
    # Define image size and background color
    width, height = 800, 600
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    while (r, g, b) in img_history:
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        if (r, g, b) not in img_history:
            break
    img_history.append((r, g, b))
    background_color = (r, g, b)  # Red color in RGB format

    # Calculate the total number of pixels
    total_pixels = width * height

    # Calculate the size of the image data (each pixel has 3 bytes for RGB)
    image_data_size = total_pixels * 3

    # Define the BMP file header
    header = bytearray([
        66, 77,               # BM - Windows Bitmap identifier
        image_data_size & 255,  # Size of the file
        (image_data_size >> 8) & 255,
        (image_data_size >> 16) & 255,
        (image_data_size >> 24) & 255,
        0, 0, 0, 0,           # Reserved bytes
        54, 0, 0, 0,          # Offset to the image data
        40, 0, 0, 0,          # Size of the second header (40 bytes)
        width & 255,          # Image width
        (width >> 8) & 255,
        (width >> 16) & 255,
        (width >> 24) & 255,
        height & 255,         # Image height
        (height >> 8) & 255,
        (height >> 16) & 255,
        (height >> 24) & 255,
        1, 0,                 # Number of color planes (must be 1)
        24, 0,                # Number of bits per pixel (24 bits)
        0, 0, 0, 0,           # Compression method (0 for none)
        0, 0, 0, 0,           # Size of the image data (can be 0 for uncompressed)
        0, 0, 0, 0,           # Horizontal resolution (pixels per meter)
        0, 0, 0, 0,           # Vertical resolution (pixels per meter)
        0, 0, 0, 0,           # Number of colors in the palette (0 for 24-bit)
        0, 0, 0, 0,           # Number of important colors (0 means all)
    ])

    # Create the image data with the background color
    image_data = bytearray([background_color[2], background_color[1], background_color[0]] * total_pixels)

    # Combine the header and image data
    bmp_data = header + image_data

    # Save the BMP data to a file
    with open(file_name, "wb") as bmp_file:
        bmp_file.write(bmp_data)


if __name__ == "__main__":
    os.mkdir("generated_images")
    for i in tqdm(range(1, 501)):
        file_name = "image_" + str(i) + ".jpg"
        file_path = os.path.join("generated_images", file_name)
        generate_random_image(file_path)
