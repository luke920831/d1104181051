import os
import random
from PIL import Image

def generate_random_ROI(image, num_ROI, ROI_size):
    image_width, image_height = image.size
    ROIs = []

    for i in range(num_ROI):
        # 生成隨機的ROI左上角座標
        x = random.randint(0, image_width - ROI_size)
        y = random.randint(0, image_height - ROI_size)

        # 從原始影像中擷取ROI
        ROI = image.crop((x, y, x + ROI_size, y + ROI_size))
        ROIs.append(ROI)

    return ROIs

def save_ROIs(ROIs, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, ROI in enumerate(ROIs):
        output_filename = os.path.join(output_dir, f"ROI{i+1:02d}.bmp")
        ROI.save(output_filename)
        print(f"ROI{i+1:02d} 儲存至 {output_filename}")

def main():
    input_filename = "baboon.png"
    output_dir = "ROIs"
    num_ROI = 10
    ROI_size = 100

    # 讀取原始影像
    try:
        image = Image.open(input_filename)
    except FileNotFoundError:
        print(f"找不到 {input_filename}，請確保檔案存在並在正確的路徑中。")
        return

    # 生成隨機ROI
    ROIs = generate_random_ROI(image, num_ROI, ROI_size)

    # 儲存ROI
    save_ROIs(ROIs, output_dir)

if __name__ == "__main__":
    main()


