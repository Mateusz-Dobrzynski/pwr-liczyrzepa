from tkinter import END, Label, StringVar, Text, Tk, filedialog, Button, Entry

from chart_creator import ChartCreator
from price_history import PriceHistory
from PIL import Image, ImageTk
from datetime import datetime
import os

from spreadsheet_saver import SpreadsheetSaver


class GUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.history = None
        self.record_creation_button_visible = False

    def build(self):
        self.root.title("Liczyrzepa")
        self.root.geometry("700x700")
        self.root.config(background="white")
        load_button = Button(
            master=self.root,
            text="Load Price History",
            command=self.read_file_history_from_file,
        )
        row_number = 1
        load_button.grid(row=row_number, column=1)
        row_number += 1

        self.name = StringVar()
        name_label = Label(self.root, text="Name", font=("Liberation Sans", 10, "bold"))
        name_label.grid(row=row_number, column=1)
        row_number += 1
        name_entry = Entry(self.root, textvariable=self.name)
        name_entry.grid(row=row_number, column=1)
        row_number += 1

        self.xpath = StringVar()
        xpath_label = Label(
            self.root, text="Xpath", font=("Liberation Sans", 10, "bold")
        )
        xpath_label.grid(row=row_number, column=1)
        row_number += 1
        xpath_entry = Entry(self.root, textvariable=self.xpath)
        xpath_entry.grid(row=row_number, column=1)
        row_number += 1

        self.url = StringVar()
        url_label = Label(self.root, text="URL", font=("Liberation Sans", 10, "bold"))
        url_label.grid(row=row_number, column=1)
        row_number += 1
        url_entry = Entry(self.root, textvariable=self.url)
        url_entry.grid(row=row_number, column=1)
        row_number += 1

        self.unit = StringVar()
        unit_label = Label(self.root, text="Unit", font=("Liberation Sans", 10, "bold"))
        unit_label.grid(row=row_number, column=1)
        row_number += 1
        unit_entry = Entry(self.root, textvariable=self.unit)
        unit_entry.grid(row=row_number, column=1)
        row_number += 1

        price_history_creation_button = Button(
            master=self.root,
            text="Create new price history",
            command=self.create_new_price_history,
        )
        price_history_creation_button.grid(row=row_number, column=1)
        row_number += 1

        price_history_save_to_json_button = Button(
            master=self.root,
            text="Save to .json",
            command=self.save_to_json,
        )
        price_history_save_to_json_button.grid(row=row_number, column=1)
        row_number += 1

        price_history_to_ods_button = Button(
            master=self.root,
            text="Save to .ods",
            command=self.save_to_spreadsheet,
        )
        price_history_to_ods_button.grid(row=row_number, column=1)
        row_number += 1

        self.error_text = Text(self.root, height=3, width=30)
        self.error_text.insert(END, "")
        self.error_text.configure(state="disabled")
        self.error_text.grid(row=row_number, column=1)
        row_number += 1

        self.root.mainloop()

    def read_file_history_from_file(self) -> None:
        dialog = filedialog.askopenfile(initialdir=".", defaultextension=".json")
        if not dialog:
            return
        try:
            price_history_path = dialog.name
            self.history = PriceHistory(price_history_path)
            self.price_history_path = price_history_path
            if not self.record_creation_button_visible:
                self.show_record_creation_button()
            self.update_price_history_chart()
        except:
            self.display_error("Failed to load price history from file!")

    def show_record_creation_button(self) -> None:
        add_record_button = Button(
            master=self.root,
            text="Add new record",
            command=self.add_new_price_record_and_update_chart,
        )
        add_record_button.grid(row=14, column=1)
        self.record_creation_button_visible = True

    def create_new_price_history(self) -> None:
        if self.url.get() == "" or self.xpath.get() == "":
            self.display_error("URL and Xpath are required!")
            return
        try:
            self.history = PriceHistory()
            self.history.url = self.url.get()
            self.history.xpath = self.xpath.get()
            self.history.name = self.name.get()
            self.history.unit = self.unit.get()
            self.history.create_new_price_record()
            self.update_price_history_chart()
            if not self.record_creation_button_visible:
                self.show_record_creation_button()
        except Exception as e:
            self.display_error(
                "Failed to create price history. Please check your URL and Xpath"
            )

    def save_to_json(self) -> None:
        dialog = filedialog.asksaveasfilename(initialdir=".", defaultextension=".json")
        if not isinstance(self.history, PriceHistory):
            return
        self.history.save_to_file(dialog)

    def save_to_spreadsheet(self) -> None:
        dialog = filedialog.asksaveasfilename(initialdir=".", defaultextension=".ods")
        if not isinstance(self.history, PriceHistory):
            return
        if not dialog.endswith(".ods"):
            dialog += ".ods"
        SpreadsheetSaver().save_history_to_file(self.history, dialog)

    def add_new_price_record_and_update_chart(self) -> None:
        if not isinstance(self.history, PriceHistory):
            return
        self.history.create_new_price_record()
        self.update_price_history_chart()

    def update_price_history_chart(self):
        temp_image_path = str(datetime.timestamp(datetime.now())) + ".png"
        ChartCreator(self.history).save_chart_as_image(temp_image_path)
        self.display_image(temp_image_path)
        os.remove(temp_image_path)

    def display_image(self, graph_path: str) -> None:
        img = Image.open(graph_path)
        img = img.resize((1024, 576))
        img = ImageTk.PhotoImage(img)
        panel = Label(self.root, image=img)
        panel.image = img
        panel.grid(row=15, column=2)

    def display_error(self, error_message: str) -> None:
        self.error_text.configure(state="normal")
        self.error_text.delete("1.0", END)
        self.error_text.insert(END, error_message)
        self.error_text.configure(state="disabled")
