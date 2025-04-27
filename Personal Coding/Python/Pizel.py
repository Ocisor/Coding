import tkinter as tk
import random
import time
import math

# Default Configuration
DEFAULTS = {
    'ROOM_SIZE': 150,
    'PIXEL_SIZE': 5,
    'ACCELERATION': 1.0,
    'MOMENTUM': 0.95,
    'WINDOW_OFFSET': 100,
    'WINDOW_SPACING': 0,
    'TOTAL_ROOMS': 20,
    'COLLECTIBLES_PER_ROOM': 3,  # New setting
    'OBSTACLES_PER_ROOM': 2,     # New setting
    'TARGET_TIME': 60            # New setting - target completion time in seconds
}

# Directions
DIRECTIONS = ['Left', 'Right', 'Up', 'Down']
OFFSETS = {'Left': (-1, 0), 'Right': (1, 0), 'Up': (0, -1), 'Down': (0, 1)}
OPPOSITE = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}

# Room Types
ROOM_TYPES = [
    {'name': 'normal', 'color': 'black', 'line_color': 'white'},
    {'name': 'ice', 'color': '#5599FF', 'line_color': 'white', 'momentum': 0.99},
    {'name': 'mud', 'color': '#996633', 'line_color': '#DDAA66', 'momentum': 0.85},
    {'name': 'dark', 'color': '#111111', 'line_color': '#444444'},
    {'name': 'wind', 'color': '#88CCFF', 'line_color': 'white', 'wind': (0.2, 0.2)}
]

def generate_specs(total):
    specs = []
    last_exit = None
    for i in range(total):
        if i == 0:
            entrance = None
            exit_ = random.choice(DIRECTIONS)
            room_type = 'normal'  # First room always normal
        elif i == total - 1:
            entrance = OPPOSITE[last_exit]
            exit_ = None
            room_type = 'normal'  # Last room always normal
        else:
            entrance = OPPOSITE[last_exit]
            exit_ = random.choice([d for d in DIRECTIONS if d != entrance])
            room_type = random.choice([t['name'] for t in ROOM_TYPES])
        
        # Each room can have collectibles and obstacles
        collectibles = []
        obstacles = []
        
        specs.append({
            'entrance': entrance, 
            'exit': exit_,
            'room_type': room_type,
            'collectibles': collectibles,
            'obstacles': obstacles,
            'visited': False
        })
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
        self.visible = False
        self.collectibles = []
        self.obstacles = []

    def render(self, spec, title, x, y):
        size = self.settings['ROOM_SIZE']
        if not self.visible or self.window.geometry() != f"{size}x{size}+{x}+{y}":
            self.window.geometry(f"{size}x{size}+{x}+{y}")
        self.window.title(title)
        self.canvas.delete('all')
        
        # Get room type properties
        room_type_props = next((t for t in ROOM_TYPES if t['name'] == spec['room_type']), ROOM_TYPES[0])
        bg_color = room_type_props['color']
        line_color = room_type_props['line_color']
        
        # Set background color
        self.canvas.config(bg=bg_color)
        
        size = self.settings['ROOM_SIZE']
        mid = size // 2
        
        # Draw walls except entrance/exit
        for side in DIRECTIONS:
            if side in (spec.get('entrance'), spec.get('exit')):
                continue
            x0, y0, x1, y1 = self._coords(side, size)
            self.canvas.create_line(x0, y0, x1, y1, width=5, fill=line_color)
        
        # Draw arrow towards exit
        arrow_opts = dict(width=3, fill=line_color, arrow='last')
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
        
        # Add room number indicator
        room_number = title.split(" ")[1]
        self.canvas.create_text(size-20, 20, text=room_number, fill=line_color, font=('Arial', 12))
        
        # Generate collectibles if not already visited
        if not spec['visited'] and self.settings['COLLECTIBLES_PER_ROOM'] > 0:
            self.generate_collectibles(spec)
            self.generate_obstacles(spec)
            spec['visited'] = True
        
        # Draw existing collectibles
        for i, (x, y) in enumerate(spec['collectibles']):
            color = self._collectible_color(i)
            item = self.canvas.create_oval(
                x-3, y-3, x+3, y+3, 
                fill=color, outline=color
            )
            self.collectibles.append(item)
        
        # Draw existing obstacles
        for i, (x, y, size) in enumerate(spec['obstacles']):
            item = self.canvas.create_rectangle(
                x-size/2, y-size/2, x+size/2, y+size/2,
                fill='red', outline='darkred'
            )
            self.obstacles.append(item)
        
        # If it's a wind room, draw some wind indicators
        if spec['room_type'] == 'wind':
            self._draw_wind_particles()

    def _draw_wind_particles(self):
        size = self.settings['ROOM_SIZE']
        for _ in range(20):
            x = random.randint(10, size-10)
            y = random.randint(10, size-10)
            length = random.randint(5, 15)
            self.canvas.create_line(
                x, y, x+length, y, 
                fill='white', width=1, dash=(2, 4)
            )

    def _collectible_color(self, index):
        # Return different colors for different collectibles
        colors = ['gold', 'silver', '#66FFFF', '#FF99FF', '#99FF99']
        return colors[index % len(colors)]

    def generate_collectibles(self, spec):
        size = self.settings['ROOM_SIZE']
        buffer = 25  # Distance from walls
        
        # Clear any existing collectibles
        spec['collectibles'] = []
        
        # Generate new collectibles
        for _ in range(self.settings['COLLECTIBLES_PER_ROOM']):
            x = random.randint(buffer, size - buffer)
            y = random.randint(buffer, size - buffer)
            spec['collectibles'].append((x, y))

    def generate_obstacles(self, spec):
        size = self.settings['ROOM_SIZE']
        buffer = 30  # Distance from walls
        
        # Clear any existing obstacles
        spec['obstacles'] = []
        
        # Generate new obstacles
        for _ in range(self.settings['OBSTACLES_PER_ROOM']):
            x = random.randint(buffer, size - buffer)
            y = random.randint(buffer, size - buffer)
            obstacle_size = random.randint(10, 20)
            spec['obstacles'].append((x, y, obstacle_size))

    def _coords(self, side, size):
        if side == 'Left':   return (0, 0, 0, size)
        if side == 'Right':  return (size, 0, size, size)
        if side == 'Up':     return (0, 0, size, 0)
        if side == 'Down':   return (0, size, size, size)
    
    def show(self):
        if not self.visible:
            self.window.update_idletasks()  # Prepare window before showing
            self.window.deiconify()
            self.visible = True
    
    def hide(self):
        if self.visible:
            self.window.withdraw()
            self.visible = False


