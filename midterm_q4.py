from PIL import Image, ImageFilter, ImageEnhance

def image_enhancement(image_path):
    # 打開原始影像
    original_image = Image.open(image_path)

    # 1. 模糊處理
    blurred_image = original_image.filter(ImageFilter.BLUR)

    # 2. 銳化處理
    sharpened_image = blurred_image.filter(ImageFilter.SHARPEN)

    # 3. 調整亮度
    brightness = ImageEnhance.Brightness(sharpened_image)
    enhanced_brightness_image = brightness.enhance(0.85)  # 增強亮度1.5倍

    # 4. 調整對比度
    contrast = ImageEnhance.Contrast(enhanced_brightness_image)
    enhanced_contrast_image = contrast.enhance(3.5)  # 增強對比度1.5倍

    # 5. 儲存增強後的影像
    output_path = "enhanced_image.png"
    enhanced_contrast_image.save(output_path)
    print(f"影像增強完成，結果已儲存至 {output_path}")

    # 顯示增強後的影像
    enhanced_contrast_image.show()

def main():
    # 輸入原始影像路徑
    image_path = "over_exposure_grey.jpg"

    # 執行影像增強
    image_enhancement(image_path)

if __name__ == "__main__":
    main()
