import tkinter as tk
import random
import time

# Default Configuration
DEFAULTS = {
    'ROOM_SIZE': 150,
    'PIXEL_SIZE': 5,
    'ACCELERATION': 1.0,
    'MOMENTUM': 0.95,
    'WINDOW_OFFSET': 100,
    'WINDOW_SPACING': 0,
    'TOTAL_ROOMS': 20
}

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
    def __init__(self, root, is_main=False, settings=None):
        self.settings = settings
        self.window = root if is_main else tk.Toplevel(root)
        self.window.overrideredirect(True)
        self.window.resizable(False, False)
        size = self.settings['ROOM_SIZE']
        self.canvas = tk.Canvas(self.window, width=size, height=size,
                                bg='black', highlightthickness=0)
        self.canvas.pack()

    def render(self, spec, title, x, y):
        size = self.settings['ROOM_SIZE']
        self.window.geometry(f"{size}x{size}+{x}+{y}")
        self.window.title(title)
        self.canvas.delete('all')
        size = self.settings['ROOM_SIZE']
        mid = size // 2
        # Draw walls except entrance/exit
        for side in DIRECTIONS:
            if side in (spec.get('entrance'), spec.get('exit')):
                continue
            x0, y0, x1, y1 = self._coords(side, size)
            self.canvas.create_line(x0, y0, x1, y1, width=5, fill='white')
        # Draw arrow towards exit
        arrow_opts = dict(width=3, fill='white', arrow='last')
        exit_dir = spec.get('exit')
        if exit_dir:
            if exit_dir == 'Left':
                self.canvas.create_line(mid, mid, 0, mid, **arrow_opts)
            elif exit_dir == 'Right':
                self.canvas.create_line(mid, mid, size, mid, **arrow_opts)
            elif exit_dir == 'Up':
                self.canvas.create_line(mid, mid, mid, 0, **arrow_opts)
            elif exit_dir == 'Down':
                self.canvas.create_line(mid, mid, mid, size, **arrow_opts)

    def _coords(self, side, size):
        if side == 'Left':   return (0, 0, 0, size)
        if side == 'Right':  return (size, 0, size, size)
        if side == 'Up':     return (0, 0, size, 0)
        if side == 'Down':   return (0, size, size, size)


class Player:
    def __init__(self, game, settings):
        self.game = game
        self.settings = settings
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
        s = self.settings
        canvas = self.game.current_panel.canvas
        self.canvas = canvas
        if self.rect:
            self.canvas.delete(self.rect)
        ent = spec.get('entrance') if self.last_direction is None else OPPOSITE[self.last_direction]
        coords = self.game.next_entry_coords
        mid = s['ROOM_SIZE'] // 2
        if ent == 'Left':
            y = coords[1] if coords else mid - s['PIXEL_SIZE']//2
            x = 0
        elif ent == 'Right':
            y = coords[1] if coords else mid - s['PIXEL_SIZE']//2
            x = s['ROOM_SIZE'] - s['PIXEL_SIZE']
        elif ent == 'Up':
            x = coords[0] if coords else mid - s['PIXEL_SIZE']//2
            y = 0
        elif ent == 'Down':
            x = coords[0] if coords else mid - s['PIXEL_SIZE']//2
            y = s['ROOM_SIZE'] - s['PIXEL_SIZE']
        else:
            x, y = mid - s['PIXEL_SIZE']//2, mid - s['PIXEL_SIZE']//2
        self.game.next_entry_coords = None
        self.rect = self.canvas.create_rectangle(
            x, y, x + s['PIXEL_SIZE'], y + s['PIXEL_SIZE'], fill='white')

    def update(self):
        s = self.settings
        if 'Left' in self.keys:  self.vx -= s['ACCELERATION']
        if 'Right' in self.keys: self.vx += s['ACCELERATION']
        if 'Up' in self.keys:    self.vy -= s['ACCELERATION']
        if 'Down' in self.keys:  self.vy += s['ACCELERATION']
        self.canvas.move(self.rect, self.vx, self.vy)
        self.vx *= s['MOMENTUM']; self.vy *= s['MOMENTUM']
        x0, y0, x1, y1 = self.canvas.coords(self.rect)
        hit = None
        if x0 <= 0: hit = 'Left'
        elif x1 >= s['ROOM_SIZE']: hit = 'Right'
        elif y0 <= 0: hit = 'Up'
        elif y1 >= s['ROOM_SIZE']: hit = 'Down'
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
            # bounce
            if hit in ('Left', 'Right'):
                self.vx *= -1.5
            else:
                self.vy *= -1.5
        self.game.root.after(16, self.update)


