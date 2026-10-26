# Fruit Freshness Classification

Deep Learning project (B.Tech CSE, Semester V).
Mentor: Sachin Raghav

## Problem
Photo se pehchanna ki fruit fresh hai ya rotten. 3 fruits (apple, banana, orange), 6 classes.

## Dataset
Kaggle: "Fruits fresh and rotten for classification" (sriramr)
- Train: 10,901 images
- Test: 2,698 images
- Dataset bada hai, isliye repo me nahi hai. Kaggle se download karke `archive/` folder me rakho.

## Method
- Transfer learning: MobileNetV2 (ImageNet weights)
- Augmentation: flip, rotation, zoom, brightness
- Input size 224x224, 5 epochs, Adam optimizer

## Results
- Test accuracy: ~99%
- Weakest class: fresh oranges (recall 0.95)

## Demo kaise chalaye
```
pip install tensorflow gradio
python app.py
```
Phir browser me http://127.0.0.1:7860 kholo aur fruit ki photo upload karo.
