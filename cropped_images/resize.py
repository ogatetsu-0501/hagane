from PIL import Image
import os

def resize_images(directory, size=(100, 100)):
    # 指定したディレクトリとそのサブディレクトリのファイルを再帰的に処理
    for root, _, files in os.walk(directory):
        for filename in files:
            # .jpg または .JPG ファイルを対象とする
            if filename.lower().endswith('.jpg'):
                file_path = os.path.join(root, filename)

                try:
                    # 画像を開く
                    with Image.open(file_path) as img:
                        # 画像をリサイズ
                        img_resized = img.resize(size, Image.Resampling.LANCZOS)
                        # 上書き保存
                        img_resized.save(file_path)
                        print(f"Resized: {file_path}")
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

# 実行ディレクトリを指定
if __name__ == "__main__":
    current_directory = os.path.join(os.getcwd(), "cropped_images")  # cropped_images フォルダを指定
    resize_images(current_directory)