class Game:
    def __init__(self, settings):
        self.settings = settings
        self.specs = generate_specs(settings['TOTAL_ROOMS'])
        self.current = 0
        self.next_entry_coords = None
        self.start_time = None
        self.root = None
        self.timer_window = None
        self.panels = []
        self.player = None

    def start(self):
        self._countdown()

    def _countdown(self):
        count = 3
        cd = tk.Toplevel()
        def tick():
            nonlocal count
            if count > 0:
                cd.geometry(f"100x50+{cd.winfo_screenwidth()-110}+10")
                lbl = tk.Label(cd, text=str(count), font=(None, 24))
                lbl.pack()
                count -= 1
                lbl.after(1000, lambda: (lbl.destroy(), tick()))
            else:
                cd.destroy()
                self.launch()
        tick()

    def launch(self):
        s = self.settings
        self.start_time = time.time()
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.update_idletasks()
        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # timer
        self.timer_window = tk.Toplevel(self.root)
        self.timer_window.overrideredirect(True)
        self.timer_window.geometry(f"100x30+{sw-110}+10")
        self.timer_label = tk.Label(self.timer_window, text="0.0s",
                                     bg='black', fg='white', font=(None, 12))
        self.timer_label.pack()
        self._update_timer()
        # positions
        raw = [(s['WINDOW_OFFSET'], s['WINDOW_OFFSET'])]
        for i in range(1, len(self.specs)):
            px, py = raw[i-1]; dir_ = self.specs[i-1]['exit']
            ox, oy = OFFSETS[dir_]
            raw.append((px + ox*(s['ROOM_SIZE']+s['WINDOW_SPACING']),
                        py + oy*(s['ROOM_SIZE']+s['WINDOW_SPACING'])))
        xs, ys = zip(*raw)
        min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
        margin = s['WINDOW_OFFSET']
        dx = margin-min_x if min_x<margin else (sw-margin-s['ROOM_SIZE']-max_x if max_x+s['ROOM_SIZE']>sw-margin else 0)
        dy = margin-min_y if min_y<margin else (sh-margin-s['ROOM_SIZE']-max_y if max_y+s['ROOM_SIZE']>sh-margin else 0)
        coords = [(max(0, min(x+dx, sw-s['ROOM_SIZE'])),
                   max(0, min(y+dy, sh-s['ROOM_SIZE']))) for x,y in raw]
        # panels
        self.panels = [Panel(self.root, settings=s) for _ in range(5)]
        # mark middle as main
        self.panels[2] = Panel(self.root, is_main=True, settings=s)
        self.player = Player(self, s)
        for p in self.panels: self.player.bind(p.window)
        self.coords = coords
        self._show()
        self.panels[2].window.focus_force()
        self.player.spawn(self.specs[0]); self.player.update()
        self.root.mainloop()

    def _update_timer(self):
        elapsed = time.time() - self.start_time
        self.timer_label.config(text=f"{elapsed:.1f}s")
        self.timer_window.after(100, self._update_timer)

    @property
    def current_panel(self):
        return self.panels[2]

    def _show(self):
        rels = [-2, -1, 0, 1, 2]
        for slot, rel in enumerate(rels):
            idx = self.current + rel
            pnl = self.panels[slot]
            if 0 <= idx < len(self.specs):
                x, y = self.coords[idx]
                pnl.render(self.specs[idx], f"Room {idx}", x, y)
                pnl.window.deiconify()
                if rel == 0: pnl.window.focus_force()
            else:
                pnl.window.withdraw()

    def change(self, new_idx):
        self.current = new_idx
        if new_idx == len(self.specs)-1:
            # end game and return to menu
            self.root.destroy()
            app = Application()
            app.run()
            return
        self._show()
        self.player.spawn(self.specs[new_idx])
        self.panels[2].window.focus_force()
        self.player.update()


class Application:
    def __init__(self):
        self.settings = DEFAULTS.copy()

    def run(self):
        self.show_menu()

    def show_menu(self):
        self.menu = tk.Tk()
        self.menu.title("Settings")
        sw, sh = self.menu.winfo_screenwidth(), self.menu.winfo_screenheight()
        mw, mh = 400, 350
        mx, my = (sw-mw)//2, (sh-mh)//2
        self.menu.geometry(f"{mw}x{mh}+{mx}+{my}")
        frm = tk.Frame(self.menu)
        frm.pack(padx=20, pady=20)
        self.entries = {}
        for i,(key,val) in enumerate(self.settings.items()):
            tk.Label(frm, text=key).grid(row=i, column=0, sticky='e')
            ent = tk.Entry(frm)
            ent.insert(0, str(val))
            ent.grid(row=i, column=1)
            self.entries[key] = ent
        btn = tk.Button(self.menu, text="Start", font=(None, 16),
                        command=self._on_start)
        btn.pack(pady=10)
        self.menu.mainloop()

    def _on_start(self):
        for key, ent in self.entries.items():
            val = ent.get()
            # convert to float or int appropriately
            if '.' in val:
                self.settings[key] = float(val)
            else:
                self.settings[key] = int(val)
        self.menu.destroy()
        game = Game(self.settings)
        game.start()


if __name__ == '__main__':
    Application().run()