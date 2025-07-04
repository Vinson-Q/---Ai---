import cv2

# 读取全屏截图和特征图片
img = cv2.imread('screenshot.png')
template = cv2.imread('features/feature.png')

# 模板匹配，返回每个位置的匹配结果
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# 获取最佳匹配位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 获取特征图片的宽高
h, w = template.shape[:2]

# 在原图上画出匹配区域（矩形框）
cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

# 保存结果图片
cv2.imwrite('match_result.png', img)

print(f"最佳匹配位置：{max_loc}，匹配度：{max_val:.2f}")
print("结果图片已保存为 match_result.png") 