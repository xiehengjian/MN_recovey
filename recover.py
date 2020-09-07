from tkinter import Tk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os

def chosePath():
    origin_path = askopenfilename(title = "选择损坏的备份文件",filetypes = [("MarginNote备份文件", "*.marginbackupall"),])
    #recover_path = asksaveasfilename(title = "请创建或者选择一个保存数据的MarginNote备份文件",filetypes = [("MarginNote3备份文件", "*.marginbackupall"),],defaultextension = ".marginbackupall")
    recover_path=origin_path.split('.')[0].split('(')[0]

    os.rename(origin_path,recover_path)
    return recover_path

def recoverData(recover_path):
    res=os.system('./sqlite3 %s/MarginNotes.sqlite ".recover" | ./sqlite3 %s/recover.db'%(recover_path,recover_path))
    if res == '0':
        os.system("rm %s/MarginNotes.sqlite"%(recover_path))
        os.system("rm %s/MarginNotes.sqlite-shm"%(recover_path))
        os.system("rm %s/MarginNotes.sqlite-wal"%(recover_path))
        os.system("mv %s/recover.db %s/MarginNotes.sqlite"%(recover_path,recover_path))
        recoverd_path="/".join(recover_path.split('/')[:-1])+"/recoverd.marginbackupall"
        os.rename(recover_path,recoverd_path)
    else:
        tkinter.messagebox.showinfo('提示',"恢复失败！")
        exit(0)
     
    
if __name__ == "__main__":
    #
    app = Tk()  #初始化GUI程序
    app.withdraw() #仅显示对话框，隐藏主窗口
    recover_path=chosePath()
    tkinter.messagebox.showinfo('提示',"开始恢复，请稍后")
    recoverData(recover_path)
    tkinter.messagebox.showinfo('提示',"恢复完成！")
    

    