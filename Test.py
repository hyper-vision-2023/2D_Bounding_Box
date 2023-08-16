import os
import json

# JSON 파일들이 있는 디렉토리 경로
json_dir = "c:\\Users\\admin\\Desktop\\wooil\\Hyper\\2D Bounding Box\\test\labels"

# YOLO 포맷으로 변환하는 함수
def convert_to_yolo_format(annotation, image_resolution):
    label = annotation["Label"]
    x_center = annotation["Coordinate"][0] / image_resolution[0]
    y_center = annotation["Coordinate"][1] / image_resolution[1]
    width = annotation["Coordinate"][2] / image_resolution[0]
    height = annotation["Coordinate"][3] / image_resolution[1]
    return f"{label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"

# JSON 파일들을 처리
for json_file_name in os.listdir(json_dir):
    if json_file_name.endswith(".json"):
        json_file_path = os.path.join(json_dir, json_file_name)
        
        # JSON 파일 불러오기
        with open(json_file_path, "r", encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            print(json_data)