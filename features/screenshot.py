import mss

class ScreenCapturer:
    def __init__(self, output_path='screenshot.png'):
        """
        初始化截图器，指定输出文件名。
        :param output_path: 截图保存路径
        """
        self.output_path = output_path

    def capture(self):
        """
        截取全屏并保存为指定文件。
        """
        with mss.mss() as sct:
            sct.shot(output=self.output_path)
        print(f"截图已保存为 {self.output_path}") 