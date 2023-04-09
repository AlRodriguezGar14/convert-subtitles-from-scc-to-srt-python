class Timecode_Parser():
    def __init__(self, timecode, framerate):
        self.smpte = timecode
        
        if len(self.smpte.split(';')) >= 2:
            self.drop_frame = True
        else:
            self.drop_frame = False

        if str(framerate).startswith('29'):
            self.int_framerate = 30
            self.framerate = 29.97
        
        elif str(framerate).startswith('23'):
            self.int_framerate = 24
            self.framerate = 23.98

        elif str(framerate).startswith('24'):
            self.int_framerate = 24
            self.framerate = 24.0

        elif str(framerate).startswith('25'):
            self.int_framerate = 25
            self.framerate = 25.0

        elif str(framerate).startswith('30'):
            self.int_framerate = 30
            self.framerate = 30.0

        else:
            self.int_framerate = 24
            self.framerate = 23.98

        # Drop frames is the 6% of the framerate rounded to the nearest number. Confirm this formula
        if self.drop_frame:
            self.drop_frames = int(round(framerate * 0.666666))
        else:
            self.drop_frames = 0

        self.total_frames = self.linear_timecode_total_frames()

        self.real_time = 0

        self.timecode = self.smpte_to_real_time()

    def printer(self):
        print(self.smpte, self.timecode)


    def linear_timecode_total_frames(self):
        #hour_frames = self.int_framerate * 60 * 60
        if len(self.smpte.split(';')) >= 2:
            hours, minutes, seconds = self.smpte.split(':')
            seconds, frames = seconds.split(';')

        else:
            hours, minutes, seconds, frames = self.smpte.split(':')

        try:
            total_minutes = (60 * int(hours)) / int(minutes)
        except:
            total_minutes = 0
        
        # Check the formula of drop frames calculation
        total_frames = (((int(hours) * 3600) + (int(minutes) * 60) + int(seconds)) * self.int_framerate) + int(frames) - (self.drop_frames * (total_minutes - total_minutes // 10))

        return total_frames
    
    def smpte_to_real_time(self):

        miliseconds = int((self.total_frames / self.framerate ) * 1000)

        hours = miliseconds // (1000 * 60 * 60)
        minutes = (miliseconds // (1000 * 60)) % 60
        seconds = (miliseconds // 1000) % 60
        miliseconds = miliseconds % 1000

        return '0{}:{:02d}:{:02d},{:03d}'.format(hours, minutes, seconds, miliseconds)


