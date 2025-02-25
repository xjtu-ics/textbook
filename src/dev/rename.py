import os
import shutil

def rename_and_move_images():
    original_format = "image-{}.png"
    # change for different chapter
    new_format = "github-{}.png"
    
    # 确保目标文件夹存在
    target_folder = "image"
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # 处理0到32的图片
    for i in range(11):
        original_file = original_format.format(i)
        new_file = new_format.format(i)
        
        if os.path.exists(original_file):
            # 重命名并移动文件
            new_path = os.path.join(target_folder, new_file)
            shutil.move(original_file, new_path)
            print(f"Renamed {original_file} to {new_file} and moved to {target_folder}")
        else:
            print(f"File {original_file} does not exist")

if __name__ == "__main__":
    rename_and_move_images()
