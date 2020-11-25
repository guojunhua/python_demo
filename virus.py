from covid import Covid
import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("新冠肺炎全球数据")
        self.geometry("1080x800")
        self.data = Covid(source="worldometers").get_data()
        self.init_widget()
        self.binding_data()

    def init_widget(self):
        self.frame = tk.Frame(self)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.tree = ttk.Treeview(self.frame)
        self.tree.pack(expand=True, fill=tk.BOTH)

    def binding_data(self):
        self.tree['columns'] = ("1", "2", "3", "4", "5")
        self.tree['show'] = "headings"
        self.tree.column("1", width=90, anchor='w')
        self.tree.column("2", width=40, anchor='e')
        self.tree.column("3", width=40, anchor='e')
        self.tree.column("4", width=40, anchor='e')
        self.tree.column("5", width=40, anchor='e')

        self.tree.heading("1", text="国家/地区", anchor="w")
        self.tree.heading("2", text="当前", anchor="e")
        self.tree.heading("3", text="死亡", anchor="e")
        self.tree.heading("4", text="康复", anchor="e")
        self.tree.heading("5", text="累计确诊", anchor="e")

        for item in self.data:
            self.tree.insert("", 'end', text="L1", values=(
                item.get('country'),
                item.get('active'),
                item.get('deaths'),
                item.get('recovered'),
                item.get('confirmed')))


if __name__ == "__main__":
    app = App()
    app.mainloop()
