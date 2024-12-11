# AI Object Counter

This project uses YOLOv8x for real-time object detection and counting. It can process live camera feed, saved images, and videos.

## Requirements

- Python 3.6+
- OpenCV
- Ultralytics YOLO

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aayush-ojha/ai-object-counter.git
    cd ai-object-counter
    ```

2. Install the required libraries:
    ```bash
    pip install opencv-python ultralytics
    ```

3. Download the YOLOv8x model:
    - Visit the [Ultralytics YOLOv8 GitHub repository](https://github.com/ultralytics/ultralytics).
    - Download the `yolov8x.pt` model file and place it in the project directory.

## Usage

### Live Camera Feed

To process live camera feed, uncomment the `process_camera()` line in `main.py`:

```python
if __name__ == "__main__":
    process_camera()
    # process_image('path_to_your_image.jpg')
    # process_video('path_to_your_video.mp4')
```

Run the script:

```bash
python3 main.py
```

### Saved Images

To process a saved image, uncomment the `process_image('path_to_your_image.jpg')` line in `main.py` and provide the path to your image:

```python
if __name__ == "__main__":
    # process_camera()
    process_image('image.jpeg')
    # process_video('path_to_your_video.mp4')
```

Run the script:

```bash
python3 main.py
```

### Saved Videos

To process a saved video, uncomment the `process_video('path_to_your_video.mp4')` line in `main.py` and provide the path to your video:

```python
if __name__ == "__main__":
    # process_camera()
    # process_image('path_to_your_image.jpg')
    process_video('path_to_your_video.mp4')
```

Run the script:

```bash
python3 main.py
```

## How It Works

The script uses the YOLOv8x model to detect objects in the input frames. It draws bounding boxes around detected objects and displays a legend showing the count of each detected object class.

## License

This project is licensed under the MIT License.

