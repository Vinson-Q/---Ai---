# 学习-AI玩游戏

## 项目简介
本项目旨在通过开发一个AI自动玩游戏（如植物大战僵尸）的程序，系统学习Python开发、图像识别、自动化操作、面向对象编程以及GitHub项目管理等技能。

---

## 环境搭建
1. **克隆或新建项目文件夹**
2. **创建并激活虚拟环境**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **安装依赖库**
   ```bash
   pip install -r requirements.txt
   ```
   > 如果没有requirements.txt，可以先手动安装：
   > ```bash
   > pip install mss opencv-python
   > ```

---

## 主要功能分步说明
1. **GitHub项目管理**
   - 注册GitHub账号，创建远程仓库
   - 本地初始化git，推送代码
2. **虚拟环境与依赖管理**
   - 使用venv创建独立环境，保证依赖隔离
3. **mss库截图功能**
   - 实现屏幕截图，为后续图像识别做准备
4. **窗口与界面**
   - 创建指定大小的客户端窗口（如807x631）
5. **特征图片采集**
   - 截取游戏关键区域图片，作为模板
6. **OpenCV模板识别**
   - 用OpenCV实现模板匹配，定位游戏界面关键坐标
7. **面向对象编程**
   - 封装功能为类，实现代码复用和模块化

---

## 学习记录建议
- 每完成一个功能，写下你的理解和遇到的问题
- 及时提交代码到GitHub，养成良好版本管理习惯
- 多查阅官方文档和优秀开源项目，提升解决问题能力

---

## 参考资料
- [mss官方文档](https://python-mss.github.io/)
- [OpenCV官方文档](https://docs.opencv.org/4.x/)
- [GitHub入门教程](https://docs.github.com/zh)

---

> 本项目适合初学者边做边学，遇到问题欢迎多提问、多记录、多总结！ 