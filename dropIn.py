import tkinter as tk
from tkinter import filedialog
import pip._vendor.requests  


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    headers = {'authorization': "1105ab38c7e6453cb1bcb31545fe63e4"}
    response = pip._vendor.requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))
    print(response.json())
    #print('Selected:', filename)

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()