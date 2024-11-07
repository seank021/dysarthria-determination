# 훈련/검증 손실 정확도 출력
import matplotlib.pyplot as plt

def draw_graph(history):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].plot(history.history['loss'])
    axs[0].plot(history.history['val_loss'])
    axs[0].set_xlabel('epoch')
    axs[0].set_ylabel('loss')
    axs[0].legend(['train', 'val'])
    axs[0].set_title('loss for each epoch')

    axs[1].plot(history.history['accuracy'])
    axs[1].plot(history.history['val_accuracy'])
    axs[1].set_xlabel('epoch')
    axs[1].set_ylabel('accuracy')
    axs[1].legend(['train', 'val'])
    axs[1].set_title('accuracy for each epoch')

    plt.show()