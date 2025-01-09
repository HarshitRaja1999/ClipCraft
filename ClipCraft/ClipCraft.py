import os
import tkinter as tk
from tkinter import filedialog, ttk
import subprocess
import threading

def select_file():
    path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov")])
    if path:
        selected_path.set(path)

def select_folder():
    path = filedialog.askdirectory()
    if path:
        selected_path.set(path)

def start_processing(option):
    if not selected_path.get():
        tk.messagebox.showerror("Error", "Please select a file or folder.")
        return

    # Disable all buttons
    disable_buttons()

    input_path = selected_path.get()

    # Determine if the selection is a file or folder
    if os.path.isfile(input_path):  # Single file selected
        output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")])
        if not output_file:
            enable_buttons()
            return
        add_progress_tile(input_path, option, output_file)
    elif os.path.isdir(input_path):  # Folder selected
        output_folder_name = os.path.basename(input_path) + f" {option}"
        output_folder_path = os.path.join(os.path.dirname(input_path), output_folder_name)

        # Create output folder
        os.makedirs(output_folder_path, exist_ok=True)

        # Process each video in the folder
        for file_name in os.listdir(input_path):
            if file_name.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
                input_file = os.path.join(input_path, file_name)
                output_file = os.path.join(output_folder_path, file_name)
                add_progress_tile(input_file, option, output_file)
    else:
        tk.messagebox.showerror("Error", "Invalid selection. Please select a valid file or folder.")
        enable_buttons()

def add_progress_tile(input_file, option, output_file):
    # Create a frame for each task (tile)
    tile_frame = tk.Frame(scrollable_frame, borderwidth=1, relief="solid", padx=10, pady=5)
    tile_frame.pack(fill="x", pady=5)

    # File name label
    file_label = tk.Label(tile_frame, text=f"File: {os.path.basename(input_file)}", font=("Arial", 10), anchor="w")
    file_label.pack(fill="x", pady=2)

    # Task label
    task_label = tk.Label(tile_frame, text=f"Task: {option}", font=("Arial", 9, "italic"), anchor="w")
    task_label.pack(fill="x", pady=2)

    # Progress bar
    progress_bar = ttk.Progressbar(tile_frame, length=300, mode="determinate", maximum=100)
    progress_bar.pack(pady=5)

    # Status label
    status_label = tk.Label(tile_frame, text="Queued...", font=("Arial", 9), anchor="w", fg="blue")
    status_label.pack(fill="x")

    # Start the processing in a new thread
    threading.Thread(
        target=run_ffmpeg,
        args=(option, input_file, output_file, progress_bar, status_label, tile_frame)
    ).start()

def run_ffmpeg(option, input_file, output_file, progress_bar, status_label, tile_frame):
    # Define ffmpeg commands for each option
    commands = {
        "Reduce Resolution": [
            "ffmpeg", "-i", input_file, "-vf", "scale=1280:720", "-c:v", "libx264", "-crf", "23", "-preset", "medium",
            "-c:a", "aac", "-b:a", "128k", output_file
        ],
        "Reduce Bitrate": [
            "ffmpeg", "-i", input_file, "-b:v", "1000k", "-c:v", "libx264", "-preset", "medium",
            "-c:a", "aac", "-b:a", "128k", output_file
        ],
        "Use Constant Rate Factor (CRF)": [
            "ffmpeg", "-i", input_file, "-c:v", "libx264", "-crf", "28", "-preset", "slow",
            "-c:a", "aac", "-b:a", "128k", output_file
        ],
        "Change Codec to H.265": [
            "ffmpeg", "-i", input_file, "-c:v", "libx265", "-crf", "28", "-preset", "medium",
            "-c:a", "aac", "-b:a", "128k", output_file
        ],
        "Lower Frame Rate": [
            "ffmpeg", "-i", input_file, "-r", "24", "-c:v", "libx264", "-crf", "23", "-preset", "medium",
            "-c:a", "aac", "-b:a", "128k", output_file
        ],
        "Remove Audio": [
            "ffmpeg", "-i", input_file, "-an", "-c:v", "libx264", "-crf", "23", "-preset", "medium", output_file
        ],
        "Maximum Compression": [
            "ffmpeg", "-i", input_file, "-c:v", "libx265", "-crf", "30", "-preset", "slower", "-c:a", "aac", "-b:a", "64k",
            output_file
        ],
    }

    command = commands.get(option)

    try:
        status_label.config(text="Processing...", fg="orange")
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        # Simulate progress bar updates
        for line in process.stdout:
            if "frame=" in line:
                progress_bar.step(1)
                root.update_idletasks()

        process.wait()  # Wait for the process to complete
        if process.returncode == 0:
            status_label.config(text="Processing Complete!", fg="green")
            progress_bar["value"] = 100
        else:
            status_label.config(text="Processing Failed!", fg="red")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")
    finally:
        # Remove tile after process completes
        tile_frame.after(2000, tile_frame.destroy)
        enable_buttons()


# Disable all buttons
def disable_buttons():
    for button in action_buttons:
        button.config(state="disabled")

# Enable all buttons
def enable_buttons():
    for button in action_buttons:
        button.config(state="normal")

# GUI setup
root = tk.Tk()
root.title("Batch Video Processing Tool")
root.geometry("500x700")
root.resizable(False, False)

# Selected path display
selected_path = tk.StringVar()
progress_panel_visible = tk.BooleanVar(value=False)

tk.Label(root, text="Select a file or folder containing videos:").pack(pady=10)
tk.Entry(root, textvariable=selected_path, width=50, state="readonly").pack(pady=5)

# Buttons to select file or folder
button_frame = tk.Frame(root)
button_frame.pack(pady=5)
file_button = tk.Button(button_frame, text="Select File", command=select_file, width=15)
file_button.pack(side="left", padx=10)
folder_button = tk.Button(button_frame, text="Select Folder", command=select_folder, width=15)
folder_button.pack(side="right", padx=10)

# Compression options
tk.Label(root, text="Choose a compression method:").pack(pady=10)

options = [
    "Reduce Resolution",
    "Reduce Bitrate",
    "Use Constant Rate Factor (CRF)",
    "Change Codec to H.265",
    "Lower Frame Rate",
    "Remove Audio",
    "Maximum Compression",
]

# Add buttons to a list for easy access to disable/enable them
action_buttons = []
for option in options:
    btn = tk.Button(root, text=option, command=lambda opt=option: start_processing(opt), width=25)
    btn.pack(pady=5)
    action_buttons.append(btn)


scrollable_canvas = tk.Canvas(root)
scrollable_canvas.pack(side="left", fill="both", expand=True, pady=10)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=scrollable_canvas.yview)
scrollbar.pack(side="right", fill="y")

scrollable_frame = tk.Frame(scrollable_canvas)
scrollable_frame.bind("<Configure>", lambda e: scrollable_canvas.configure(scrollregion=scrollable_canvas.bbox("all")))
scrollable_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollable_canvas.configure(yscrollcommand=scrollbar.set)

root.mainloop()
