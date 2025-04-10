# 📦 Object detection with 2D Bounding Box (YOLO)

This project provides a complete pipeline to convert annotation data in JSON format into the **YOLO format** for object detection tasks. It automatically processes training, validation, and test datasets, creates `train.txt` and `valid.txt` image lists, and generates a `custom_dataset.yaml` configuration file for YOLO training.

---

## 📁 Directory Structure Example

```
2D_Bounding_Box/
├── training/
│   ├── images/
│   └── labels/         # JSON label files
├── validation/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
```

---

## ✅ Main Features

### 📄 1. Image Path List Generation
- Uses `glob` to collect training and validation image file paths
- Saves them as `train.txt` and `valid.txt` for YOLO training

### 🔄 2. JSON ➝ YOLO Format Conversion
- Extracts `Label` and `Coordinate` info from JSON files
- Converts each annotation to YOLO format:

```
YOLO Format: <class_id> <x_center> <y_center> <width> <height>
```

- Saves converted annotations to `.txt` files

### 🧭 3. Class Mapping and YAML Configuration File Creation
- Generates `custom_dataset.yaml` with class names and paths to image lists

```yaml
nc: 9
names: ["car", "truck", "bus", "special_vehicle", "motorcycle", "bicycle", "pedestrian", "traffic_sign", "traffic_light"]
train: path_to_train.txt
val: path_to_valid.txt
```

### 📊 4. Data Augmentation using Albumentations
- Horizontal and vertical flips are applied for data augmentation using Albumentations

---

## 🔧 Requirements

- Python 3.8+
- PyTorch
- Albumentations
- TorchVision
- PyYAML

```bash
pip install torch torchvision albumentations pyyaml
```

---

## 📌 Class Mapping

| Class ID | Class Name        |
|----------|-------------------|
| 0        | car               |
| 1        | truck             |
| 2        | bus               |
| 3        | special vehicle   |
| 4        | motorcycle        |
| 5        | bicycle           |
| 6        | pedestrian        |
| 7        | traffic_sign      |
| 8        | traffic_light     |

---

## 🗂️ Output Files

| File                          | Description                           |
|-------------------------------|---------------------------------------|
| `train.txt`, `valid.txt`      | Lists of image file paths             |
| `custom_dataset.yaml`         | YOLO configuration file               |
| `.txt` (YOLO labels)          | Annotation files in YOLO format       |

---

## 🚀 Future Enhancements

- Add bounding box visualization tool
- Add label validation utilities (e.g., invalid box checker)
- Automate training script generation for YOLOv5/YOLOv8

---

## 📝 References

- [Albumentations Documentation](https://albumentations.ai/)
- [YOLO Format Guide - Ultralytics](https://docs.ultralytics.com/datasets/detect/#format)
