import webbrowser
class picture():
    def __init__(self,heading,description,picture,video):
                 self.heading=heading
                 self.description=description
                 self.picture_url=picture
                 self.video_url=video
    def show_tailer(self):
                 webbrowser.open(self.trailer_youtube_url)
