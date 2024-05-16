import cv2
import matplotlib.pyplot as plt

image_path = "images/anime.jpg"
image = cv2.imread(image_path)

if image is None:
    print("f:Error in displaying")
else:
    # gaussian blur to image
    blurred_image = cv2.GaussianBlur(image,(5,5),5)

    plt.figure(figsize=(12,6))

    plt.subplot(1,2,1)
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.imshow(cv2.cvtColor(blurred_image,cv2.COLOR_BGR2RGB))
    plt.title('Blurred Image')
    plt.axis('off')

    plt.show()