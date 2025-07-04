from features.screenshot import ScreenCapturer
from features.template_match import TemplateMatcher
from features.area_marker import AreaMarker

# 1. 截图
capturer = ScreenCapturer('screenshot.png')
capturer.capture()

# 2. 模板匹配
matcher = TemplateMatcher('screenshot.png', 'features/feature.png')
max_loc, w, h, max_val = matcher.match()

if max_val < 0.8:
    print("没有匹配的特征图片，请检查游戏窗口是否已经打开，或特征图片是否正确！")
else:
    print(f"特征图片匹配到的位置：{max_loc}，模板宽高：{w}x{h}，匹配度：{max_val:.2f}")
    marker = AreaMarker('screenshot.png')
    marker.mark(max_loc[0], max_loc[1], 807, 631, 'work_area.png') 