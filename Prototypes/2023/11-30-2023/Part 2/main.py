from PIL import Image, ImageDraw

def create_png():
    # Create a new image with a white background
    original_image = Image.open("20231129_073914.jpg")

    # Get a drawing context
    draw = ImageDraw.Draw(original_image)

    # Draw a white rectangle to cover the entire image
    draw.rectangle([(70, 160), (300, 200)], fill=(0, 0, 0))

    # Save the image as a PNG file
    original_image.save("output.png")

if __name__ == "__main__":
    create_png()
