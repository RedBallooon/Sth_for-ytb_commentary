from yt_dlp import YoutubeDL
from tkinter import Tk
from tkinter.filedialog import askdirectory

#tinker
root = Tk()
root.withdraw()

# Nhập URL của video
vid_url = input("Nhập URL của video: ")

# Mở File Explorer để chọn thư mục
print("Chọn thư mục để lưu video...")
save_path = askdirectory()

if save_path:
    print("Đang tải xuống video...")
    # Cấu hình `yt-dlp`
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Định dạng tên tệp
        'format': 'bestvideo+bestaudio/best',         # Chọn chất lượng tốt nhất
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([vid_url])
    print(f"Video đã được tải xuống tại {save_path}")
else:
    print("Bạn chưa chọn thư mục. Không có tệp nào được tải xuống.")
