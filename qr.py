import qrcode

# Your GitHub Pages URL
url = "https://shakiraaaaaa.github.io/Health-care/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("health_care_qr.png")

print("QR code saved as 'health_care_qr.png'")
