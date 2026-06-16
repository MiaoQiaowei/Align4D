import os

def rename_mp4_files(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):  # 遍历所有文件夹和文件
        for filename in filenames:  # 遍历当前文件夹中的所有文件
            if filename.lower().endswith(".mp4"):  # 检查是否是.mp4文件
                old_path = os.path.join(dirpath, filename)  # 原文件路径
                new_name = None  # 用于存储新的文件名

                # 判断文件名并修改
                if filename.isdigit() and len(filename.split(".")[0]) == 3:  # 三位数字.mp4
                    # new_name = "base.mp4"
                    continue  # 跳过
                elif "static" in filename.lower():  # 包含"static"
                    new_name = "3D.mp4"
                elif filename.lower() == "0.mp4" or "right" in filename:  # 文件名为"0.mp4"
                    new_name = "Align4D.mp4"
                elif "generated" in filename.lower():
                    new_name = "video.mp4"

                # 如果需要重命名
                if new_name:
                    new_path = os.path.join(dirpath, new_name)

                    # 检查是否已存在目标文件
                    if os.path.exists(new_path):
                        print(f"目标文件已存在，跳过：{new_path}")
                    else:
                        os.rename(old_path, new_path)  # 执行重命名
                        print(f"重命名: {old_path} -> {new_path}")

# 使用示例：将 "your_folder_path" 替换为你实际的文件夹路径
root_folder = r"D:\Desktop\Align4D\videos\show"
rename_mp4_files(root_folder)
