from pytube import YouTube

video_url = input("Enter YouTube Video link: ")

yt= YouTube(video_url)

stream = yt.streams.get_highest_resolution()

stream.download()

print("Download Completed")
