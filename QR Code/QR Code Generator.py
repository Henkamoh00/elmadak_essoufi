import qrcode
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_qr(url):
    # توليد رمز QR للرابط المختصر
    qr = qrcode.make(url)
    qr.save(os.path.join(BASE_DIR, "qr_code.png"))  # حفظ الرمز في ملف


def generate_qr_with_logo(url, logo_path):
    # توليد رمز QR للرابط
    qr = qrcode.make(url)
    
    # فتح الصورة التي سيتم وضعها في المنتصف
    logo = Image.open(logo_path)

    # # إذا كانت الصورة تحتوي على قناة ألفا (شفافية)، نقوم بإزالتها
    # if logo.mode == 'RGBA':
    #     logo = logo.convert('RGB')  # تحويل الصورة إلى وضع RGB بدون شفافية

    if logo.mode != 'RGBA':
        logo = logo.convert('RGBA')
    qr = qr.convert('RGBA')
    # حساب حجم الصورة ووضعها في المنتصف
    qr_width, qr_height = qr.size
    logo_size = int(qr_width / 2.5)  # تعديل الحجم كما تريد
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # حساب موضع وضع الصورة في المنتصف
    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # دمج الرمز مع الصورة (بدون قناع شفافية)
    qr.paste(logo, logo_position, logo)

    # حفظ الرمز النهائي
    qr.save(os.path.join(BASE_DIR, "qr_code_with_logo.png"))


logo_path = os.path.join(BASE_DIR, "..", "images", "logo.png")
url = "https://elmadakessoufi.space"
generate_qr(url)
generate_qr_with_logo(url, logo_path)