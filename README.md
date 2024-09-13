# Transcribe Subtitles Project

This project extracts audio from video files, transcribes it, and generates subtitles in different languages. Follow the steps below to set up your environment and run the script.

## Prerequisites

- Python 3.11 or later
- FFmpeg

## Setup Instructions

1. **Create a virtual environment:**

   `python -m venv .venv`

2. **Activate the virtual environment:**

   - For Windows:  
     `.\.venv\Scripts\activate`
   
   - For macOS/Linux:  
     `source .venv/bin/activate`

3. **Install required packages:**

   `pip install moviepy git+https://github.com/openai/whisper.git googletrans==4.0.0-rc1 pysrt`

4. **Install `deep-translator`:**

   `pip install deep-translator`

5. **Install `ffmpeg-python`:**

   `pip install ffmpeg-python`

6. **Uninstall the existing `numpy` package:**

   `pip uninstall numpy`

7. **Install the compatible version of `numpy`:**

   `pip install numpy==2.0.0`

8. **Reinstall `moviepy` (if necessary):**

   `pip install moviepy`

9. **Install `imageio[ffmpeg]`:**

   `pip install imageio[ffmpeg]`

10. **Reinstall `whisper` (if necessary):**

    `pip install git+https://github.com/openai/whisper.git`

11. **Reinstall `googletrans` (if necessary):**

    `pip install googletrans==4.0.0-rc1`

12. **Reinstall `pysrt` (if necessary):**

    `pip install pysrt`

13. **Run the script:**

    `python transcribe_subtitles.py`
