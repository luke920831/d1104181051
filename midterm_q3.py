# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:07:49 2024

@author: F308
"""

from PIL import ImageEnhance, Image

def image_enhancement(image_path):
    # 打開原始影像
    original_image = Image.open(image_path)

    # 1. 調整亮度
    brightness = ImageEnhance.Brightness(original_image)
    enhanced_brightness_image = brightness.enhance(3)  # 增強亮度1.5倍

    # 2. 調整對比度
    contrast = ImageEnhance.Contrast(enhanced_brightness_image)
    enhanced_contrast_image = contrast.enhance(0.5)  # 增強對比度1.5倍

    # 3. 調整色彩飽和度
    saturation = ImageEnhance.Color(enhanced_contrast_image)
    enhanced_saturation_image = saturation.enhance(1.5)  # 增強色彩飽和度1.2倍

    # 4. 調整銳度
    sharpness = ImageEnhance.Sharpness(enhanced_saturation_image)
    enhanced_sharpness_image = sharpness.enhance(3.0)  # 增強銳度2倍

    # 5. 儲存增強後的影像
    output_path = "carshort_grey.jpg"
    enhanced_sharpness_image.save(output_path)
    print(f"影像增強完成，結果已儲存至 {output_path}")

    # 顯示增強後的影像
    enhanced_sharpness_image.show()

def main():
    # 輸入原始影像路徑
    image_path = "carshort_grey.jpg"

    # 執行影像增強
    image_enhancement(image_path)

if __name__ == "__main__":
    main()
