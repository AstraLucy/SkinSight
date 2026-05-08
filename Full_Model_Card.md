# Model Card — Skin Lesion Classification Model

## Model Overview

This project is a deep learning image classification model designed to classify dermatological skin lesion images into multiple diagnostic categories. The model was developed using transfer learning with MobileNetV2 and implemented using [Keras](https://keras.io?utm_source=chatgpt.com) and [TensorFlow](https://www.tensorflow.org?utm_source=chatgpt.com).

The aim of the project was to explore the practical application of convolutional neural networks (CNNs) within a healthcare imaging context.

---

# Model Details

| Item                | Description                                       |
| ------------------- | ------------------------------------------------- |
| Model Type          | Convolutional Neural Network (CNN)                |
| Architecture        | MobileNetV2                                       |
| Framework           | TensorFlow / Keras                                |
| Task                | Multiclass image classification                   |
| Input Size          | 224 × 224 RGB images                              |
| Output              | Probability distribution across 10 lesion classes |
| Activation Function | Softmax                                           |
| Loss Function       | Sparse Categorical Crossentropy                   |
| Optimizer           | Adam                                              |
| Transfer Learning   | Yes                                               |
| Pretrained Weights  | ImageNet                                          |
| Fine-Tuning         | Partial fine-tuning of deeper layers              |

---

# Intended Use

## Primary Use

* Educational and research demonstration of AI-assisted medical image classification.
* Exploration of transfer learning techniques for healthcare datasets.
* Proof-of-concept dermatology image classifier.

## Intended Users

* Students
* Researchers
* Developers learning medical AI workflows
* Educational demonstrations

---

# Out-of-Scope Use

This model is **not intended** for:

* Clinical diagnosis
* Medical decision-making
* Emergency healthcare settings
* Autonomous diagnostic use
* Replacement of professional dermatological assessment

The model should be considered a research prototype only.

---

# Training Data

The model was trained on a labelled multiclass skin lesion image dataset containing dermatological image categories.

## Dataset Characteristics

* RGB dermoscopic/clinical skin images
* Multiple lesion categories
* Variable class distribution
* Pre-split into training, validation, and testing datasets

## Preprocessing

* Image resizing to 224×224
* Normalisation using MobileNetV2 preprocessing
* Data augmentation:

  * Horizontal flipping
  * Rotation
  * Zoom augmentation

---

# Model Architecture

The model uses a pretrained MobileNetV2 feature extractor followed by custom classification layers.

## Architecture Summary

```python
Input Layer
→ Data Augmentation
→ MobileNetV2 (ImageNet pretrained)
→ GlobalAveragePooling2D
→ BatchNormalization
→ Dense(128, ReLU)
→ Dropout(0.3)
→ Dense(10, Softmax)
```

---

# Performance

| Metric              | Result                             |
| ------------------- | ---------------------------------- |
| Overall Accuracy    | 69%                                |
| Classification Type | 10-class multiclass classification |
| Transfer Learning   | Successful                         |
| Fine-Tuning Applied | Yes                                |

## Interpretation

The model demonstrated the ability to learn meaningful visual features from dermatological images and perform multiclass classification substantially above random baseline performance.

Performance varied between classes, with stronger results typically observed in categories containing larger numbers of training examples.

---

# Strengths

* Lightweight and efficient architecture
* Fast training and inference compared to larger CNNs
* Effective use of transfer learning
* Supports multiclass classification
* Demonstrates practical medical imaging workflow
* Suitable for educational and research applications

---

# Limitations

* Performance may vary across lesion categories
* Sensitive to image quality and lighting conditions
* Class imbalance may affect minority class accuracy
* Dataset diversity may limit generalisation
* Not clinically validated
* Should not be used as a standalone diagnostic system

---

# Ethical Considerations

Medical AI systems can inherit biases present within training data. Differences in skin tone representation, image quality, lesion prevalence, and annotation quality may influence model performance.

The model should therefore be used responsibly within educational or research contexts only and not as a replacement for professional clinical judgement.

---

# Future Improvements

Potential future developments include:

* Larger and more balanced datasets
* Improved class balancing techniques
* Higher-resolution image processing
* Use of EfficientNet architectures
* Additional evaluation metrics
* Confusion matrix analysis
* Explainable AI visualisation methods (e.g., Grad-CAM)

---

# Technical Specifications

| Specification               | Value                           |
| --------------------------- | ------------------------------- |
| Input Shape                 | (224, 224, 3)                   |
| Batch Size                  | Configurable                    |
| Training Method             | Transfer Learning + Fine-Tuning |
| Base Model Frozen Initially | Yes                             |
| Fine-Tuning Learning Rate   | 1e-5                            |
| Output Classes              | 10                              |
| Model Format                | `.keras`                        |

---

# Conclusion

This project demonstrates the successful implementation of a transfer learning pipeline for multiclass skin lesion classification using MobileNetV2. The model achieved encouraging performance for an educational healthcare AI prototype and highlights both the potential and practical challenges of applying deep learning techniques within medical imaging domains.
