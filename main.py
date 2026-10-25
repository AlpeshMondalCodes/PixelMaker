import os
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from json import load
import theme

pywhatkit_imported = False
kit=None  # Placeholder for pywhatkit module after dynamic import
with open("app.json","r") as f:
    appConfigurations = load(f)

# Set default appearance mode and color theme
ctk.set_appearance_mode(appConfigurations.get("theme","System"))  # Options: "Light", "Dark", "System"

# --- Main Window Initialization ---
root = ctk.CTk()
root.title("PixelMaker")
root.geometry(f"{appConfigurations.get("appWidth",720)}x{appConfigurations.get("appHeight",880)}")
root.minsize(900, 650)
root.configure(fg_color=theme.get_color("bg_main"))

# State variables
selected_file_path = ctk.StringVar(value="")
current_pil_image = None
processed_pil_image = None
preview_photo_image = None
last_width = 0
last_height = 0


# --- Interaction Handlers & Callbacks ---
def browse_file():
    global current_pil_image, processed_pil_image
    path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")]
    )
    if path:
        selected_file_path.set(path)
        try:
            current_pil_image = Image.open(path)
            processed_pil_image = current_pil_image.copy()
            slider.set(1)
            value_entry.delete(0, tk.END)
            value_entry.insert(0, "1")
            show_image_preview(current_pil_image)
            hide_ascii_view()
        except Exception as e:
            print(f"Error opening image: {e}")


def show_image_preview(pil_img):
    global preview_photo_image
    hide_ascii_view()
    
    preview_card.update_idletasks()
    max_w = max(400, preview_card.winfo_width() - 40)
    max_h = max(250, preview_card.winfo_height() - 50)
    
    img_copy = pil_img.copy()
    img_copy.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    
    preview_photo_image = ImageTk.PhotoImage(img_copy)
    preview_image_label.configure(image=preview_photo_image, text="")


def on_window_resize(event):
    global last_width, last_height
    if event.widget == root:
        if event.width != last_width or event.height != last_height:
            last_width = event.width
            last_height = event.height
            if current_pil_image:
                target_img = processed_pil_image if processed_pil_image else current_pil_image
                show_image_preview(target_img)


root.bind("<Configure>", on_window_resize)


def on_slider_change(value):
    val_int = int(value)
    value_entry.delete(0, tk.END)
    value_entry.insert(0, str(val_int))
    if current_pil_image:
        pixelate_action(apply_preview_only=True)


def on_entry_change(event=None):
    try:
        val = int(value_entry.get())
        val = max(1, min(60, val))  # Slider range: 1 to 60
        slider.set(val)
        value_entry.delete(0, tk.END)
        value_entry.insert(0, str(val))
        if current_pil_image:
            pixelate_action(apply_preview_only=True)
    except ValueError:
        value_entry.delete(0, tk.END)
        value_entry.insert(0, str(int(slider.get())))


def show_tips_window():
    """Opens a custom styled modal dialog with detailed usage tips."""
    tips_win = ctk.CTkToplevel(root)
    tips_win.title("PixelMaker Tips & Guide")
    tips_win.geometry("440x360")
    tips_win.resizable(False, False)
    tips_win.configure(fg_color=theme.get_color("bg_main"))
    tips_win.grab_set()

    lbl = ctk.CTkLabel(
        tips_win,
        text="PixelMaker Pro Tips",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color=theme.get_color("text_primary")
    )
    lbl.pack(padx=20, pady=(20, 10), anchor="w")

    tips_text = (
        "• Pixel Density & Resolution:\n"
        "  Increasing density makes the image more pixelated and the ASCII "
        " more clearer, but also larger/wider. Decreasing does the reverse.\n\n"
        "• Best Image Selection:\n"
        "  Use ASCII conversion for symbolic, high-contrast, or simpler "
        "images for maximum clarity and readability.\n\n"
        "• Performance & Aesthetics:\n"
        "  Keep pixel density lower for faster text rendering and a classic "
        "retro aesthetic. (ASCII)"
    )

    tips_box = ctk.CTkTextbox(
        tips_win,
        corner_radius=10,
        fg_color=theme.get_color("bg_inset"),
        text_color=theme.get_color("text_primary"),
        font=ctk.CTkFont(size=13),
        wrap="word"
    )
    tips_box.pack(padx=20, pady=10, fill="both", expand=True)
    tips_box.insert("1.0", tips_text)
    tips_box.configure(state="disabled")

    close_btn = ctk.CTkButton(
        tips_win,
        text="Got it!",
        height=36,
        corner_radius=8,
        fg_color=theme.get_color("accent_primary"),
        hover_color=theme.get_color("accent_primary_hover"),
        text_color="#FFFFFF",
        font=ctk.CTkFont(weight="bold"),
        command=tips_win.destroy
    )
    close_btn.pack(padx=20, pady=(10, 20), fill="x")


