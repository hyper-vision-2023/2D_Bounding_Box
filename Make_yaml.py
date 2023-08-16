import yaml

# 클래스 이름과 인덱스 매핑
class_mapping = {
    1: "car",
    2: "truck",
    3: "bus",
    4: "special_vehicle",
    5: "motorcycle",
    6: "bicycle",
    7: "pedestrian",
    8: "traffic_sign",
    9: "traffic_light"
}

# YAML 파일에 들어갈 데이터 생성
data = {
    "names": list(class_mapping.values()),
    "nc": len(class_mapping),
    "train": "path_to_train.txt",
    "val": "path_to_valid.txt"
}

# YAML 파일 생성
yaml_file_path = "custom_dataset.yaml"
with open(yaml_file_path, "w") as yaml_file:
    yaml.dump(data, yaml_file)

print(f"YAML 파일 {yaml_file_path}이 생성되었습니다.")