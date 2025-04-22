import tkinter as tk
import random

# Configuration
ROOM_SIZE = 150  # reduced room dimensions
PIXEL_SIZE = 5
ACCELERATION = 0.9  # increased speed
MOMENTUM = 0.9
DOOR_SIZE = 50
WINDOW_OFFSET = 100
WINDOW_SPACING = 0  # no gaps between windows

# Directions
DIRECTIONS = ['Left', 'Right', 'Up', 'Down']
OFFSETS = {'Left': (-1, 0), 'Right': (1, 0), 'Up': (0, -1), 'Down': (0, 1)}
OPPOSITE = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}

def generate_specs(total):
    specs = []
    last_exit = None
    for i in range(total):
        if i == 0:
            entrance = None
            exit_ = random.choice(DIRECTIONS)
        elif i == total - 1:
            entrance = OPPOSITE[last_exit]
            exit_ = None
        else:
            entrance = OPPOSITE[last_exit]
            exit_ = random.choice([d for d in DIRECTIONS if d != entrance])
        specs.append({'entrance': entrance, 'exit': exit_})
        last_exit = exit_
    return specs

class Panel:
    def __init__(self, root, is_main=False):
        # Create a window without title bar
        self.window = root if is_main else tk.Toplevel(root)
        self.window.overrideredirect(True)
        self.window.resizable(False, False)
        self.canvas = tk.Canvas(self.window, width=ROOM_SIZE, height=ROOM_SIZE,
                                bg='black', highlightthickness=0)
        self.canvas.pack()

    def render(self, spec, title, x, y):
        self.window.geometry(f"{ROOM_SIZE}x{ROOM_SIZE}+{x}+{y}")
        self.window.title(title)
        self.canvas.delete('all')
        mid = ROOM_SIZE // 2
        gap = DOOR_SIZE // 2
        for side in DIRECTIONS:
            x0, y0, x1, y1 = self._coords(side)
            if side in (spec.get('entrance'), spec.get('exit')):
                if side in ('Up', 'Down'):
                    self.canvas.create_line(0, y0, mid-gap, y1, width=5, fill='white')
                    self.canvas.create_line(mid+gap, y0, ROOM_SIZE, y1, width=5, fill='white')
                else:
                    self.canvas.create_line(x0, 0, x1, mid-gap, width=5, fill='white')
                    self.canvas.create_line(x0, mid+gap, x1, ROOM_SIZE, width=5, fill='white')
            else:
                self.canvas.create_line(x0, y0, x1, y1, width=5, fill='white')

    def _coords(self, side):
        if side == 'Left':   return (0, 0, 0, ROOM_SIZE)
        if side == 'Right':  return (ROOM_SIZE, 0, ROOM_SIZE, ROOM_SIZE)
        if side == 'Up':     return (0, 0, ROOM_SIZE, 0)
        if side == 'Down':   return (0, ROOM_SIZE, ROOM_SIZE, ROOM_SIZE)

