import os
import shutil
from PIL import Image
from datetime import datetime

# Windows聚焦图片的原始路径
original_path = os.path.expanduser(
    '~') + '\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'

# 目标路径
base_target_path = 'C:\\WindowsFocusImages'


def is_wallpaper(image):
    # 判断图片是否适合作为壁纸（这里我们假设壁纸的尺寸应大于1000像素）
    width, height = image.size
    return 'landscape' if width > height and width > 1000 else 'portrait' if height > width and height > 1000 else None


# 获取当前日期并创建相应的目录
today = datetime.today().strftime('%y%m%d')
target_path = os.path.join(base_target_path, today)

if not os.path.exists(target_path):
    os.makedirs(target_path)

# 为每个方向的图片分配一个序号
orientation_counters = {'landscape': 0, 'portrait': 0}

# 检查原始路径下的每个文件
for filename in os.listdir(original_path):
    file_path = os.path.join(original_path, filename)

    try:
        with Image.open(file_path) as img:
            orientation = is_wallpaper(img)
            if orientation:
                orientation_counters[orientation] += 1
                orientation_path = os.path.join(target_path, orientation)
                if not os.path.exists(orientation_path):
                    os.makedirs(orientation_path)
                target_file_path = os.path.join(orientation_path, f'{orientation_counters[orientation]:03d}.jpg')
                shutil.copyfile(file_path, target_file_path)
    except Exception as e:
        print(f"Error processing file {filename}: {e}")
