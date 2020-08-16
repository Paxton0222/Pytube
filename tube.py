from pytube import YouTube
import os,shutil,subprocess,time
class Youtube:
    def __init__(self,url,userdir):
        try:
            os.makedirs('./YT/影片下載目錄')
        except:
            pass
        self.dir = './YT/影片下載目錄'
        self.userdir = userdir
        self.url = url
        self.yt = YouTube(self.url)
        self.title = self.yt.title
        self.views = self.yt.views
        self.times = self.yt.length
        self.auth = self.yt.author

    def find(self):
        return self.title,self.views,self.times,self.auth
        #title 觀看次數 時間長度 作者
    
    def download_mp4(self):
        self.yt = YouTube(self.url,on_progress_callback=self.progress_mp4)
        try:
            print('正在下載1080P影片...')
            self.download_video = self.yt.streams.filter(subtype='mp4',resolution="1080p")[0]
            self.download_video.download(output_path=self.dir)
            self.download_audio = self.yt.streams.filter(subtype='webm',audio_codec='opus',type='audio')[-1]
            self.download_audio.download(output_path=self.dir)
        except IndexError:
            try:
                print('該影片沒有1080P片源，嘗試720P...')
                self.download_video = self.yt.streams.filter(subtype='mp4',resolution="720p")[0]
                self.download_video.download(output_path=self.dir)
                self.download_audio = self.yt.streams.filter(subtype='webm',audio_codec='opus',type='audio')[-1]
                self.download_audio.download(output_path=self.dir)
            except IndexError:
                try:
                    print('該影片沒有720P片源，嘗試480P...')
                    self.download_video = self.yt.streams.filter(subtype='mp4',resolution="480p")[0]
                    self.download_video.download(output_path=self.dir)
                    self.download_audio = self.yt.streams.filter(subtype='webm',audio_codec='opus',type='audio')[-1]
                    self.download_audio.download(output_path=self.dir)
                except IndexError:
                    try:
                        print('該影片沒有480P片源，嘗試360P...')
                        self.download_video = self.yt.streams.filter(subtype='mp4',resolution="360p")[0]
                        self.download_video.download(output_path=self.dir)
                        self.download_audio = self.yt.streams.filter(subtype='webm',audio_codec='opus',type='audio')[-1]
                        self.download_audio.download(output_path=self.dir)
                    except IndexError:
                        try:
                            print('該影片沒有360P片源，嘗試144P...')
                            self.download_video = self.yt.streams.filter(subtype='mp4',resolution="144p")[0]
                            self.download_video.download(output_path=self.dir)
                            self.download_audio = self.yt.streams.filter(subtype='webm',audio_codec='opus',type='audio')[-1]
                            self.download_audio.download(output_path=self.dir)
                        except IndexError:
                            print('尚未找到該影片片源!')
    def file_mix(self):
        try:
            self.dirlist = os.listdir(self.dir)
            self.video = self.dirlist[int(0)]
            self.audio = self.dirlist[int(1)]
            self.new_video_name = '1.mp4'
            self.new_audio_name = '1.mp3'
            shutil.copy(self.dir+"/"+self.video,self.new_video_name)
            shutil.copy(self.dir+"/"+self.audio,self.new_audio_name)
            self.cmd = f'ffmpeg.exe -i {self.new_video_name} -i {self.new_audio_name} mix.mp4'
            subprocess.call(self.cmd,shell=True)
            os.remove(self.dir+'/'+self.video)
            os.remove(self.dir+'/'+self.audio)
            os.remove(self.new_video_name)
            os.remove(self.new_audio_name)
            try:
                os.rename('mix.mp4',self.title+'.mp4')
                shutil.move(self.title+'.mp4',self.userdir+'/'+self.title+'.mp4')
                shutil.rmtree('./YT')
            except:
                self.time = time.strftime('%Y_%m_%d_%H_%M_%S')
                os.rename('mix.mp4',self.time+'.mp4')
                shutil.move(self.time+'.mp4',self.userdir+'/'+self.time+'.mp4')
                shutil.rmtree('./YT')
        except:
            pass

    def progress_mp4(self,stream,chunk,bytes_remaining):
        self.contentsize = self.download_video.filesize
        size = self.contentsize - bytes_remaining
        print('\r' + '[下載進度]:[%s%s] %.2f%%' % (
        '█' * int(size*20/self.contentsize), 
        ' '*(20-int(size*20/self.contentsize)), 
        float(size/self.contentsize*100)), 
        end='')

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=kXptPzKNMq4&list=RDBaACrT6Ydik&index=18' #更改Url
    dir = r'C:\Users\paxto\Desktop\Tube\video' #指定儲存路徑
    tube = Youtube(url,dir)
    data = tube.find() #查找是否有影片
    print(data) #影片資訊
    video = tube.download_mp4() #下載 mp4 檔案
    mix = tube.file_mix() #合併