class Player:
    def __init__(self, game, settings):
        self.game = game
        self.settings = settings
        self.canvas = None
        self.rect = None
        self.vx = self.vy = 0
        self.keys = set()
        self.last_direction = None
        self.score = 0

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
        
        # Get player color based on progress through the game
        progress = self.game.current / max(1, len(self.game.specs) - 1)
        color = self._get_progress_color(progress)
        
        self.rect = self.canvas.create_rectangle(
            x, y, x + s['PIXEL_SIZE'], y + s['PIXEL_SIZE'], fill=color)

    def _get_progress_color(self, progress):
        # Change player color based on progress through the game
        # Starts white, gradually transitions to bright green
        r = int(255 * (1 - progress))
        g = 255
        b = int(255 * (1 - progress))
        return f'#{r:02x}{g:02x}{b:02x}'

    def update(self):
        s = self.settings
        idx = self.game.current
        spec = self.game.specs[idx]
        room_type = spec['room_type']
        
        # Get room-specific properties
        room_props = next((t for t in ROOM_TYPES if t['name'] == room_type), {})
        momentum = room_props.get('momentum', s['MOMENTUM'])
        wind = room_props.get('wind', (0, 0))
        
        # Apply controls
        if 'Left' in self.keys:  self.vx -= s['ACCELERATION']
        if 'Right' in self.keys: self.vx += s['ACCELERATION']
        if 'Up' in self.keys:    self.vy -= s['ACCELERATION']
        if 'Down' in self.keys:  self.vy += s['ACCELERATION']
        
        # Apply room effects
        self.vx += wind[0]
        self.vy += wind[1]
        
        # Apply movement
        self.canvas.move(self.rect, self.vx, self.vy)
        
        # Apply momentum
        self.vx *= momentum
        self.vy *= momentum
        
        # Get player position
        x0, y0, x1, y1 = self.canvas.coords(self.rect)
        player_center_x = (x0 + x1) / 2
        player_center_y = (y0 + y1) / 2
        
        # Check collectible collisions
        self._check_collectibles(player_center_x, player_center_y)
        
        # Check obstacle collisions
        self._check_obstacles(player_center_x, player_center_y)
        
        # Check wall collisions
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

    def _check_collectibles(self, px, py):
        idx = self.game.current
        spec = self.game.specs[idx]
        panel = self.game.current_panel
        
        # Check if player collides with any collectibles
        to_remove = []
        for i, (x, y) in enumerate(spec['collectibles']):
            dist = math.sqrt((px - x)**2 + (py - y)**2)
            if dist < 10:  # Collision threshold
                to_remove.append(i)
                # Remove the visual representation
                if i < len(panel.collectibles):
                    panel.canvas.delete(panel.collectibles[i])
                # Update score
                self.score += 10
                self.game.update_score()
        
        # Remove collected items (in reverse order to avoid index issues)
        for i in sorted(to_remove, reverse=True):
            if i < len(spec['collectibles']):
                del spec['collectibles'][i]
        
        # Update collectibles list
        panel.collectibles = [c for j, c in enumerate(panel.collectibles) if j not in to_remove]

    def _check_obstacles(self, px, py):
        idx = self.game.current
        spec = self.game.specs[idx]
        
        # Check if player collides with any obstacles
        for x, y, size in spec['obstacles']:
            dist = math.sqrt((px - x)**2 + (py - y)**2)
            if dist < (size/2 + self.settings['PIXEL_SIZE']/2):  # Collision threshold
                # Bounce away from obstacle
                angle = math.atan2(py - y, px - x)
                force = 3.0
                self.vx += math.cos(angle) * force
                self.vy += math.sin(angle) * force


