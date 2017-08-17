from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil




def main():
    #ydl_opt = {}
    ydl_opts = {
        'verbose': True,
        #'format' : '{}'.format(int(comboget)),
        'outtmpl': '%(title)s-%(id)s.%(ext)s',
        #'noplaylist': mt,
        #'logger' : MyLogger(),
        #'progress_hooks': [durum],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=fMiHCbQqN1E'])  # muse
        #ydl.download(['https://www.youtube.com/watch?v=u1OyF1Gkz-A&t=3208s'])
        #ydl.download(['https://www.youtube.com/watch?v=fzWQV5OiQQQ'])
        #ydl.download(['https://www.youtube.com/watch?v=u1OyF1Gkz-A&t=3147s'])
        #ydl.download(['https://www.youtube.com/watch?v=Tgh0kADkGXM'])






if __name__ == "__main__":
    main()