import wx
import logging
app = wx.App()
frame = wx.Frame(None, title="Log File GUI", size=(350, 200))
panel = wx.Panel(frame)
def create_log(event):
    logging.basicConfig(
        filename="HELLO.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Program started")
    logging.warning("Low battery")
    logging.error("File not found")
    logging.error("Connection failed")
    logging.info("Program ended")
    wx.MessageBox("Log file created (HELLO.log)", "Success")
def count_errors(event):
    error_count = 0
    try:
        with open("HELLO.log", "r") as f:
            for line in f:
                if "ERROR" in line:
                    error_count += 1
        wx.MessageBox(f"Total Errors: {error_count}", "Result")
    except FileNotFoundError:
        wx.MessageBox("Log file not found!", "Error")
btn1 = wx.Button(panel, label="Create Log", pos=(100, 30), size=(150, 30))
btn2 = wx.Button(panel, label="Count Errors", pos=(100, 80), size=(150, 30))
btn1.Bind(wx.EVT_BUTTON, create_log)
btn2.Bind(wx.EVT_BUTTON, count_errors)
frame.Show()
app.MainLoop()
