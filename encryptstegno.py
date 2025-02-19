import cv2
import os

# Load the image
img = cv2.imread("my_img.png")  # Updated to use PNG file

# Take user inputs
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionary for encoding and decoding
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Encoding message into the image
m, n, z = 0, 0, 0

for char in msg:
    img[n, m, z] = d[char]
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= img.shape[1]:
            m = 0
            n += 1

# Marking end of the message with a special character
img[n, m, z] = d["~"]

# Save encrypted image
cv2.imwrite("encryptedImage.png", img)  # Updated to save as PNG
os.system("start encryptedImage.png")  # Open image in Windows

print("Message encrypted successfully in 'encryptedImage.png'.")
