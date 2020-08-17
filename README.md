[tube.py](./tube.py) 使用方法
---
* 欲使用tube.py的話須先下載 **ffmpeg.exe**，並且須移動ffmpeg.exe至同個資料夾

    https://ffmpeg.org/download.html

    linux用戶直接使用 tube.download_ffmpeg() 指令即可 (Debian用戶)

* Pytube 模組更改 pytube/extract.py line 301行(修改此問題後將不會在出現報錯)

        parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)

    詳情請見 :
    https://stackoverflow.com/questions/62098925/why-my-youtube-video-downloader-only-downloads-some-videos-and-for-other-videos/62115943#62115943

* 指定儲存路徑(須自己建立一個已存在的資料夾)

    dir = r'' #指定儲存路徑

* 模組下載指令

        pip install pytube3