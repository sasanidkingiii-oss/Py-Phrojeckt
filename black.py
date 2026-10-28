from tkinter import *
from tkinter import filedialog, messagebox




def black():



    win = Tk()
    win.title("Note Pad")
    win.geometry("700x500")
    win.config(bg="#202020")

    def new_file():
        text_box.delete("1.0", END)


    def setting():
        win = Tk()
        win.title("Setting")
        win.geometry("700x500")
        win.config(bg="#202020")

        menu_bar = Frame(
            win,
            bg="#1F1F1F",
            height=30
        )

        menu_bar.pack(
            side="top",
            fill="x"
        )

        Button(
            menu_bar,
            text="File",
            fg="#FFFFFF",
            command=open_file,
            bg="#1F1F1F",
            bd=0
        ).pack(
            side="left",
            padx=8
        )

        Button(
            menu_bar,
            text="Edit",
            fg="#FFFFFF",
            command=copy_text,
            bg="#1F1F1F",
            bd=0
        ).pack(
            side="left",
            padx=8
        )

        Button(
            menu_bar,
            text="View",
            fg="#FFFFFF",
            bg="#1F1F1F",
            bd=0
        ).pack(
            side="left",
            padx=8
        )


    def open_file():
        file = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file:
            text_box.delete("1.0", END)

            with open(file, "r", encoding="utf-8") as f:
                text_box.insert("1.0", f.read())


    def save_file():
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(text_box.get("1.0", END))


    def cut_text():
        text_box.event_generate("<<Cut>>")


    def copy_text():
        text_box.event_generate("<<Copy>>")


    def undo():
        try:
            text_box.edit_undo()
        except TclError:
            pass


    def redo():
        try:
            text_box.edit_redo()
        except TclError:
            pass


    def find_text():

        search_window = Toplevel(win)
        search_window.title("Find")
        search_window.geometry("300x100")

        entry = Entry(search_window)
        entry.pack(pady=10)

        def search():

            text_box.tag_remove("found", "1.0", END)

            word = entry.get()

            if word:

                start = "1.0"

                while True:

                    start = text_box.search(
                        word,
                        start,
                        stopindex=END
                    )

                    if not start:
                        break

                    end = f"{start}+{len(word)}c"

                    text_box.tag_add(
                        "found",
                        start,
                        end
                    )

                    start = end

                text_box.tag_config(
                    "found",
                    background="yellow"
                )

        Button(
            search_window,
            text="Find",
            command=search
        ).pack()





    menu_bar = Frame(
        win,
        bg="#1F1F1F",
        height=30
    )

    menu_bar.pack(
        side="top",
        fill="x"
    )

    Button(
        menu_bar,
        text="File",
        fg="#FFFFFF",
        command=open_file,
        bg="#1F1F1F",
        bd=0
    ).pack(
        side="left",
        padx=8
    )

    Button(
        menu_bar,
        text="Edit",
        fg="#FFFFFF",
        command=copy_text,
        bg="#1F1F1F",
        bd=0
    ).pack(
        side="left",
        padx=8
    )

    Button(
        menu_bar,
        text="View",
        fg="#FFFFFF",
        bg="#1F1F1F",
        bd=0
    ).pack(
        side="left",
        padx=8
    )

    Button(
        menu_bar,
        text="About",
        command=lambda: messagebox.showinfo(
            "About",
            "این نوت پد من هست"
        ),
        bg="#1F1F1F",
        fg="#FFFFFF",
        bd=0
    ).pack(
        side="left",
        padx=8
    )
    Button(
        menu_bar,
        text="setting",
        bg="#1F1F1F",
        fg="#FFFFFF",
        command=setting,
        bd=0
    ).pack(
        side="left",
        padx=8
    )


    # =========================
    # Tool Bar
    # =========================

    toolbar = Frame(
        win,
        bg="#181818",
        height=35
    )

    toolbar.pack(
        side="top",
        fill="x"
    )


    Button(
        toolbar,
        text="📄",
        command=new_file,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    Button(
        toolbar,
        text="📂",
        command=open_file,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    Button(
        toolbar,
        text="💾",
        command=save_file,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    Button(
        toolbar,
        text="✂",
        command=cut_text,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    Button(
        toolbar,
        text="📋",
        command=copy_text,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    Button(
        toolbar,
        text="↩",
        command=undo,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    Button(
        toolbar,
        text="↪",
        command=redo,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    Button(
        toolbar,
        text="🔍",
        command=find_text,
        font=("Arial", 14),
        bg="#181818",
        fg="#FFFFFF",
        bd=0
    ).pack(side="left")


    # =========================
    # Text Box
    # =========================

    text_box = Text(
        win,
        font=("Arial", 12),
        bg="#202020",
        fg="#FFFFFF",
        undo=True
    )

    text_box.pack(
        fill="both",
        expand=True
    )

    win.mainloop()

