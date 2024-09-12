import os
import requests
import time

import tkinter as tk
from tkinter import ttk, filedialog, font, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import re

class Downloader(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.maxsize(600,400)
        self.title("Samsung Bios Downloader")
        self.configure(bg="#2C3E50")
        
        
        self.frame = ttk.Frame(self, padding="20")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2C3E50')
        self.style.configure('TLabel', background='#2C3E50', foreground='white')  
        self.style.configure('TButton', background='#2C3E50', foreground='grey', font=("Helvetica", 10)) 
        self.style.configure('TEntry', fieldbackground='#ECF0F1', foreground='black')  
        self.style.configure('TProgressbar', troughcolor='#34495E', background='#3498DB')
        
        # SamsungID Text
        self.professional_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.try_text1 = ttk.Label(self.frame, text="Samsung Id:", font=self.professional_font)
        self.try_text1.grid(row=1, column=0, padx=5, pady=5)

        # Drag URL
        self.file_drop_entry = ttk.Entry(self.frame, width=50)
        self.file_drop_entry.grid(row=1, column=1, padx=5, pady=5)
        self.add_placeholder(self.file_drop_entry, "Drag Your File Here")

        # Save location entry
        self.save_location_entry = ttk.Entry(self.frame, width=50)
        self.save_location_entry.grid(row=2, column=1, padx=5, pady=5)
        self.add_placeholder(self.save_location_entry, "Save Location")

        # Save location button
        self.save_location_button = ttk.Button(self.frame, text="Browse", command=self.browse_save_location)
        self.save_location_button.grid(row=2, column=0, padx=5, pady=5)

        # Download button
        self.download_button = ttk.Button(self.frame, text="Download", command=self.download)
        self.download_button.grid(row=4, column=1, padx=5, pady=5)
        self.download_button["state"] = "disabled"

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.frame, orient='horizontal', mode='determinate', length=300)
        self.progress_bar.grid(row=5, column=1, padx=5, pady=5)

        # Bind drag and drop only to the entry widget
        self.file_drop_entry.drop_target_register(DND_FILES)
        self.file_drop_entry.dnd_bind('<<Drop>>', self.drop_test)

    def add_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.config(foreground='grey')
        entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, placeholder))
        entry.bind("<FocusOut>", lambda event: self.restore_placeholder(event, placeholder))

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)
            event.widget.config(foreground='black')

    def restore_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(foreground='grey')

    def browse_save_location(self):
        save_location = filedialog.askdirectory()
        if save_location:
            self.save_location_entry.delete(0, 'end')
            self.save_location_entry.insert(0, save_location)

    def process_file(self, file_path):
        samsung_hex_value = b'\x53\x45\x43\x57\x55\x50'
        with open(file_path, "rb") as file:
            samsung_content = file.read()
            samsung_index = samsung_content.find(samsung_hex_value)
            if samsung_index != -1:
                samsung_index += 13
                next_bytes = samsung_content[samsung_index:samsung_index + 3]
                samsung_id = next_bytes.decode('ascii')
                self.file_drop_entry.delete(0, 'end')
                self.file_drop_entry.insert(0, samsung_id)
                self.download_button["state"] = "normal"
            else:
                messagebox.showwarning("Samsung ID not found in the file.")
                return

    def download(self):
        save_location = self.save_location_entry.get()
        if not save_location:
            messagebox.showerror("Error", "Save location is empty.")
            return

        samsung_id = self.file_drop_entry.get()
        if not samsung_id:
            messagebox.showerror("Error", "Samsung ID is empty.")
            return

        url = f"http://sbuservice.samsungmobile.com/BUWebServiceProc.asmx/GetContents?platformID={samsung_id}&PartNumber=AAAA"
        max_retries = 10
        retry_delay = 1

        for attempt in range(max_retries):
            try:
                response = requests.get(url, stream=True)

                if response.status_code == 200:
                    content = response.text
                    match = re.search(r'<FilePathName>(.*?)</FilePathName>', content)
                    version = re.search(r'<Version>(.*?)</Version>', content)
                    if match:
                        file = match.group(1)
                    if version:
                        ver = version.group(1)
                        messagebox.showinfo("Version", f"The File Version is: {ver}")

                        for_download = f"http://sbuservice.samsungmobile.com/upload/BIOSUpdateItem/{file}"
                        file_path = os.path.join(save_location, file)
                        print(file_path)

                        if os.path.exists(file_path):
                            file_size = os.path.getsize(file_path)
                            headers = requests.head(for_download).headers
                            expected_size = int(headers.get('Content-Length', 0))

                            if file_size < expected_size:
                                headers = {"Range": f"bytes={file_size}-"}
                                response = requests.get(for_download, headers=headers, stream=True)
                                response.raise_for_status()

                                with open(file_path, "ab") as f:
                                    self.progress_bar["maximum"] = expected_size
                                    self.progress_bar["value"] = file_size
                                    for chunk in response.iter_content(chunk_size=8192):
                                        if chunk:
                                            f.write(chunk)
                                            self.progress_bar["value"] += len(chunk)
                                            self.update_idletasks()
                                messagebox.showinfo("Success", f"File {file} downloaded successfully")
                                break
                            else:
                                messagebox.showinfo("Success", "File already fully downloaded.")
                                break
                        else:
                            response = requests.get(for_download, stream=True)
                            expected_size = int(response.headers.get('Content-Length', 0))
                            self.progress_bar["maximum"] = expected_size
                            self.progress_bar["value"] = 0
                            with open(file_path, 'wb') as f:
                                for chunk in response.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                                        self.progress_bar["value"] += len(chunk)
                                        self.update_idletasks()
                            messagebox.showinfo("Success", f"File {file} downloaded successfully")
                            break
                    else:
                        messagebox.showerror("Missing", "File not found")
                        break
                else:
                    messagebox.showerror("Server Issue", "Failed to connect to server")

            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Error occurred during attempt {attempt + 1}: {e}")

            except IOError as e:
                messagebox.showerror("IOError", f"Error occurred while handling files: {e}")

            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                messagebox.showwarning("Retries", "Maximum retries reached. Exiting...")
                break

    def drop_test(self, event):
        file_path = event.data.strip()
        if file_path.startswith("{") and file_path.endswith("}"):
            file_path = file_path[1:-1]
        self.process_file(file_path)

if __name__ == "__main__":
    app = Downloader()
    app.mainloop()
