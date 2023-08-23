import os
import json
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torch.utils.data import DataLoader
from torchvision.transforms import functional as F
from torchvision.io import read_image
from torchvision.transforms import functional as F
from torchvision.transforms import functional_pil as FP
import torch

# JSON 파일들이 있는 디렉토리 경로
json_dir = "C:\\Users\\admin\\Desktop\\wooil\\Hyper\\2D_Bounding_Box\\2D_Bounding_Box1\\training\\labels"

class_mapping = {
   'car' : 0,
    'truck' : 1,
    'bus' : 2,
    'special vehicle' : 3,
    'motorcycle' : 4,
    'bicycle' : 5,
    'pedestrian' : 6,
    'traffic_sign' : 7,
    'traffic_light' : 8
}


# YOLO 포맷으로 변환하는 함수
def convert_to_yolo_format(annotation, image_resolution):

    label = annotation["Label"]
    class_idx = class_mapping.get(label, -1)  # 클래스가 없을 경우 -1을 반환
    if class_idx == -1:
        return ""  # 매핑되지 않은 클래스는 빈 문자열 반환
    coordinate = annotation["Coordinate"]
    x_center = (coordinate[0] + coordinate[2]/2)/image_resolution[0]
    y_center = (coordinate[1] + coordinate[3]/2)/image_resolution[1]
    width = coordinate[2]/image_resolution[0]
    height = coordinate[3]/ image_resolution[1]


    return f"{class_idx} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
def get_transform():
    return A.Compose([
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        ToTensorV2(),
    ])

model = fasterrcnn_resnet50_fpn(pretrained=True)
model.roi_heads.box_predictor.cls_score.out_features = len(class_mapping)
model.roi_heads.box_predictor.bbox_pred.out_features = len(class_mapping)
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)


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
            if yolo_annotation is not None:
                yolo_annotations.append(yolo_annotation)

        
        # YOLO 포맷으로 변환된 결과를 txt 파일로 저장
        output_file_name = os.path.splitext(json_file_name)[0] + ".txt"
        output_file_path = os.path.join(json_dir, output_file_name)
        with open(output_file_path, "w") as output_file:
            output_file.write("\n".join(yolo_annotations))
        
        print(f"{json_file_name}을 YOLO 포맷으로 변환하여 {output_file_name}에 저장했습니다.")