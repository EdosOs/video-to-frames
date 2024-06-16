import cv2
import os


def extract_frames(video_path, output_folder):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video from the specified path
    video_capture = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not video_capture.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total number of frames: {frame_count}")

    frame_index = 0
    while True:
        # Read the next frame
        ret, frame = video_capture.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            break

        # Save the frame as a JPEG file
        frame_filename = os.path.join(output_folder, f"frame_{frame_index:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        print(f"Saved {frame_filename}")

        frame_index += 1

    # Release the video capture object
    video_capture.release()
    print("Done extracting frames.")

# VID-20240611-WA0001
# Usage example
# path1 = r'C:\Users\gilim\Documents\studies\MATLAB\Semester7\VAN\final_proj\EfficientPose-main\test_data\duck_tests'
# for diritem in os.listdir(path1):
#     vid_path = os.listdir(os.path.join(path1,diritem))
#     if len(vid_path) != 0:
#         vidname = os.listdir(vid_path[0])
        # video_path = os.path.join(path1,diritem,vid_path[0])
        # output_folder = os.path.join(path1,diritem)
video_path = r'C:\Users\gilim\Documents\studies\MATLAB\Semester7\VAN\final_proj\EfficientPose-main\test_data\cup\Can_test_controlled\can_vid.mp4'
output_folder = r'C:\Users\gilim\Documents\studies\MATLAB\Semester7\VAN\final_proj\EfficientPose-main\test_data\cup\Can_test_controlled'
extract_frames(video_path, output_folder)