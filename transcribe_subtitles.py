import moviepy.editor as mp
import whisper
from googletrans import Translator
import pysrt

# 動画ファイルから音声を抽出する関数
def extract_audio_from_video(video_path, output_audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)
    audio_clip.close()

# 音声を文字起こしし、字幕ファイルを生成する関数
def transcribe_and_generate_subtitles(audio_path, output_srt_path, target_language='ja'):
    # Whisperモデルの読み込み
    model = whisper.load_model("base")

    # 音声ファイルを文字起こし
    result = model.transcribe(audio_path)

    # 日本語または英語に翻訳
    translator = Translator()
    translated_texts = []
    for segment in result['segments']:
        text = segment['text']
        if target_language != 'en':
            translated = translator.translate(text, dest=target_language).text
        else:
            translated = text
        translated_texts.append((segment['start'], segment['end'], translated))
    
    # .srtファイルとして出力
    subs = pysrt.SubRipFile()
    for idx, (start, end, text) in enumerate(translated_texts):
        # 字幕のインデックス
        sub = pysrt.SubRipItem()
        sub.index = idx + 1
        
        # 開始・終了時間のフォーマット
        sub.start.seconds = start
        sub.end.seconds = end
        
        # 翻訳されたテキストを追加
        sub.text = text
        subs.append(sub)
    
    # srtファイルに保存
    subs.save(output_srt_path, encoding='utf-8')

# 動画ファイルを指定して音声を抽出
video_path = r'E:\gameplay\Desktop\Desktop 2024.09.13 - 22.03.51.04.DVR.mp4'  # .mp4拡張子をつける
audio_path = r'E:\gameplay\Desktop\extracted_audio.wav'

extract_audio_from_video(video_path, audio_path)

# 日本語字幕を作成
output_srt_path_japanese = 'output_japanese.srt'
transcribe_and_generate_subtitles(audio_path, output_srt_path_japanese, target_language='ja')

# 英語字幕を作成
output_srt_path_english = 'output_english.srt'
transcribe_and_generate_subtitles(audio_path, output_srt_path_english, target_language='en')
