import argparse
import requests
from PIL import Image

# 引数のパーサーを作成する
parser = argparse.ArgumentParser(description='Convert an image to ASCII art.')
parser.add_argument('url', metavar='url', type=str, help='the URL of the image to convert')
parser.add_argument('--width', type=int, default=80, help='the number of ASCII characters per row (default: 80)')
parser.add_argument('--height', type=int, default=0, help='the number of ASCII characters per column (default: automatic calculation)')

# コマンドライン引数を解析する
args = parser.parse_args()

# 画像をダウンロードして保存する
response = requests.get(args.url)
with open("image.jpg", "wb") as f:
    f.write(response.content)

# 画像をアスキーアートに変換する
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
image = Image.open("image.jpg").convert("L")
width, height = image.size

if args.height == 0:
    aspect_ratio = height / float(width)
    args.height = int(aspect_ratio * args.width / 2)

aspect_ratio = height / float(width)
scale_y = aspect_ratio / 2

new_width = args.width
new_height = int(scale_y * args.height)
image = image.resize((new_width, new_height))

ascii_image = ""
for y in range(new_height):
    for x in range(new_width):
        pixel = image.getpixel((x, y))
        index = int((pixel/255) * (len(ascii_chars)-1))
        ascii_image += ascii_chars[index]
    ascii_image += "\n"

# アスキーアートを表示する
print(ascii_image)
