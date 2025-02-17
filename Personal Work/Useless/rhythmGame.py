import tkinter as tk
import time


class RhythmGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.score = 0
        self.beats = []
        self.running = False
        self.hit_offsets = []
        self.start_time = None
        self.create_widgets()
        self.master.bind("<Key>", self.handle_key_press)
        self.beatmap = "140 1,,,,1,,,,1,,,,2,,,,2,,,,1,,2,,1,,2,,"

    def create_widgets(self):
        self.canvas = tk.Canvas(self, bg="black", height=500, width=500)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Helvetica", 14))
        self.score_label.grid(row=1, column=0)

        self.start_button = tk.Button(self, text="Start", command=self.start_game)
        self.start_button.grid(row=1, column=1)

        self.offset_label = tk.Label(self, text="Offsets: ", font=("Helvetica", 14))
        self.offset_label.grid(row=2, column=0, columnspan=2)

    def start_game(self):
        self.running = True
        self.score = 0
        self.hit_offsets = []
        self.start_time = time.time()  # Start the timing here
        self.update_score()
        self.parse_beatmap(self.beatmap)  # Generate beats based on the beatmap
        self.animate_beats()

    def parse_beatmap(self, beatmap):
        sections = beatmap.split()
        self.beats = []
        i = 0
        while i < len(sections):
            bpm = int(sections[i])
            pattern = sections[i + 1]
            interval = 60 / bpm
            start_time = self.start_time + 2  # start after 2 seconds

            for j, char in enumerate(pattern):
                if char in '12':
                    track = int(char)
                    beat_time = start_time + j * interval
                    x = 150 if track == 1 else 350
                    y = 0
                    beat_id = self.canvas.create_oval(x - 10, y, x + 10, y + 20, fill="red")
                    self.beats.append((beat_time, beat_id, track))

            i += 2

    def animate_beats(self):
        if not self.running:
            return

        for beat in self.beats:
            beat_time, beat_id, track = beat
            if beat_time <= time.time():
                self.canvas.move(beat_id, 0, 10)
                if self.canvas.coords(beat_id)[1] >= 480:  # if beat reaches bottom
                    self.canvas.delete(beat_id)
                    self.beats.remove(beat)

        self.master.after(50, self.animate_beats)

    def handle_key_press(self, event):
        key = event.keysym  # get the key symbol
        if key == "j":
            self.check_hits(1)
        elif key == "k":
            self.check_hits(2)

    def check_hits(self, track):
        closest_beat = None
        closest_offset = float('inf')

        for beat in self.beats:
            beat_time, beat_id, beat_track = beat
            if beat_track == track:
                offset = abs(time.time() - beat_time) * 1000
                if offset < closest_offset and 450 <= self.canvas.coords(beat_id)[1] <= 480:
                    closest_offset = offset
                    closest_beat = beat

        if closest_beat:
            _, beat_id, _ = closest_beat
            self.canvas.delete(beat_id)
            self.beats.remove(closest_beat)
            self.score += 1
            self.hit_offsets.append(closest_offset)
            self.update_score()
            self.update_offsets()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def update_offsets(self):
        offsets_text = "Offsets: " + ", ".join(f"{offset:.1f}ms" for offset in self.hit_offsets)
        self.offset_label.config(text=offsets_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = RhythmGame(master=root)
    app.master.title("Rhythm Game")
    app.mainloop()
