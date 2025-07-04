import cv2

# 读取全屏截图和特征图片
img = cv2.imread('screenshot.png')
template = cv2.imread('features/feature.png')

# 模板匹配，返回每个位置的匹配结果
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 工作区域的左上角
window_x, window_y = max_loc

# 工作区域的宽高（已知）
window_w, window_h = 807, 631

# 工作区域的右下角
window_x2 = window_x + window_w
window_y2 = window_y + window_h

print(f"工作区域左上角：(x={window_x}, y={window_y})")
print(f"工作区域右下角：(x={window_x2}, y={window_y2})，宽={window_w}，高={window_h}")

# 可视化：在截图上画出工作区域
cv2.rectangle(img, (window_x, window_y), (window_x2, window_y2), (255, 0, 0), 2)
cv2.imwrite('work_area.png', img)
print("已在截图上标记工作区域，保存为 work_area.png") 