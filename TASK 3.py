#UPDATING STUDENTS MARKS
import wx
def display(event):
    output.Clear()
    with open("studentsrecord.txt", "r") as f:
        output.SetValue(f.read())
def update(event):
    roll = roll_txt.GetValue()
    marks = marks_txt.GetValue()
    lines = open("studentsrecord.txt").readlines()
    updated = False
    with open("studentsrecord.txt", "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == roll:
                parts[2] = marks
                updated = True
            f.write(",".join(parts) + "\n")
    if updated:
        wx.MessageBox("Marks Updated")
        display(None)
    else:
        wx.MessageBox("Roll Not Found")
app = wx.App()
frame = wx.Frame(None, title="Student Record", size=(400,400))
panel = wx.Panel(frame)
wx.Button(panel, label="Display Records", pos=(20,20)).Bind(wx.EVT_BUTTON, display)

output = wx.TextCtrl(panel, pos=(20,60), size=(340,150),
                     style=wx.TE_MULTILINE | wx.TE_READONLY)
wx.StaticText(panel, label="Roll No", pos=(20,230))
roll_txt = wx.TextCtrl(panel, pos=(90,230))
wx.StaticText(panel, label="Marks", pos=(20,270))
marks_txt = wx.TextCtrl(panel, pos=(90,270))
wx.Button(panel, label="Update", pos=(150,310)).Bind(wx.EVT_BUTTON, update)
frame.Show()
app.MainLoop()
