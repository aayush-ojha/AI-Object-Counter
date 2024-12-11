import cv2
from ultralytics import YOLO


model = YOLO('yolov8x.pt')

def process_frame(frame):
 
    results = model(frame)[0]
    
    object_counts = {}
    

    for box in results.boxes.data:
        x1, y1, x2, y2, conf, cls = box
        class_name = results.names[int(cls)]
        
 
        if class_name in object_counts:
            object_counts[class_name] += 1
        else:
            object_counts[class_name] = 1
            
  
        label = f'{class_name} {conf:.2f}'
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(x1), int(y1) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)  
    

    y_offset = 30
    cv2.putText(frame, "Object Counts:", (10, y_offset), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)  
    
    for class_name, count in object_counts.items():
        y_offset += 30
        cv2.putText(frame, f"{class_name}: {count}", (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)  
    
    return frame

def process_camera():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        frame = process_frame(frame)
        cv2.imshow('Object Counter', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def process_image(image_path):
    image = cv2.imread(image_path)
    image = process_frame(image)
    cv2.imshow('Object Counter', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = process_frame(frame)
        cv2.imshow('Object Counter', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # process_camera()
    process_image('image.jpeg')
    # process_video('path_to_your_video.mp4')