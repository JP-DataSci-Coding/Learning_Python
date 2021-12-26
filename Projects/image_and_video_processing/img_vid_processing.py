import cv2

# Read galaxy.jpg image file
# Specifying a 0 will load the image in grayscale
image = cv2.imread('galaxy.jpg', 0)

# Should return numpy array, i.e. image in matrix form
# Images are just a matrices of pixels. A pixel is the smallest unit of a digital image or graphic that can be
# displayed and represented on a digital display device. A pixel is the basic logical unit in digital graphics.
# Pixels are combined to form a complete image, video, text, or any visible thing on a computer display.
print(image)
print(image.shape)  # Number of rows and columns
print(image.ndim)  # Dimensions
print(type(image))

cv2.imshow('Galaxy', image)
