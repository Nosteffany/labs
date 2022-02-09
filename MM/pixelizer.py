import cv2

# Input image
input = cv2.imread(r'C:\Users\me\Desktop\project\HED2\images\winter.jpg')

# Get input size
height, width = input.shape[:2]
sz = 164
# Desired "pixelated" size
w, h = (sz, sz)

# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Input', input)
cv2.imshow('Output', output)

cv2.waitKey(0)
