# Video Processing Tool | ClipCraft

A user-friendly GUI tool for batch video processing. This tool allows users to perform various tasks such as reducing resolution, changing bitrate, compressing videos, and more. It supports both individual file processing and processing multiple files within a folder.

## Requirements

Before running this project, you need the following:

1. **Python 3.6+**  
   Ensure that Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **PyInstaller**  
   PyInstaller is used to convert this Python script into an executable `.exe` file. To install it, run:
   ```bash
   pip install pyinstaller

3. **FFmpeg**  
   FFmpeg is a powerful multimedia framework used for video encoding, decoding, and processing. This project relies on FFmpeg to process videos.

## Assumptions

* It is assumed that the user already has a basic understanding of how to run an executable file on their operating system.
* The user should be able to choose a file or folder containing videos to process.
* The user is familiar with selecting different video processing tasks (e.g., reduce resolution, lower bitrate, etc.).


# FFmpeg Installation
=====================================

### Step 1: Download FFmpeg

If you do not have FFmpeg installed on your system, follow these steps:

* Download FFmpeg from the official website: [FFmpeg Downloads](https://www.ffmpeg.org/download.html)
* Select the appropriate version based on your operating system.

### Step 2: Extract and Store FFmpeg

1. After downloading, extract the contents of the archive to a folder.

    Example: Extract the files to `C:\ffmpeg`.

2. Inside the `ffmpeg` folder, you should see a `bin` folder containing `ffmpeg.exe`.

### Step 3: Add FFmpeg to the System's Path

* Copy the full path to the `bin` folder. For example:
    ```
    C:\ffmpeg\bin
    ```
* Open the Start menu and search for Environment Variables. Select Edit the system environment variables.

* In the System Properties window, click on the Environment Variables button.

* In the Environment Variables window, under System variables, scroll and select the Path variable, then click Edit.

* In the Edit Environment Variable window, click New and paste the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).

* Click OK to save the changes.

### Step 4: Verify FFmpeg Installation

To verify if FFmpeg is correctly installed and accessible via the command line, open the command prompt (cmd) and type:
```bash
ffmpeg -version
```
You should see FFmpeg version details if the installation was successful.

# How This Project Works
==========================

This video processing tool allows users to:

### Choose a File or Folder

* Select a single video file or an entire folder containing multiple videos.

### Select a Task

Choose from several video processing tasks, such as:

* Reduce Resolution
* Reduce Bitrate
* Use Constant Rate Factor (CRF)
* Change Codec to H.265
* Lower Frame Rate
* Remove Audio
* Maximum Compression

### Process Videos

Once the task is selected, the tool processes the videos and saves the output to the specified location.

## Features

* Batch Processing: Supports processing multiple videos at once when a folder is selected.
* Progress Tracking: Shows progress bars for each file being processed.
* Task Flexibility: Choose from multiple video processing tasks, such as reducing resolution, bitrate, or frame rate.
* Easy to Use: GUI-based tool with a simple interface.

## Workflow

1. The user selects a file or folder.
2. The user chooses the processing task (e.g., reduce resolution, remove audio).
3. The program processes the videos and shows a progress bar for each file.
4. Once processing is complete, the output files are saved in a new folder named according to the selected task.

# Usage Instructions
=====================

## Running the Executable

* After downloading or building the executable `.exe`, double-click it to run the application. The interface will allow you to select a file or folder and choose the desired processing task.
* You can also download the exe from [Here]() it is already built from the same source code.

### Select File/Folder

Click the "Select File" or "Select Folder" button to choose the video file or folder you want to process.

### Select Task

Choose one of the available tasks (e.g., "Reduce Resolution", "Remove Audio", etc.).

### Start Processing

After selecting the task, the processing will begin, and you will see a progress bar indicating the current progress for each video file.

# Troubleshooting
==================

* FFmpeg not found: If the program cannot find FFmpeg, ensure that the FFmpeg folder path is added to your system's environment variables.
* Windows Console Window: If a console window appears when running the application, make sure to use the `--windowed` flag while building the executable with PyInstaller. This will prevent the console from opening for GUI applications.

# License
==========

This project is licensed under the MIT License - see the LICENSE file for details.

For any further questions or issues, feel free to open an issue on the GitHub repository.


### Key Sections in the README:
1. **Requirements**: Lists the necessary dependencies for the project.
2. **Assumptions**: Assumptions about the user's prior knowledge.
3. **FFmpeg Installation**: A step-by-step guide for downloading, installing, and configuring FFmpeg on the system.
4. **How the Project Works**: Overview of the project's functionality, tasks, and features.
5. **Usage Instructions**: Clear instructions on how to use the tool.
6. **Troubleshooting**: Solutions to common issues.

