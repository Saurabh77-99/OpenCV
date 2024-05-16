import cv2
import matplotlib.pyplot as plt

image_path = 'images/anime.jpg'

image = cv2.imread(image_path)

# print(cv2.__version__)
if image is None:
    print(f"Error:Unable to  load image at {image_path}")
else:
    width = 400
    height = 500
    resized_image = cv2.resize(image,(width,height))
    
    gray_image = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)

    # plt.imshow(cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGBA))
    plt.imshow(gray_image,cmap='gray')
    plt.title('Anime grayscale resized')
    plt.axis('off')
    plt.show()
