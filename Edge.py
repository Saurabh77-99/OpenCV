import cv2
import matplotlib.pyplot as plt

image_path = "images/anime.jpg"
image = cv2.imread(image_path)

if image is None:
    print("f:Error in displaying")
else:
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_image,100,200)

    plt.figure(figsize=(12,6))

    plt.subplot(1,2,1)
    plt.imshow(gray_image,cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(edges,cmap='gray')
    plt.title('Edge Detected Image')
    plt.axis('off')

    plt.show()