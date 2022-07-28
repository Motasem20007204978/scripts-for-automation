
import math
import pafy
import os

def extractedVideos(playlist):

    listOfVideos = []

    # getting playlist items 
    items = playlist["items"] 
      
    # selecting single item 
    for item in items:
        
        # getting pafy object 
        i_pafy = item['pafy'] 
              
              
        # getting watch url 
        y_url = i_pafy.watchv_url 
          
        # add url 
        listOfVideos.append(y_url) 

    return listOfVideos

def typeStream():
    
    Type = input('1.video with audio\n2.video without audio\n'
        '3.only audio\ninput number of type :')

    while True:
        
        try:
            chosenTypeOfStream = int(Type)
            while chosenTypeOfStream not in range(1,4):
                chosenTypeOfStream = int(input('Please enter from list :'))
            break
        except :
            Type = input('invalid input, must be a number from list :')

    return chosenTypeOfStream

def savePath():
    SAVE_PATH = input('enter the path u wanna save video to :')
    while not os.path.exists(SAVE_PATH) :
        SAVE_PATH = input('invalid path, please enter correct path :')
    return SAVE_PATH

    

char = input('enter \'v\' if u want to download single video or \'p\' if playlist :')
while char not in ['v','p']:
    char = input(('please inter v or p :' ))

if char == 'v':
    #link of the video to be downloaded
    videoLink = input("enter video link u wanna download :")
    try:
        vid = pafy.new(videoLink)        
    except :
        print('invalid link')
        exit(0)

    chosenTypeOfStream = typeStream()

    if chosenTypeOfStream == 1:
        Streams = vid.streams
    elif chosenTypeOfStream == 2:
        Streams = vid.videostreams
    else:
        Streams = vid.audiostreams


    print('list of streams :')
    for c,stream in enumerate(Streams) :
        # print stream & getting size of stream in mega 
        videoSize = stream.get_filesize()
        print(c,' stream is ',stream,' & its size is %f migabytes '
            %(videoSize/math.pow(10,6)))

    itag = int(input("enter number of itag u wanna download :"))
    while itag not in range(len(Streams)):
        itag = int(input('Please enter from list :'))


    SAVE_PATH = savePath()
    
    def download_progress(self,dledBytes,dlPercentage,dlSpeed,remainingTime):
        print('Done...')#print progress of parameters in download
        

    #downloading the video   callback=video_progressbar
    Streams[itag].download(SAVE_PATH, progress="MB",callback = download_progress) 

    print('Download Completed!') 

else:

    
    #link of the playlist to be downloaded
    playlistLink = input('enter playlist link :')
    try:        
        playlist = pafy.get_playlist(playlistLink)
    except :
        print('invalid link')
        exit(0)

    chosenTypeOfStream = typeStream()

    SAVE_PATH = savePath()

    videosLinks = extractedVideos(playlist)

    for c,v in enumerate(videosLinks):
        vid = pafy.new(v)

        if chosenTypeOfStream == 1:
            bestStream = vid.streams[0]
        elif chosenTypeOfStream == 2:
            bestStream = vid.videostreams[len(vid.videostreams)-1]
        else:
            bestStream = vid.audiostreams[len(vid.audiostreams)-1]

        print('video %d is going to download :'%(c+1))

        streamSize = bestStream.get_filesize()
        print('stream is ',bestStream,' & its size is %f migabytes '
            %(streamSize/math.pow(10,6)))
        
        def download_progress(self,dledBytes,dlPercentage,dlSpeed,remainingTime):
            print('Done...')#print progress of parameters in download
        
        bestStream.download(SAVE_PATH, progress="MB",callback = download_progress) 

    print('Download Completed!')