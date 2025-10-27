import qrcode
import sys
import os
from datetime import datetime

def generate_qr(url: str):
    # Ensure output folder exists
    output_dir = "qr_codes"
    os.makedirs(output_dir, exist_ok=True)

    # Generate QR
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save with timestamp
    filename = f"{output_dir}/qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

if __name__ == "__main__":
    # Allow custom URL argument
    if len(sys.argv) > 2 and sys.argv[1] == "--url":
        url = sys.argv[2]
    else:
        url = "https://github.com/kaw393939"
    generate_qr(url)
