import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from visualization.Visualizer import *
from data_access.DataProvider import *
from pipelines import *
class App:

    def __init__(self, root):
        
        self.factory = PipelineFactory()
        
        
        # Window -------------------------------------------------------------------------------------------
        root.title("Article comparer")
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        # Articles -------------------------------------------------------------------------------------------
        self.article_1 = tk.Text(root)
        self.article_1["borderwidth"] = "1px"
        self.article_1["fg"] = "#333333"
        self.article_1.place(x=130,y=50,width=400,height=500)

        self.article_2 = tk.Text(root)
        self.article_2["borderwidth"] = "1px"
        self.article_2["fg"] = "#333333"
        self.article_2.place(x=570,y=50,width=400,height=500)


        #Buttons -------------------------------------------------------------------------------------------
        compare_button = tk.Button(root)
        compare_button["bg"] = "#f0f0f0"
        compare_button["fg"] = "#000000"
        compare_button["justify"] = "center"
        compare_button["text"] = "Compare"
        compare_button.place(x=30,y=520,width=70,height=25)
        compare_button["command"] = self.compare_command

        url_button1=tk.Button(root)
        url_button1["bg"] = "#f0f0f0"
        url_button1["fg"] = "#000000"
        url_button1["justify"] = "center"
        url_button1["text"] = "Paste Url"
        url_button1.place(x=210,y=560,width=70,height=25)
        url_button1["command"] = self.open_input1_window
        
        self.url1 = tk.StringVar()
        
        url_button2=tk.Button(root)
        url_button2["bg"] = "#f0f0f0"
        url_button2["fg"] = "#000000"
        url_button2["justify"] = "center"
        url_button2["text"] = "Paste Url"
        url_button2.place(x=650,y=560,width=70,height=25)
        url_button2["command"] = self.open_input2_window

        self.url2 = tk.StringVar()

        import_button1=tk.Button(root)
        import_button1["bg"] = "#f0f0f0"
        import_button1["fg"] = "#000000"
        import_button1["justify"] = "center"
        import_button1["text"] = "Import file"
        import_button1.place(x=130,y=560,width=70,height=25)
        import_button1["command"] = self.import_file1

        import_button2=tk.Button(root)
        import_button2["bg"] = "#f0f0f0"
        import_button2["fg"] = "#000000"
        import_button2["justify"] = "center"
        import_button2["text"] = "Import file"
        import_button2.place(x=570,y=560,width=70,height=25)
        import_button2["command"] = self.import_file2

        # Lables -------------------------------------------------------------------------------------------------------

        label_1=tk.Label(root)
        label_1["fg"] = "#333333"
        label_1["justify"] = "center"
        label_1["text"] = "Article 1"
        label_1.place(x=290,y=20,width=70,height=25)

        label_2=tk.Label(root)
        label_2["fg"] = "#333333"
        label_2["justify"] = "center"
        label_2["text"] = "Article 2"
        label_2.place(x=740,y=20,width=70,height=25)

        label_3=tk.Label(root)
        label_3["fg"] = "#333333"
        label_3["justify"] = "left"
        label_3["text"] = "Language"
        label_3.place(x=30,y=210,width=80,height=25)

        label_4=tk.Label(root)
        label_4["fg"] = "#333333"
        label_4["justify"] = "left"
        label_4["text"] = "Preprocessing"
        label_4.place(x=30,y=260,width=80,height=25)

        label_5=tk.Label(root)
        label_5["fg"] = "#333333"
        label_5["justify"] = "left"
        label_5["text"] = "Nmin"
        label_5.place(x=30,y=310,width=80,height=25)

        label_5=tk.Label(root)
        label_5["fg"] = "#333333"
        label_5["justify"] = "left"
        label_5["text"] = "Nmax"
        label_5.place(x=30,y=360,width=80,height=25)

        
        #Options ----------------------------------------------
        self.text_Nmin=tk.Text(root)
        self.text_Nmin["borderwidth"] = "1px"
        self.text_Nmin["fg"] = "#333333"
        self.text_Nmin.place(x=30,y=330,width=80,height=25)
        self.text_Nmin.insert(tk.END, 2)

        self.text_Nmax=tk.Text(root)
        self.text_Nmax["borderwidth"] = "1px"
        self.text_Nmax["fg"] = "#333333"
        self.text_Nmax.place(x=30,y=380,width=80,height=25)
        self.text_Nmax.insert(tk.END, 4)

        # Create a StringVar to hold the selected item
        self.selected_lang = tk.StringVar()
        self.selected_prep = tk.StringVar()
        self.selected_lang.initialize('PL')
        self.selected_prep.initialize('Yes')
        self.selected_Nmin = 2
        self.selected_Nmax = 4

        # Create a Combobox widget
        self.combobox_lang = ttk.Combobox(root, textvariable = self.selected_lang)
        
        self.combobox_lang['values'] = ('PL', 'EN','SL','HR')  # Set the options
        self.combobox_lang.place(x=30,y=235,width=80,height=25)
        #self.combobox_lang.current('PL')
        #self.combobox_lang.bind("<<ComboboxSelected>>", self.language_selected)
        self.combobox_lang.current(0)

        self.combobox_prep = ttk.Combobox(root, textvariable = self.selected_prep)
        
        self.combobox_prep['values'] = ('Yes','No')  # Set the options
        self.combobox_prep.place(x=30,y=285,width=80,height=25)
        self.combobox_prep.set('Yes')
        #self.combobox_prep.bind("<<ComboboxSelected>>", self.preprocessing_selected)


    def compare_command(self):

        text1 = self.article_1.get("1.0",'end-1c')
        text2 = self.article_2.get("1.0",'end-1c')

        if text1 == "" or text2 == "":
            messagebox.showerror("Invalid Input", "Both texts must be provided")
            return
        
        try:
            Nmin = int(self.text_Nmin.get("1.0",'end-1c'))
        except ValueError:
            messagebox.showerror("Invalid Input", "Provide valid integer value for Nmin")

        try:
            Nmax = int(self.text_Nmax.get("1.0",'end-1c'))
        except ValueError:
            messagebox.showerror("Invalid Input", "Provide valid integer value for Nmax")

        if Nmax < Nmin:
            messagebox.showerror("Invalid Input", "Nmin must be less or equal to Nmax")

        #self.plot()

        fac = PipelineFactory()
        pipe = fac.CreatePipeline(self.selected_lang.get())

        res = pipe.ProcessPipeline([[text1,text2]], Nmin, Nmax)  

        message = f"Lexical Similarity: {res[0].tfidf_result}\nSemantic Similarity: {res[0].embedding_result}\nNER Similarity: {res[0].ner_result}"
        messagebox.showinfo('Results', message)
        

    def present_results(self):
        child_window = tk.Toplevel(root)
        child_window.title("Results")

        # Add widgets or content to the child window
        label = tk.Label(child_window, text="This is the child window.")
        label.pack(padx=10, pady=10)

        close_button = tk.Button(child_window, text="Close", command=child_window.destroy)
        close_button.pack(pady=10)

    def import_file1(self):
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt")]
        )
        if not file_path:
            return
        self.article_1.delete(1.0, tk.END)
        if file_path.lower().endswith('.txt'):
            with open(file_path, 'r') as file:
                self.article_1.insert(tk.END, file.read())
        elif file_path.lower().endswith('.pdf'):
            self.article_1.insert(tk.END, load_text(file_path))


    def import_file2(self):
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt")]
        )
        if not file_path:
            return
        self.article_2.delete(1.0, tk.END)
        if file_path.lower().endswith('.txt'):
            with open(file_path, 'r') as file:
                self.article_2.insert(tk.END, file.read())
        elif file_path.lower().endswith('.pdf'):
            self.article_2.insert(tk.END, load_text(file_path))

        self.article_2.insert(tk.END, load_text(file_path))

    def open_input1_window(self):
        self.url1 = simpledialog.askstring("Paste Url", "Enter Url:")
        
        if self.article_1.get("1.0",'end-1c') == "":
            self.article_1.delete(1.0, tk.END)
        
        self.article_1.insert(tk.END, load_url(url = self.url1))
        
    def open_input2_window(self):
        self.url2 = simpledialog.askstring("Paste Url", "Enter Url:")
        
        if self.article_2.get("1.0",'end-1c') == "":
            self.article_2.delete(1.0, tk.END)
            
        self.article_2.insert(tk.END, load_url(self.url2))

    def plot(self):
         # Create a new window for the plots
        plot_window = tk.Toplevel(root)
        plot_window.title("Plot Window")

        # Create a Figure and three subplots in the new window
        x = np.linspace(0, 2 * np.pi, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)
        y3 = np.tan(x)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
        ax1.plot(x, y1, label='Sin Function')
        ax2.plot(x, y2, label='Cos Function')
        ax3.plot(x, y3, label='Tan Function')

        ax1.set_title("Sine Function")
        ax2.set_title("Cosine Function")
        ax3.set_title("Tangent Function")

        #vs = Visualizer()
        #rd = vs.generate_wordcloud(self.article_1.get("1.0",'end-1c'))
        # Embed the plots in the Tkinter window
        
        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

        # Create a "Close" button in the new window
        close_button = ttk.Button(plot_window, text="Close", command=plot_window.destroy)
        close_button.pack(pady=10)




def load_text(path):
    dp = DataFromPdf()
    return dp.get_article_text(path)

def load_url(url):
    dp = DataFromUrl()
    return dp.get_article_text(url)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
