import os
import requests
from PIL import Image

# 保存フォルダの名前
save_folder = "downloaded_images"
cropped_folder = "cropped_images"

# 保存フォルダを作成する
os.makedirs(save_folder, exist_ok=True)
os.makedirs(cropped_folder, exist_ok=True)

# 画像のURLの基本部分
base_url = "https://www.hagaren.jp/fa/characters/images01/detail/"

# 1から48までの画像を処理する
for i in range(1, 49):
    # 画像のURLを作成する
    image_url = f"{base_url}{i}.jpg"
    
    # 保存する画像のファイル名を設定する
    image_filename = os.path.join(save_folder, f"image_{i}.jpg")
    cropped_filename = os.path.join(cropped_folder, f"cropped_image_{i}.jpg")

    try:
        # 画像をダウンロードする
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # エラーが発生した場合に例外を投げる

        # ダウンロードした画像をファイルに保存する
        with open(image_filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {image_filename}")

        # 画像を開く
        with Image.open(image_filename) as img:
            # 縦幅を取得する
            width, height = img.size
            crop_size = min(width, height)  # 縦幅と横幅の小さい方を基準にする

            # 右からトリミングして正方形にする
            left = width - crop_size
            top = 0
            right = width
            bottom = crop_size
            cropped_img = img.crop((left, top, right, bottom))

            # 加工した画像を保存する
            cropped_img.save(cropped_filename)
            print(f"Cropped and saved: {cropped_filename}")

    except Exception as e:
        print(f"Error processing {image_url}: {e}")

print("すべての処理が完了しました！")
