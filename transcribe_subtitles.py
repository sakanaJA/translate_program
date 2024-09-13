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

# 音声を文字起こしし、英語と日本語の字幕を生成する関数
def transcribe_and_generate_bilingual_subtitles(audio_path, output_srt_path):
    # Whisperモデルの読み込み
    model = whisper.load_model("base")

    # 音声ファイルを文字起こし
    result = model.transcribe(audio_path)

    # 翻訳用のインスタンス
    translator = Translator()

    # 字幕ファイルを作成
    subs = pysrt.SubRipFile()
    for idx, segment in enumerate(result['segments']):
        start = segment['start']
        end = segment['end']
        english_text = segment['text']

        # 英語の後に日本語翻訳を追加
        japanese_text = translator.translate(english_text, dest='ja').text

        # 字幕のインデックス
        sub = pysrt.SubRipItem()
        sub.index = idx + 1

        # 開始・終了時間のフォーマット
        sub.start.seconds = start
        sub.end.seconds = end

        # 英語と日本語を追加
        sub.text = f"{english_text}\n{japanese_text}"
        subs.append(sub)
    
    # srtファイルに保存
    subs.save(output_srt_path, encoding='utf-8')

# 動画ファイルを指定して音声を抽出
video_path = r'E:\gameplay\Desktop\Desktop 2024.09.13 - 22.03.51.04.DVR.mp4'  # .mp4拡張子をつける
audio_path = r'E:\gameplay\Desktop\extracted_audio.wav'

extract_audio_from_video(video_path, audio_path)

# 英語と日本語が交互に並ぶ字幕ファイルを作成
output_srt_path_bilingual = 'output_bilingual.srt'
transcribe_and_generate_bilingual_subtitles(audio_path, output_srt_path_bilingual)
