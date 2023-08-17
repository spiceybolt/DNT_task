import cv2

input_video_path = 'input.mp4'
cap = cv2.VideoCapture(input_video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
output_video_path = 'outputrevslow.mp4'

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

slow = 2
frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

for frame in reversed(frames):
    out.write(frame)

cap.release()
out.release()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
input_video_path = output_video_path
cap = cv2.VideoCapture(input_video_path)
output_video_path = 'final.mp4'

out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
slow = 2
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    for _ in range(slow):
        out.write(frame)
cap.release()
out.release()