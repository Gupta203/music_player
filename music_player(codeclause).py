import os
import pygame
from tkinter import Tk, Button, filedialog

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.root = Tk()
        self.root.title("Simple Music Player")
        self.root.configure(bg="lightblue")  # Set background color
        self.current_song = None
        self.paused = False

        self.play_button = Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.select_button = Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_button.pack()

    def play(self):
        if self.current_song:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.load(self.current_song)
                pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.current_song = None

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.stop()
            songs = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.mp3')]
            if songs:
                self.current_song = songs[0]
                self.play()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
