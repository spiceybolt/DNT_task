import cv2

input_video_path = 'input.mp4'  # Replace with the path to your input video
cap = cv2.VideoCapture(input_video_path)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

output_video_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

frame_list = []
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame_list.append(frame)

cap.release()

reversed_frame_list = frame_list[::-1]

target_fps = 15
frame_interval = int(fps / target_fps)

for frame in reversed_frame_list:
    out.write(frame)
    for _ in range(frame_interval - 1):
        out.write(frame)  

out.release()

