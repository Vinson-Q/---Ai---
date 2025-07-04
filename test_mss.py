import mss

# 创建一个mss截图对象
with mss.mss() as sct:
    # 截取全屏并保存为 screenshot.png
    sct.shot(output='screenshot.png')

print("截图完成，图片已保存为 screenshot.png") 