class Player:
    def __init__(self, game):
        self.game = game
        self.canvas = None
        self.rect = None
        self.vx = self.vy = 0
        self.keys = set()
        self.last_direction = None

    def bind(self, window):
        window.bind('<KeyPress>', self._press)
        window.bind('<KeyRelease>', self._release)

    def _press(self, e):
        if e.keysym in DIRECTIONS:
            self.keys.add(e.keysym)

    def _release(self, e):
        if e.keysym in DIRECTIONS:
            self.keys.discard(e.keysym)

    def spawn(self, spec):
        canvas = self.game.current_panel.canvas
        self.canvas = canvas
        if self.rect:
            self.canvas.delete(self.rect)
        ent = spec.get('entrance') if self.last_direction is None else OPPOSITE[self.last_direction]
        coords = self.game.next_entry_coords
        mid = ROOM_SIZE // 2
        if ent == 'Left':
            y = (coords[1] if coords else mid - PIXEL_SIZE//2)
            x = 0
        elif ent == 'Right':
            y = (coords[1] if coords else mid - PIXEL_SIZE//2)
            x = ROOM_SIZE - PIXEL_SIZE
        elif ent == 'Up':
            x = (coords[0] if coords else mid - PIXEL_SIZE//2)
            y = 0
        elif ent == 'Down':
            x = (coords[0] if coords else mid - PIXEL_SIZE//2)
            y = ROOM_SIZE - PIXEL_SIZE
        else:
            x, y = mid - PIXEL_SIZE//2, mid - PIXEL_SIZE//2
        self.game.next_entry_coords = None
        self.rect = self.canvas.create_rectangle(x, y, x + PIXEL_SIZE, y + PIXEL_SIZE,
                                                 fill='white')

    def update(self):
        if 'Left' in self.keys:  self.vx -= ACCELERATION
        if 'Right' in self.keys: self.vx += ACCELERATION
        if 'Up' in self.keys:    self.vy -= ACCELERATION
        if 'Down' in self.keys:  self.vy += ACCELERATION
        self.canvas.move(self.rect, self.vx, self.vy)
        self.vx *= MOMENTUM; self.vy *= MOMENTUM
        x0, y0, x1, y1 = self.canvas.coords(self.rect)
        hit = None
        if x0 <= 0:       hit = 'Left'
        elif x1 >= ROOM_SIZE: hit = 'Right'
        elif y0 <= 0:     hit = 'Up'
        elif y1 >= ROOM_SIZE: hit = 'Down'
        if hit:
            self.game.next_entry_coords = (x0, y0, x1, y1)
            idx = self.game.current
            spec = self.game.specs[idx]
            if spec.get('exit') == hit and idx < len(self.game.specs) - 1:
                self.last_direction = hit
                self.game.change(idx + 1)
                return
            if spec.get('entrance') == hit and idx > 0:
                self.last_direction = hit
                self.game.change(idx - 1)
                return
            if hit in ('Left', 'Right'):
                self.vx *= -1.5
            else:
                self.vy *= -1.5
        self.game.root.after(16, self.update)

class Game:
    def __init__(self, total=20):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        self.specs = generate_specs(total)
        raw = []
        x0, y0 = WINDOW_OFFSET, WINDOW_OFFSET
        raw.append((x0, y0))
        for i in range(1, len(self.specs)):
            prev = raw[i - 1]
            dir_ = self.specs[i - 1]['exit']
            off = OFFSETS.get(dir_, (0, 0))
            raw.append((prev[0] + off[0] * (ROOM_SIZE + WINDOW_SPACING),
                        prev[1] + off[1] * (ROOM_SIZE + WINDOW_SPACING)))
        xs = [c[0] for c in raw]; ys = [c[1] for c in raw]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        margin = WINDOW_OFFSET
        dx = margin - min_x if min_x < margin else (
            screen_w - margin - ROOM_SIZE - max_x if max_x + ROOM_SIZE > screen_w - margin else 0)
        dy = margin - min_y if min_y < margin else (
            screen_h - margin - ROOM_SIZE - max_y if max_y + ROOM_SIZE > screen_h - margin else 0)
        self.coords = [(x + dx, y + dy) for x, y in raw]
        
        self.panels = [Panel(self.root), Panel(self.root, is_main=True), Panel(self.root)]
        self.player = Player(self)
        for p in self.panels:
            self.player.bind(p.window)
        self.current = 0
        self.next_entry_coords = None
        self.show_panels()
        self.panels[1].window.focus_force()
        self.player.spawn(self.specs[0])
        self.player.update()
        self.root.mainloop()

    @property
    def current_panel(self):
        return self.panels[1]

    def show_panels(self):
        for slot, rel in enumerate([-1, 0, 1]):
            idx = self.current + rel
            pnl = self.panels[slot]
            if 0 <= idx < len(self.specs):
                x, y = self.coords[idx]
                pnl.render(self.specs[idx], f"Room {idx}", x, y)
                pnl.window.deiconify()
                if rel == 0:
                    pnl.window.focus_force()
            else:
                pnl.window.withdraw()

    def change(self, new_idx):
        self.current = new_idx
        self.show_panels()
        self.player.spawn(self.specs[new_idx])
        self.panels[1].window.focus_force()
        self.player.update()

if __name__ == '__main__':
    Game(total=20)
