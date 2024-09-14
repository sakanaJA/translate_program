import moviepy.editor as mp
import whisper
from googletrans import Translator
import pysrt
import os

# 動画ファイルの名前から字幕ファイル名を設定
videoname = 'Desktop 2024.09.12 - 20.19.00.14.DVR.mp4'

# ImageMagickのバイナリパスを指定
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

# 動画ファイルから音声を抽出する関数
def extract_audio_from_video(video_path, output_audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)
    audio_clip.close()

# 音声を文字起こしし、英語と日本語の字幕を生成する関数
def transcribe_and_generate_bilingual_subtitles(audio_path):
    # Whisperモデルの読み込み
    model = whisper.load_model("base")

    # 音声ファイルを文字起こし
    result = model.transcribe(audio_path)

    # 翻訳用のインスタンス
    translator = Translator()

    subtitles = []
    for segment in result['segments']:
        start = segment['start']
        end = segment['end']
        english_text = segment['text']

        # 英語の後に日本語翻訳を追加
        japanese_text = translator.translate(english_text, dest='ja').text

        # 字幕テキスト (英語 + 日本語)
        subtitle_text = f"{english_text}\n{japanese_text}"

        # 字幕として追加
        subtitles.append((start, end, subtitle_text))

    return subtitles

# 字幕をSRT形式で保存する関数
def save_subtitles_to_srt(subtitles, output_srt_path):
    subs = pysrt.SubRipFile()

    for index, (start, end, text) in enumerate(subtitles):
        # 字幕の開始時間と終了時間をSRTの形式に変換
        start_time = pysrt.SubRipTime(seconds=int(start))
        end_time = pysrt.SubRipTime(seconds=int(end))

        # 字幕エントリーを作成
        subs.append(pysrt.SubRipItem(index=index + 1, start=start_time, end=end_time, text=text))

    # 一旦UTF-8でSRTファイルを保存
    temp_srt_path = output_srt_path + "_temp"
    subs.save(temp_srt_path, encoding='utf-8')

    # 改行コードをCRに変換して保存
    with open(temp_srt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # CR (`\r`) に変換して保存
    content_cr = content.replace('\n', '\r')

    with open(output_srt_path, 'w', encoding='utf-8') as f:
        f.write(content_cr)

    # 一時ファイルを削除
    os.remove(temp_srt_path)


# 動画ファイルを指定して音声を抽出
video_path = rf'E:\gameplay\Desktop\{videoname}'
audio_path = rf'E:\gameplay\Desktop\temp.wav'

extract_audio_from_video(video_path, audio_path)

# 英語と日本語が交互に並ぶ字幕データを取得
subtitles = transcribe_and_generate_bilingual_subtitles(audio_path)

# 字幕ファイルのパスを動画ファイル名に基づいて作成
output_srt_path = rf'E:\gameplay\subtitle\{os.path.splitext(videoname)[0]}_subtitles.srt'

# 字幕をSRTファイルに保存 (CR形式で改行)
save_subtitles_to_srt(subtitles, output_srt_path)

print(f"字幕ファイルが生成されました: {output_srt_path}")
