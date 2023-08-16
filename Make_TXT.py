import os
import json

# JSON 파일들이 있는 디렉토리 경로
json_dir = "c:\\Users\\admin\\Desktop\\wooil\\Hyper\\2D Bounding Box\\training\\labels"

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
        with open(json_file_path, "r",encoding='UTF8') as json_file:
            json_data = json.load(json_file)
        
        # YOLO 포맷으로 변환한 결과 저장할 리스트
        yolo_annotations = []
        
        # Annotation 정보를 YOLO 포맷으로 변환
        for annotation in json_data["Annotation"]:
            yolo_annotation = convert_to_yolo_format(annotation, json_data["Source_Image_Info"]["Resolution"])
            yolo_annotations.append(yolo_annotation)
        
        # YOLO 포맷으로 변환된 결과를 txt 파일로 저장
        output_file_name = os.path.splitext(json_file_name)[0] + ".txt"
        output_file_path = os.path.join(json_dir, output_file_name)
        with open(output_file_path, "w") as output_file:
            output_file.write("\n".join(yolo_annotations))
        
        print(f"{json_file_name}을 YOLO 포맷으로 변환하여 {output_file_name}에 저장했습니다.")