from PIL import Image

def generate_chessboard(size, square_size):
    # 創建一個新的空影像
    image = Image.new('L', (size, size), color=0)
    pixels = image.load()

    # 設置每個方塊的大小
    square_width = size // square_size
    square_height = size // square_size

    # 用白色和黑色交替填充方塊
    for i in range(square_size):
        for j in range(square_size):
            if (i + j) % 2 == 0:
                for x in range(square_width):
                    for y in range(square_height):
                        pixels[i * square_width + x, j * square_height + y] = 255

    return image

def main():
    image_size = 512
    square_size = 8
    output_filename = "output.bmp"

    # 生成西洋棋盤影像
    chessboard_image = generate_chessboard(image_size, square_size)

    # 儲存影像
    chessboard_image.save(output_filename)
    print(f"影像已儲存至 {output_filename}")

if __name__ == "__main__":
    main()

     

