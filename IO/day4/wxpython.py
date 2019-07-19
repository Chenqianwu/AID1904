import wx  # 导入wxPython


class App(wx.App):
    def OnInit(self):  # 初始化方法
        frame = wx.Frame(parent=None, title='第一个窗口程序')  # 创建顶级窗口
        frame.Show()  # 显示窗口
        return True  # 返回值(返回窗口，在屏幕展示)


if __name__ == '__main__':
    app = App()  # 实例化App类
    app.MainLoop()  # 调用App类的MainLoop()主循环方法