def copy_text():
    text = output_textbox.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text)
    
    original_text = copy_btn.cget("text")
    copy_btn.configure(text="Copied!")
    root.after(1500, lambda: copy_btn.configure(text=original_text))


def pixelate_action(apply_preview_only=False):
    global current_pil_image, processed_pil_image
    if not current_pil_image:
        return

    pixel_size = int(slider.get())
    
    if pixel_size <= 1:
        processed_pil_image = current_pil_image.copy()
    else:
        orig_width, orig_height = current_pil_image.size
        small_width = max(1, orig_width // pixel_size)
        small_height = max(1, orig_height // pixel_size)

        # Robust pixelation logic (downscale bilinear, upscale nearest)
        img_small = current_pil_image.resize((small_width, small_height), resample=Image.Resampling.BILINEAR)
        processed_pil_image = img_small.resize((orig_width, orig_height), resample=Image.Resampling.NEAREST)

    if not apply_preview_only:
        processed_pil_image.show()
    
    show_image_preview(processed_pil_image)


def save_action():
    global processed_pil_image
    if not processed_pil_image:
        messagebox.showerror("Error", "No image to save.")
        return
        
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg"), ("All Files", "*.*")]
    )
    if save_path:
        processed_pil_image.save(save_path)
        messagebox.showinfo("Save Successful", f"Image successfully saved to {save_path}")


def ascii_action():
    global current_pil_image
    path = selected_file_path.get()
    if not path or not os.path.exists(path) or not current_pil_image:
        output_textbox.delete("1.0", tk.END)
        output_textbox.insert("1.0", "Please select a valid image file first!")
        show_ascii_view()
        return

    try:
        ascii_art = generate_ascii_from_root()

        output_textbox.delete("1.0", tk.END)
        output_textbox.insert("1.0", ascii_art)
        try:
            os.remove("pywhatkit_asciiart.txt")
        except FileNotFoundError:
            pass
    except Exception as e:
        output_textbox.delete("1.0", tk.END)
        messagebox.showerror("Error", f"Error converting image to ASCII:\n{e}")

    show_ascii_view()


def generate_ascii_from_root():
    global pywhatkit_imported
    if not pywhatkit_imported:
        messagebox.showinfo("ASCII Conversion", "loading Modules after clicking OK button. Take a moment to load the modules. ")
        import pywhatkit as imported_kit
        global kit
        kit = imported_kit
        pywhatkit_imported = True
    # issues : after importing it cannot access the kit variable
    ascii_str = kit.image_to_ascii_art(selected_file_path.get())
            
    return ascii_str


def show_ascii_view():
    preview_image_label.pack_forget()
    card_header.pack(fill="x", padx=15, pady=(10, 5))
    output_textbox.pack(padx=15, pady=(0, 15), fill="both", expand=True)


def hide_ascii_view():
    card_header.pack_forget()
    output_textbox.pack_forget()
    preview_image_label.pack(padx=15, pady=10, fill="both", expand=True)


# --- UI Layout Construction ---

tips_btn = ctk.CTkButton(
    root,
    text="💡 Tips",
    width=75,
    height=30,
    corner_radius=8,
    font=ctk.CTkFont(size=12, weight="bold"),
    fg_color=theme.get_color("accent_muted"),
    hover_color=theme.get_color("accent_muted_hover"),
    text_color="#FFFFFF",
    command=show_tips_window
)
tips_btn.place(relx=0, rely=0, anchor="w",x=40,y=40)


# 1. Header Section
header_frame = ctk.CTkFrame(root, fg_color="transparent")
header_frame.pack(padx=20, pady=(10, 8),anchor="center")

title_label = ctk.CTkLabel(
    header_frame,
    text="PixelMaker",
    font=ctk.CTkFont(family="Helvetica", size=32, weight="bold"),
    text_color=theme.get_color("text_primary")
)
title_label.pack(anchor="center")

subtitle_label = ctk.CTkLabel(
    header_frame,
    text="Image to ASCII",
    font=ctk.CTkFont(family="Helvetica", size=24, weight="normal"),
    text_color=theme.get_color("accent_secondary")
)
subtitle_label.pack(anchor="center", pady=(2, 0))


# 2. File Selector Section
card_file = ctk.CTkFrame(
    root,
    fg_color=theme.get_color("bg_card"),
    corner_radius=14,
    border_width=1,
    border_color=theme.get_color("border")
)
card_file.pack(padx=25, pady=6, fill="x")

file_label = ctk.CTkLabel(
    card_file,
    text="Select Image Source",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color=theme.get_color("text_secondary")
)
file_label.pack(anchor="w", padx=15, pady=(10, 4))

input_container = ctk.CTkFrame(card_file, fg_color="transparent")
input_container.pack(padx=15, pady=(0, 12), fill="x")

path_entry = ctk.CTkEntry(
    input_container,
    textvariable=selected_file_path,
    state="readonly",
    height=36,
    corner_radius=8,
    fg_color=theme.get_color("bg_inset"),
    border_color=theme.get_color("border"),
    text_color=theme.get_color("text_primary")
)
path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

browse_btn = ctk.CTkButton(
    input_container,
    text="Browse...",
    width=90,
    height=36,
    corner_radius=8,
    font=ctk.CTkFont(weight="bold"),
    fg_color=theme.get_color("accent_muted"),
    hover_color=theme.get_color("accent_muted_hover"),
    text_color="#FFFFFF",
    command=browse_file
)
browse_btn.pack(side="right")


# 3. Preview / Output Card (Flexible resizing container)
preview_card = ctk.CTkFrame(
    root,
    fg_color=theme.get_color("bg_card"),
    corner_radius=14,
    border_width=1,
    border_color=theme.get_color("border")
)
preview_card.pack(padx=25, pady=6, fill="both", expand=True)

# Image Preview Label
preview_image_label = ctk.CTkLabel(
    preview_card,
    text="No image loaded.\nSelect an image to preview.",
    font=ctk.CTkFont(size=13),
    text_color=theme.get_color("text_secondary")
)
preview_image_label.pack(padx=15, pady=10, fill="both", expand=True)

# ASCII Header & Copy Button Container (Hidden initially)
card_header = ctk.CTkFrame(preview_card, fg_color="transparent")
out_label = ctk.CTkLabel(
    card_header,
    text="ASCII Output Display",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color=theme.get_color("text_secondary")
)
out_label.pack(side="left")

copy_btn = ctk.CTkButton(
    card_header,
    text="Copy",
    width=70,
    height=28,
    corner_radius=6,
    font=ctk.CTkFont(size=12, weight="bold"),
    fg_color=theme.get_color("accent_muted"),
    hover_color=theme.get_color("accent_muted_hover"),
    text_color="#FFFFFF",
    command=copy_text
)
copy_btn.pack(side="right")

# ASCII Textbox (Hidden initially)
output_textbox = ctk.CTkTextbox(
    preview_card,
    corner_radius=8,
    font=ctk.CTkFont(family="Courier", size=8),
    fg_color=theme.get_color("bg_inset"),
    border_color=theme.get_color("border"),
    text_color=theme.get_color("text_primary"),
    wrap="none"
)

# 5. Action Buttons Section (Bottom - Save & ASCII)
button_container = ctk.CTkFrame(root, fg_color="transparent")
button_container.pack(padx=25, pady=(6, 10), fill="x")
button_container.grid_columnconfigure((0, 1), weight=1, uniform="group1")

controls_container = ctk.CTkFrame(button_container, fg_color="transparent")
controls_container.pack(padx=15, pady=(0, 12), fill="x",side="left", expand=True)

sider_lbl= ctk.CTkLabel(
    controls_container,
    text="Density:",
    font=ctk.CTkFont(size=13, weight="bold"),
    text_color=theme.get_color("text_secondary")
)
sider_lbl.pack(side="left", padx=(0, 10),pady=(4,0))

slider = ctk.CTkSlider(
    controls_container,
    from_=1,
    to=80,
    number_of_steps=79,
    height=20,
    corner_radius=40,
    button_color=theme.get_color("accent_primary"),
    button_hover_color=theme.get_color("accent_primary_hover"),
    progress_color=theme.get_color("accent_primary"),
    fg_color=theme.get_color("border"),
    command=on_slider_change
)
slider.pack(side="left", fill="x", expand=True, padx=(0, 15),pady=(4,0))
slider.set(1)

value_entry = ctk.CTkEntry(
    controls_container,
    width=65,
    height=36,
    corner_radius=8,
    justify="center",
    font=ctk.CTkFont(size=14, weight="bold"),
    fg_color=theme.get_color("bg_inset"),
    border_color=theme.get_color("border"),
    text_color=theme.get_color("text_primary")
)
value_entry.pack(side="right",pady=(4,0))
value_entry.insert(0, "1")
value_entry.bind("<Return>", on_entry_change)
value_entry.bind("<FocusOut>", on_entry_change)


btn_ascii = ctk.CTkButton(
    button_container,
    text="ASCII",
    height=40,
    width=100,
    corner_radius=40,
    font=ctk.CTkFont(size=14, weight="bold"),
    fg_color=theme.get_color("accent_muted"),
    hover_color=theme.get_color("accent_muted_hover"),
    text_color="#FFFFFF",
    command=ascii_action
)
btn_ascii.pack(side="right", padx=(5, 0),fill="y")

btn_save = ctk.CTkButton(
    button_container,
    text="Save",
    height=40,
    width=100,
    corner_radius=40,
    font=ctk.CTkFont(size=14, weight="bold"),
    fg_color=theme.get_color("accent_secondary"),
    hover_color=theme.get_color("accent_secondary_hover"),
    text_color="#121013",
    command=save_action
)
btn_save.pack(side="right", padx=(0, 5),fill="y")


# --- Run Application ---
if __name__ == "__main__":
    root.mainloop()