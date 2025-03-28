import customtkinter as ctk
from window import Window

class App:
    def __init__(self):
        pass
    def run(self):
        self.root = ctk.CTk()
        self.root.title('Menu')

        c = ctk.StringVar()
        g = ctk.StringVar()
        x = ctk.StringVar()
        y = ctk.StringVar()
        w = ctk.StringVar()
        h = ctk.StringVar()
        m = ctk.StringVar()

        entities_nbr = ctk.CTkLabel(self.root, text="number of entities : ")
        entities_nbr.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entities_entry = ctk.CTkEntry(self.root, textvariable=c)
        entities_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        gg = ctk.CTkLabel(self.root, text="duration of a generation : ")
        gg.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ge = ctk.CTkEntry(self.root, textvariable=g)
        ge.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        z = ctk.CTkLabel(self.root, text="FOOD AREA (max: (900, 900)): ")
        z.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        xx = ctk.CTkLabel(self.root, text="x: ")
        xx.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        xe = ctk.CTkEntry(self.root, textvariable=x)
        xe.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        yy = ctk.CTkLabel(self.root, text="y: ")
        yy.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        ye = ctk.CTkEntry(self.root, textvariable=y)
        ye.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        ww = ctk.CTkLabel(self.root, text="width : ")
        ww.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        we = ctk.CTkEntry(self.root, textvariable=w)
        we.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        hh = ctk.CTkLabel(self.root, text="height : ")
        hh.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        he = ctk.CTkEntry(self.root, textvariable=h)
        he.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        mm = ctk.CTkLabel(self.root, text="mutation /1000: ")
        mm.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        me = ctk.CTkEntry(self.root, textvariable=m)
        me.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        def get():
            window = Window(c, g, x, y, w, h, m)
            window.main()

        submit = ctk.CTkButton(self.root, text="Submit", command=get)
        submit.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
