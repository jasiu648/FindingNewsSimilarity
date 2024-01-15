import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
class App:

    def __init__(self, root):
        #setting title
        root.title("Article comparer")
        #setting window size
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_262=tk.Text(root)
        GLineEdit_262["borderwidth"] = "1px"
        
        
        GLineEdit_262["fg"] = "#333333"
        #GLineEdit_262["justify"] = "center"
        #GLineEdit_262["text"] = ""
        GLineEdit_262.place(x=130,y=50,width=400,height=500)

        compare_button = tk.Button(root)
        compare_button["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        
        compare_button["fg"] = "#000000"
        compare_button["justify"] = "center"
        compare_button["text"] = "Compare"
        compare_button.place(x=30,y=520,width=70,height=25)
        compare_button["command"] = self.GButton_583_command

        GListBox_534=tk.Listbox(root)
        GListBox_534["borderwidth"] = "1px"
        
        
        GListBox_534["fg"] = "#333333"
        GListBox_534["justify"] = "center"
        GListBox_534.place(x=30,y=380,width=80,height=25)

        GButton_220=tk.Button(root)
        GButton_220["bg"] = "#f0f0f0"
        
        
        GButton_220["fg"] = "#000000"
        GButton_220["justify"] = "center"
        GButton_220["text"] = "Button"
        GButton_220.place(x=460,y=560,width=70,height=25)
        GButton_220["command"] = self.GButton_220_command

        GLineEdit_230=tk.Text(root)
        GLineEdit_230["borderwidth"] = "1px"
        
        
        GLineEdit_230["fg"] = "#333333"
        #GLineEdit_230["justify"] = "left"
        #GLineEdit_230["text"] = ""
        #GLineEdit_230.insert(0,'')
        #GLineEdit_230.icursor(0)
        GLineEdit_230.place(x=570,y=50,width=400,height=500)

        GButton_934=tk.Button(root)
        GButton_934["bg"] = "#f0f0f0"
        GButton_934["fg"] = "#000000"
        GButton_934["justify"] = "center"
        GButton_934["text"] = "Button"
        GButton_934.place(x=900,y=560,width=70,height=25)
        GButton_934["command"] = self.GButton_934_command

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
        label_3["text"] = "Model"
        label_3.place(x=30,y=260,width=70,height=25)

        label_4=tk.Label(root)
        label_4["fg"] = "#333333"
        label_4["justify"] = "left"
        label_4["text"] = "Extractor"
        label_4.place(x=30,y=310,width=70,height=25)

        label_5=tk.Label(root)
        label_5["fg"] = "#333333"
        label_5["justify"] = "left"
        label_5["text"] = "Evaluator"
        label_5.place(x=30,y=360,width=70,height=25)

        import_button1=tk.Button(root)
        import_button1["bg"] = "#f0f0f0"
        import_button1["fg"] = "#000000"
        import_button1["justify"] = "center"
        import_button1["text"] = "Import file"
        import_button1.place(x=130,y=560,width=70,height=25)
        import_button1["command"] = self.GButton_800_command

        import_button2=tk.Button(root)
        import_button2["bg"] = "#f0f0f0"
        import_button2["fg"] = "#000000"
        import_button2["justify"] = "center"
        import_button2["text"] = "Import file"
        import_button2.place(x=570,y=560,width=70,height=25)
        #import_button2["command"] = self.GButton_800_command

        GListBox_191=tk.Listbox(root)
        GListBox_191["borderwidth"] = "1px"
        GListBox_191["fg"] = "#333333"
        GListBox_191["justify"] = "center"
        GListBox_191.place(x=30,y=330,width=80,height=25)

        GListBox_975=tk.Listbox(root)
        GListBox_975["borderwidth"] = "1px"
        GListBox_975["fg"] = "#333333"
        GListBox_975["justify"] = "center"
        #GListBox_975.place(x=30,y=280,width=80,height=25)

        # Create a StringVar to hold the selected item
        selected_model = tk.StringVar()
        selected_extractor = tk.StringVar()
        selected_evaluator = tk.StringVar()

        # Create a Combobox widget
        self.combobox_model = ttk.Combobox(root, textvariable=selected_model)
        self.combobox_model['values'] = ('TD-IDF', 'BERT')  # Set the options
        self.combobox_model.place(x=30,y=280,width=80,height=25)

        # Set a default value (optional)
        self.combobox_model.set('TD_IDF')
        
        # Bind the event handler to the <<ComboboxSelected>> event
        self.combobox_model.bind("<<ComboboxSelected>>", self.on_combobox_selected)

        self.combobox_extractor = ttk.Combobox(root, textvariable=selected_model)


        

    def GButton_583_command(self):
        print("command")


    def GButton_220_command(self):
        print("command")


    def GButton_934_command(self):
        print("command")


    def GButton_800_command(self):
        print("command")

    def on_combobox_selected(self, event):
        # Get the selected item from the combobox
        selected_item = self.combobox_model.get()
        
        
        # Display the selected item in the console (you can modify this part based on your needs)
        print("Selected Item:", selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
