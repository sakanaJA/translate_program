1.
python -m venv .venv
2.
.\.venv\Scripts\activate
3.
pip install moviepy git+https://github.com/openai/whisper.git googletrans==4.0.0-rc1 pysrt
4.
pip install deep-translator
5.
pip install ffmpeg-python
6.
pip uninstall numpy
7.
pip install numpy==2.0.0
8.
pip install moviepy
9.
pip install imageio[ffmpeg]
10.
pip install git+https://github.com/openai/whisper.git
11.
pip install googletrans==4.0.0-rc1
12.
pip install pysrt
13.
python transcribe_subtitles.py
