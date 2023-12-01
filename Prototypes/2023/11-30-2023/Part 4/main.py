import cv2
import numpy as np

# Set video properties
width, height = 1920, 1080
fps = 30
seconds = 10
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 format

# Create a VideoWriter object
video_writer = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# Create a loop to generate frames and write to the video file
for frame_count in range(fps * seconds):
    # Create a simple gradient for demonstration purposes
    frame = np.ones((height, width, 3), dtype=np.uint8) * (frame_count % 256)

    # Write the frame to the video file
    video_writer.write(frame)

# Release the VideoWriter object
video_writer.release()

print("Video created successfully.")
