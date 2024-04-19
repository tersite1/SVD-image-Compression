import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load_image():
    """ 이미지 파일을 선택하고 numpy 배열로 변환하는 함수 """
    root = tk.Tk()
    root.withdraw()  # 루트 윈도우를 숨깁니다
    file_path = filedialog.askopenfilename()  # 파일 선택 다이얼로그
    image = Image.open(file_path)
    image = image.convert('RGB')  # RGB로 변환
    data = np.array(image)
    return data

def perform_svd(data, k):
    """ 이미지에 대해 RGB 채널별로 SVD를 수행하고 압축된 이미지 데이터를 반환하는 함수 """
    compressed_data = np.zeros_like(data)
    singular_values = {}
    for i in range(3):  # RGB 채널별로 반복
        U, s, VT = np.linalg.svd(data[:, :, i], full_matrices=False)
        S = np.diag(s[:k])
        compressed_data[:, :, i] = np.dot(U[:, :k], np.dot(S, VT[:k, :]))
        singular_values['RGB'[i]] = s
    return compressed_data, singular_values

def display_singular_values(singular_values):
    """ 특이값을 그래프로 표시하는 함수 """
    plt.figure()
    for key, values in singular_values.items():
        plt.semilogy(values, label=f'{key} channel')
    plt.title('Singular Values by Channel')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

def main():
    data = load_image()
    k = simpledialog.askinteger("Input", "압축할 특이값의 개수를 입력하세요:")
    compressed_data, singular_values = perform_svd(data, k)
    
    # 압축된 이미지 표시
    plt.imshow(compressed_data)
    plt.title(f'Compressed image with {k} singular values')
    plt.axis('off')  # 축 없애기
    plt.show()
    
    # 특이값 그래프 표시
    display_singular_values(singular_values)

if __name__ == '__main__':
    main()
