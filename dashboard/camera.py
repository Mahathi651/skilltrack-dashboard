import cv2
import threading
import numpy as np

current_filter = "normal"
filter_lock = threading.Lock()


def set_filter(filter_name):
    global current_filter
    with filter_lock:
        current_filter = filter_name


def apply_filter(frame, filter_name):
    if filter_name == "gray":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    elif filter_name == "blur":
        frame = cv2.GaussianBlur(frame, (21, 21), 0)

    elif filter_name == "sepia":
        kernel = np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ])
        frame = cv2.transform(frame, kernel)
        frame = np.clip(frame, 0, 255).astype(np.uint8)

    return frame


def generate_frames():
    camera = cv2.VideoCapture(0)

    try:
        while True:
            success, frame = camera.read()

            if not success:
                break

            with filter_lock:
                selected_filter = current_filter

            frame = apply_filter(frame, selected_filter)

            ret, buffer = cv2.imencode(".jpg", frame)

            if not ret:
                continue

            frame_bytes = buffer.tobytes()

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" +
                frame_bytes +
                b"\r\n"
            )

    finally:
        camera.release()