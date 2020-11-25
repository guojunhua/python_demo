# 公众号：优特编程
# 网站： https://www.xuepy.com

import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox
import pyttsx3


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("文本-语音 转换器 - 优特编程")
        self.geometry("300x120")
        self.iconbitmap("favicon.ico")
        self.engine = pyttsx3.init()
        self.file_path = tk.StringVar()
        self.init_ui()


    def init_ui(self):
        self.row1 = tk.LabelFrame(self, text="文本文件")
        self.txt_path = tk.Entry(self.row1, textvariable=self.file_path)
        self.txt_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        
        self.btn_sel = tk.Button(self.row1, text="选择", command=self.select_file)
        self.btn_sel.pack(side=tk.RIGHT, pady=5, padx=5)
        self.row1.pack(fill=tk.X, padx=5, pady=5)
        
        self.btn_convert = tk.Button(self, text="转换为 MP3", command=self.convert_to_mp3)
        self.btn_convert.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)


    def select_file(self):
        txt_file = filedialog.askopenfile(initialdir=".", title="选择文件", filetypes=(('文件文件', '*.txt'),('所有文件', '*.*')))
        if txt_file:
            self.file_path.set(txt_file.name)
    
    
    def convert_to_mp3(self):
        filename = pathlib.Path(self.file_path.get())
        with open(filename, 'r', encoding='utf8') as f:
            self.engine.save_to_file(f.read(), f"{filename.stem}.mp3")
            self.engine.runAndWait()
        msgbox.showinfo("转换结果", "文件转换成功!")
        

if __name__ == "__main__":
    app = Application()
    app.mainloop()
