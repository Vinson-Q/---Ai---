import cv2

class TemplateMatcher:
    def __init__(self, img_path, template_path):
        """
        初始化模板匹配器。
        :param img_path: 原始图片路径
        :param template_path: 特征图片路径
        """
        self.img_path = img_path
        self.template_path = template_path

    def match(self):
        """
        在原始图片中查找特征图片，返回最佳匹配的左上角坐标、模板宽高和匹配度。
        :return: (max_loc, w, h, max_val)
        """
        img = cv2.imread(self.img_path)
        template = cv2.imread(self.template_path)
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        h, w = template.shape[:2]
        return max_loc, w, h, max_val

    def is_match(self, threshold=0.8):
        """
        判断是否匹配成功。
        :param threshold: 匹配度阈值
        :return: True/False
        """
        _, _, _, max_val = self.match()
        return max_val >= threshold 