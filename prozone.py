import tkinter as tk
from tkinter import messagebox
import pyperclip

class ProZone:
    def __init__(self, root):
        self.root = root
        self.root.title("ProZone - Clipboard Manager")
        self.root.geometry("300x400")

        self.clipboard_list = []

        self.create_widgets()
        self.update_clipboard()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.X)

        self.add_clip_btn = tk.Button(btn_frame, text="Add Clip", command=self.add_clip)
        self.add_clip_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.remove_clip_btn = tk.Button(btn_frame, text="Remove Clip", command=self.remove_clip)
        self.remove_clip_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.paste_clip_btn = tk.Button(btn_frame, text="Paste Clip", command=self.paste_clip)
        self.paste_clip_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def add_clip(self):
        clip_content = pyperclip.paste()
        if clip_content:
            self.clipboard_list.append(clip_content)
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Clipboard is empty!")

    def remove_clip(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            del self.clipboard_list[selected_index[0]]
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "No clip selected!")

    def paste_clip(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            clip_content = self.clipboard_list[selected_index[0]]
            pyperclip.copy(clip_content)
            messagebox.showinfo("Info", "Clip copied to clipboard!")
        else:
            messagebox.showinfo("Info", "No clip selected!")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for clip in self.clipboard_list:
            self.listbox.insert(tk.END, clip)

    def update_clipboard(self):
        self.root.after(1000, self.update_clipboard)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProZone(root)
    root.mainloop()