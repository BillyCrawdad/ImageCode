from PIL import Image, ImageDraw
def create_png():
    # Create a new image with a white background
    image = Image.new("RGBA", (500, 500), (255, 255, 255, 0))

    # Get a drawing context
    draw = ImageDraw.Draw(image)

    # Draw a white rectangle to cover the entire image
    draw.rectangle([(0, 0), (500, 500)], fill=(255, 255, 255, 255))

    # Draw a transparent rectangle (hole) in the middle
    draw.rectangle([(50, 50), (450, 450)], fill=(0, 0, 0, 0))

    # Save the image as a PNG file
    image.save("output.png")

if __name__ == "__main__":
    create_png()
