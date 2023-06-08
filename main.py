import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
root = ctk.CTk()
root.iconbitmap("")
# Title
root.title("BMI Calculator")
# Geometry
root.geometry("500x300")
# User will not be able to resize
root.resizable(False, False)
# Entry Box
weight_entry_box = ctk.CTkEntry(
    root, width=150, placeholder_text="Weight (Kilogram)", border_width=0)
weight_entry_box.place(x=20, y=40)
heigh_entry_box = ctk.CTkEntry(
    root, placeholder_text="Heigh (Meter)", width=150, border_width=0)
heigh_entry_box.place(x=20, y=80)


# calc call backfunction to calculate bmi


def calc():
    try:
        height = float(heigh_entry_box.get())
        weight = float(weight_entry_box.get())
        if height and weight:
            bmi = round(weight/(height**2), 2)
            bmi_label = ctk.CTkLabel(
                root, text="")
            bmi_label.place(x=20, y=200)
            if bmi < 18.5:
                # print("Underweight")
                bmi_label.destroy()
                bmi_label = ctk.CTkLabel(
                    root, text=f"Your BMI Index is {bmi}, Underweight")
                bmi_label.place(x=20, y=200)
            elif bmi >= 18.5 and bmi <= 24.9:
                # print("Normal")
                bmi_label.destroy()
                bmi_label = ctk.CTkLabel(
                    root, text=f"Your BMI Index is {bmi}, Normal")
                bmi_label.place(x=20, y=200)
            else:
                # print("Overweight")
                bmi_label.destroy()
                bmi_label = ctk.CTkLabel(
                    root, text=f"Your BMI Index is {bmi}, Overweight")
                bmi_label.place(x=20, y=200)
        else:
            messagebox.showerror("Required", "Both input fields are required")
    except:
        messagebox.showerror("Invalid Data", "Provide Valid Data")
        weight_entry_box.delete(0, tk.END)
        heigh_entry_box.delete(0, tk.END)
# reset button callback function


def reset():
    weight_entry_box.delete(0, tk.END)
    heigh_entry_box.delete(0, tk.END)


# Calculate BMI Button
calculate_button = ctk.CTkButton(
    root, text="Calculate BMI", width=150, fg_color="SkyBlue", text_color="black", hover_color="white", border_width=0, command=calc)
calculate_button.place(x=20, y=120)
# Reset all Button
reset_button = ctk.CTkButton(root, text="Reset All", width=150, fg_color="SkyBlue",
                             text_color="black", hover_color="white", border_width=0, command=reset)
reset_button.place(x=20, y=160)
# bmi image
image_bmi = tk.PhotoImage(file="bmi.png")
image_label = tk.Label(image=image_bmi)
image_label.place(x=300, y=30)
root.mainloop()
