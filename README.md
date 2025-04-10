# 📦 2D Bounding Box 객체 탐지 데이터셋 전처리 및 YOLO 포맷 변환

본 프로젝트는 주어진 JSON 포맷의 라벨 데이터를 **YOLO 형식**으로 변환하고, 객체 탐지 모델 학습을 위한 환경을 구축하기 위한 파이프라인입니다.  
학습, 검증 및 테스트 데이터를 YOLO 형식으로 자동 변환하고, `train.txt`, `val.txt`, `.yaml` 구성 파일을 생성하여 학습에 바로 활용할 수 있습니다.

---



## ✅ 주요 기능

### 📄 1. 이미지 경로 목록 생성
- `glob`을 통해 학습/검증 이미지 파일 경로를 수집
- `train.txt`, `valid.txt`로 저장

### 🔄 2. JSON ➝ YOLO 포맷 변환
- 주어진 JSON 파일에서 객체 정보(`Label`, `Coordinate`)를 불러와 YOLO 형식으로 변환
- 변환된 라벨을 `.txt` 파일로 저장

```text
YOLO 포맷: <class_id> <x_center> <y_center> <width> <height>

