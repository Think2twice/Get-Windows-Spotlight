import os
import shutil
from PIL import Image

# Windows聚焦图片的原始路径
original_path = os.path.expanduser(
    '~') + '\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'

# 目标路径
target_path = 'C:\\WindowsFocusImages'


def is_wallpaper(image):
    # 判断图片是否适合作为壁纸（这里我们假设壁纸的宽度应大于其高度，并且宽度应大于1000像素）
    width, height = image.size
    return True if width > height and width > 1000 else False


# 创建目标文件夹（如果它尚不存在）
if not os.path.exists(target_path):
    os.makedirs(target_path)

# 检查原始路径下的每个文件
for filename in os.listdir(original_path):
    file_path = os.path.join(original_path, filename)

    try:
        with Image.open(file_path) as img:
            if is_wallpaper(img):
                target_file_path = os.path.join(target_path, filename + '.jpg')
                shutil.copyfile(file_path, target_file_path)
    except Exception as e:
        print(f"Error processing file {filename}: {e}")

print("Images have been successfully copied.")
