# dysarthria-determination
- 2023 AI입문 프로젝트 (2인 1조)
- 마비말장애(dysarthria) 여부를 판단하는 머신러닝 시스템

## What is dysarthria?
마비말장애(dysarthria)란 말소리장애의 신경계조절장애 중 하나로, 조음에 관여하는 근육의 마비, 약화, 협응 실패로 인해 일어난다. 호흡, 발성, 조음, 공명, 운율 문제로 인한 말명료도의 저하가 나타나는데, 이 때문에 마비말장애의 주된 특징은 부정확한 자음이다.

## Why this ML system is needed
이러한 조음장애를 판별하는 데에는 주로 청지각적 평가가 사용되기 때문에 전문가의 주관적인 생각이 개입될 가능성이 크다. 또한, 마비말장애를 판별하는 과정에서 객관적인 모델이 쓰이지 않고 있다는 현실에 의거하여, 만일 이를 판단하는 머신러닝 시스템이 존재한다면 조금 더 명확하고 객관적인 분류가 가능할 것이라 판단하였다. 더 나아가, 대부분의 음성 장애의 경우 질병 여부와 장애 종류를 판단하기 위해서는 laryngoscopy, stroboscopy 등의 침습적인 진단이 요구된다. 이러한 진단 방식은 비용이 많이 들며 직접 병원에 가야지만 가능하다는 한계점을 지닌다. 따라서 머신러닝 기반의 프로그램을 통해 음성을 객관적으로 인식하고, 음성 장애를 적절히 진단할 수 있다면 비용적 측면에서도 많은 이점을 가질 것이다.

## Method
마비말장애를 가진 사람들과 그렇지 않은 사람들의 음성 데이터를 모은다. 이는 이후 데이터 수집 부분에서 그 출처를 밝힐 예정이다. 그 후 데이터 전처리, 모델 구축 및 훈련 등의 과정을 거쳐 마비말장애 여부를 분류하는 머신러닝 시스템을 구축할 예정이다.

- dataset: https://www.kaggle.com/datasets/iamhungundji/dysarthria-detection (torgo_data.zip)
- reference code: https://www.kaggle.com/code/akshadagaonkar/dysarthria-detection-cnn/notebook
- waveplot, MFCC, Mel-Spectrogram, CNN

## Result
- model.evaluate()
    - loss: 0.0436
    - accuracy: 0.9833
- Confusion Matrix
    - F1 Score: 0.98
