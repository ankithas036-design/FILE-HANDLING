#MERGING TWO TEXT FILES
import wx
import os
app = wx.App()
frame = wx.Frame(None, title="Merge Files", size=(300, 200))
panel = wx.Panel(frame)
files = {"f1": "", "f2": ""}
def open1(event):
    dlg = wx.FileDialog(panel, "Open File 1",
                        wildcard="Text files (*.txt)|*.txt",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    if dlg.ShowModal() == wx.ID_OK:
        files["f1"] = dlg.GetPath()
        wx.MessageBox("File 1 selected")
    dlg.Destroy()
def open2(event):
    dlg = wx.FileDialog(panel, "Open File 2",
                        wildcard="Text files (*.txt)|*.txt",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    if dlg.ShowModal() == wx.ID_OK:
        files["f2"] = dlg.GetPath()
        wx.MessageBox("File 2 selected")
    dlg.Destroy()
def merge(event):
    if files["f1"] == "" or files["f2"] == "":
        wx.MessageBox("Please select both files first")
        return
    dlg = wx.FileDialog(panel, "Save Merged File",
                        wildcard="Text files (*.txt)|*.txt",
                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
    if dlg.ShowModal() == wx.ID_OK:
        out = dlg.GetPath()
        with open(files["f1"], "r") as a, \
             open(files["f2"], "r") as b, \
             open(out, "w") as c:
            c.write(a.read())
            c.write("\n")
            c.write(b.read())
        wx.MessageBox("Merged Successfully")
        os.startfile(out)
    dlg.Destroy()
b1 = wx.Button(panel, label="File 1", pos=(100, 20))
b2 = wx.Button(panel, label="File 2", pos=(100, 60))
b3 = wx.Button(panel, label="Merge",  pos=(100, 100))
b1.Bind(wx.EVT_BUTTON, open1)
b2.Bind(wx.EVT_BUTTON, open2)
b3.Bind(wx.EVT_BUTTON, merge)
frame.Show()
app.MainLoop()
