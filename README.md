Subtitle Transcription and Translation Setup
このプロジェクトでは、動画から音声を抽出し、字幕を生成・翻訳するPythonスクリプトを実行します。以下の手順に従って、必要な環境をセットアップしてください。

環境セットアップ手順
仮想環境の作成
プロジェクトディレクトリで仮想環境を作成します。

bash
コードをコピーする
python -m venv .venv
仮想環境のアクティベート
仮想環境をアクティブにします。

bash
コードをコピーする
.\.venv\Scripts\activate
依存関係のインストール
以下のコマンドで必要なライブラリをインストールします。

bash
コードをコピーする
pip install moviepy git+https://github.com/openai/whisper.git googletrans==4.0.0-rc1 pysrt
追加ライブラリのインストール
deep-translator と ffmpeg-python をインストールします。

bash
コードをコピーする
pip install deep-translator
pip install ffmpeg-python
NumPyのダウングレード
Whisperが依存するNumPyのバージョンを2.0.0に設定します。

bash
コードをコピーする
pip uninstall numpy
pip install numpy==2.0.0
MoviePy、ffmpegの再インストール
必要なパッケージを再インストールします。

bash
コードをコピーする
pip install moviepy
pip install imageio[ffmpeg]
WhisperとGoogle Translate、Pysrtの再インストール
再度Whisperやその他ライブラリをインストールします。

bash
コードをコピーする
pip install git+https://github.com/openai/whisper.git
pip install googletrans==4.0.0-rc1
pip install pysrt
スクリプトの実行
環境が整ったら、以下のコマンドで字幕生成スクリプトを実行します。

bash
コードをコピーする
python transcribe_subtitles.py
