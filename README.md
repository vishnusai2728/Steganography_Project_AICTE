# Image Steganography Project

This project implements a simple image steganography technique using OpenCV in Python to hide and retrieve secret messages within an image.

## Files in the Repository

- **encryptstegno.py** - Encrypts a secret message into an image.
- **decrptstegno.py** - Decrypts the hidden message from the encrypted image.
- **my_img.png** - The input image used for steganography.
- **encryptedImage.png** - The output image containing the hidden message.

## Requirements

Ensure you have the following installed before running the scripts:

- Python 3.x
- OpenCV (`cv2`)

Install dependencies using:
```bash
pip install opencv-python
```

## Usage

### Encryption
1. Run `encryptstegno.py`:
```bash
python encryptstegno.py
```
2. Enter the secret message.
3. Provide a passcode for encryption.
4. The script embeds the message into `my_img.png` and saves it as `encryptedImage.png`.

### Decryption
1. Run `decrptstegno.py`:
```bash
python decrptstegno.py
```
2. Enter the correct passcode.
3. The hidden message will be extracted and displayed.

## Notes
- The image should have enough pixels to store the message.
- If an incorrect passcode is provided, decryption will fail.

## License
This project is open-source and available for use and modification.
