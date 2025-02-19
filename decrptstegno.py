import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")  # Updated to use PNG file

# Take passcode input
pas = input("Enter passcode for Decryption: ")

# Dictionary for decoding
c = {i: chr(i) for i in range(255)}

# Check password
if pas == input("Enter the same passcode: "):  
    message = ""
    m, n, z = 0, 0, 0

    while True:
        char = c[img[n, m, z]]
        if char == "~":  # Stop when message terminator is found
            break
        message += char
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
