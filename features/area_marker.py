import cv2

class AreaMarker:
    def __init__(self, img_path):
        """
        初始化区域标记器。
        :param img_path: 原始图片路径
        """
        self.img_path = img_path

    def mark(self, start_x, start_y, w, h, output_path='work_area.png'):
        """
        在图片上标记指定区域并保存。
        :param start_x: 区域左上角x坐标
        :param start_y: 区域左上角y坐标
        :param w: 区域宽度
        :param h: 区域高度
        :param output_path: 输出图片路径
        """
        img = cv2.imread(self.img_path)
        end_x, end_y = start_x + w, start_y + h
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (255, 0, 0), 2)
        cv2.imwrite(output_path, img)
        print(f"已在截图上标记区域，保存为 {output_path}") 