class Game:
    def __init__(self, settings):
        self.settings = settings
        self.specs = generate_specs(settings['TOTAL_ROOMS'])
        self.current = 0
        self.next_entry_coords = None
        self.start_time = None
        self.root = None
        self.timer_window = None
        self.score_window = None
        self.panels = []
        self.player = None

    def start(self):
        self._countdown()

    def _countdown(self):
        count = 3  # Increased countdown from 1 to 3
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
        
        # timer window
        self.timer_window = tk.Toplevel(self.root)
        self.timer_window.overrideredirect(True)
        self.timer_window.geometry(f"100x30+{sw-110}+10")
        self.timer_window.configure(bg='black')
        self.timer_label = tk.Label(self.timer_window, text="0.0s",
                                     bg='black', fg='white', font=(None, 12))
        self.timer_label.pack()
        
        # score window
        self.score_window = tk.Toplevel(self.root)
        self.score_window.overrideredirect(True)
        self.score_window.geometry(f"100x30+{sw-110}+50")
        self.score_window.configure(bg='black')
        self.score_label = tk.Label(self.score_window, text="Score: 0",
                                     bg='black', fg='white', font=(None, 12))
        self.score_label.pack()
        
        # progress window
        self.progress_window = tk.Toplevel(self.root)
        self.progress_window.overrideredirect(True)
        self.progress_window.geometry(f"150x30+{sw-160}+90")
        self.progress_window.configure(bg='black')
        self.progress_label = tk.Label(self.progress_window, text="Room: 0/" + str(s['TOTAL_ROOMS']-1),
                                     bg='black', fg='white', font=(None, 12))
        self.progress_label.pack()
        
        # panels
        self.panels = [Panel(self.root, settings=s) for _ in range(5)]
        # mark middle as main
        self.panels[2] = Panel(self.root, is_main=True, settings=s)
        self.player = Player(self, s)
        for p in self.panels: self.player.bind(p.window)

        self._update_timer()
        self.update_score()
        self.update_progress()
        
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
                   
        self.coords = coords
        self._show()
        self.panels[2].window.focus_force()
        self.player.spawn(self.specs[0]); self.player.update()
        self.root.mainloop()

    def _update_timer(self):
        elapsed = time.time() - self.start_time
        
        # Set color based on time compared to target
        target = self.settings['TARGET_TIME']
        if elapsed > target:
            color = 'red'  # Over time
        elif elapsed > target * 0.8:
            color = 'yellow'  # Getting close to target time
        else:
            color = 'lime'  # Well under target time
            
        self.timer_label.config(text=f"{elapsed:.1f}s", fg=color)
        self.timer_window.after(100, self._update_timer)
    
    def update_score(self):
        self.score_label.config(text=f"Score: {self.player.score}")
    
    def update_progress(self):
        self.progress_label.config(text=f"Room: {self.current}/{len(self.specs)-1}")

    @property
    def current_panel(self):
        return self.panels[2]

    def _show(self):
        # Prepare all windows first before showing/hiding any
        rels = [-2, -1, 0, 1, 2]
        for slot, rel in enumerate(rels):
            idx = self.current + rel
            pnl = self.panels[slot]
            if 0 <= idx < len(self.specs):
                x, y = self.coords[idx]
                pnl.render(self.specs[idx], f"Room {idx}", x, y)
        
        # Update progress indicator
        self.update_progress()
            
        # Then show or hide windows as needed
        for slot, rel in enumerate(rels):
            idx = self.current + rel
            pnl = self.panels[slot]
            if 0 <= idx < len(self.specs):
                pnl.show()
                if rel == 0: 
                    pnl.window.focus_force()
            else:
                pnl.hide()

    def change(self, new_idx):
        self.current = new_idx
        if new_idx == len(self.specs)-1:
            # end game and show results
            elapsed = time.time() - self.start_time
            self.show_results(elapsed)
            return
        self._show()
        self.player.spawn(self.specs[new_idx])
        self.panels[2].window.focus_force()
        self.player.update()
    
    def show_results(self, elapsed):
        # Create results window
        results = tk.Toplevel(self.root)
        results.title("Game Complete!")
        
        # Position in center of screen
        sw, sh = results.winfo_screenwidth(), results.winfo_screenheight()
        w, h = 400, 300
        x, y = (sw-w)//2, (sh-h)//2
        results.geometry(f"{w}x{h}+{x}+{y}")
        
        # Calculate final score
        time_bonus = max(0, self.settings['TARGET_TIME'] - elapsed) * 5
        final_score = self.player.score + int(time_bonus)
        
        # Format time
        minutes = int(elapsed // 60)
        seconds = elapsed % 60
        time_str = f"{minutes}m {seconds:.1f}s"
        
        # Show results
        tk.Label(results, text="Game Complete!", font=('Arial', 20)).pack(pady=10)
        tk.Label(results, text=f"Time: {time_str}", font=('Arial', 14)).pack(pady=5)
        tk.Label(results, text=f"Items Collected: {self.player.score // 10}", font=('Arial', 14)).pack(pady=5)
        tk.Label(results, text=f"Time Bonus: +{int(time_bonus)}", font=('Arial', 14)).pack(pady=5)
        tk.Label(results, text=f"Final Score: {final_score}", font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Button to return to menu
        btn = tk.Button(results, text="Return to Menu", font=('Arial', 14),
                       command=lambda: (results.destroy(), self.root.destroy(), Application().run()))
        btn.pack(pady=20)


class Application:
    def __init__(self):
        self.settings = DEFAULTS.copy()

    def run(self):
        self.show_menu()

    def show_menu(self):
        self.menu = tk.Tk()
        self.menu.title("Pizel Game Settings")
        sw, sh = self.menu.winfo_screenwidth(), self.menu.winfo_screenheight()
        mw, mh = 400, 400  # Made taller to accommodate more settings
        mx, my = (sw-mw)//2, (sh-mh)//2
        self.menu.geometry(f"{mw}x{mh}+{mx}+{my}")
        
        # Title
        tk.Label(self.menu, text="Pizel Game", font=('Arial', 18, 'bold')).pack(pady=10)
        
        # Settings frame
        frm = tk.Frame(self.menu)
        frm.pack(padx=20, pady=10)
        self.entries = {}
        
        # Create settings entries
        for i,(key,val) in enumerate(self.settings.items()):
            tk.Label(frm, text=key, anchor='e', width=20).grid(row=i, column=0, sticky='e', pady=2)
            ent = tk.Entry(frm, width=10)
            ent.insert(0, str(val))
            ent.grid(row=i, column=1, padx=5, pady=2)
            self.entries[key] = ent
        
        # Instructions
        instructions = """
        • Move using arrow keys
        • Collect items for points
        • Avoid obstacles
        • Reach the final room as fast as possible
        • Different rooms have different properties
        """
        tk.Label(self.menu, text=instructions, justify=tk.LEFT).pack(pady=10)
        
        # Start button
        btn = tk.Button(self.menu, text="Start Game", font=('Arial', 14, 'bold'),
                        bg='green', fg='white', command=self._on_start)
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