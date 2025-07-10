import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import sys

def generate_qr_code(data, filename="qrcode.png", fill_color="black", back_color="white", size=10):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"✅ QR code generated successfully: {filename}")
        print(f"🔹 Data encoded: {data}")
        img.show()
    except Exception as e:
        print(f"❌ Error generating QR code: {str(e)}")

def add_text_label(img, text):
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text_width = font.getlength(text)
    img_width = img.size[0]
    position = ((img_width - text_width) / 2, img.size[1] - 20)
    draw.text(position, text, font=font, fill="black")
    return img

def main():
    print("\n" + "=" * 50)
    print("📟 QR Code Generator (Python Edition)")
    print("=" * 50)
    
    while True:
        try:
            data = input("\n➡ Enter text/URL (or 'q' to quit): ").strip()
            if data.lower() in ["q", "quit"]:
                print("\n👋 Exiting program... Goodbye!")
                break
            if not data:
                print("⚠ Please enter valid text or a URL.")
                continue
            filename = f"qr_{data[:10]}.png".replace(" ", "").replace("://", "")
            generate_qr_code(data, filename=filename)
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            sys.exit(0)
            
if _name_ == "_main_":
    main()
