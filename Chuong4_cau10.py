#Câu 10: Vẽ hình dùng Sleep
import os
import time

# Hàm xóa màn hình (Windows và macOS/Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Các khung hình
frames = [
    [
        "   *   ",
        "   **  ",
        "   *** ",
        "*******",
        " ***   ",
        "  **   ",
        "   *   "
    ],
    [
        "   *   ",
        "   **  ",
        "   * *  ",
        "*******",
        " * *   ",
        "  **   ",
        "   *   "
    ],
    [
        "   ***** ",
        "   ***   ",
        "   **    ",
        "   *     ",
        "  **     ",
        " ***     ",
        "****     "
    ],
    [
        "   ***** ",
        "   * *   ",
        "   **    ",
        "   *     ",
        "  **     ",
        " * *     ",
        "****     "
    ]
]

# Lặp qua các khung hình tạo hiệu ứng
while True:
    for frame in frames:
        clear()
        for line in frame:
            print(line)
        time.sleep(0.3)  # Tạm dừng 0.3 giây mỗi khung

