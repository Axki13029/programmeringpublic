import math
import random
import time
import os

# För att fånga tangenttryckningar på Windows (om du kör på annat system behövs annan lösning)
try:
    import msvcrt
    has_msvcrt = True
except ImportError:
    has_msvcrt = False

# Definiera rutans storlek (antal kolumner och rader)
WIDTH = 40
HEIGHT = 20

class Atom:
    def __init__(self, x, y, vx, vy):
        self.x = x      # x-position (float)
        self.y = y      # y-position (float)
        self.vx = vx    # x-hastighet
        self.vy = vy    # y-hastighet

    def update(self, dt):
        """Uppdaterar atomens position med tiden dt och studsar mot väggarna."""
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Studsa mot vänster eller höger vägg
        if self.x < 0:
            self.x = -self.x
            self.vx = -self.vx
        if self.x >= WIDTH:
            self.x = 2*WIDTH - self.x - 1
            self.vx = -self.vx

        # Studsa mot topp eller botten
        if self.y < 0:
            self.y = -self.y
            self.vy = -self.vy
        if self.y >= HEIGHT:
            self.y = 2*HEIGHT - self.y - 1
            self.vy = -self.vy

# Lista över atomer i simuleringen
atoms = []

def add_atom():
    """Skapar en atom med slumpmässig position och hastighet och lägger till den i listan."""
    x = random.uniform(0, WIDTH - 1)
    y = random.uniform(0, HEIGHT - 1)
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(1, 3)
    vx = math.cos(angle) * speed
    vy = math.sin(angle) * speed
    atoms.append(Atom(x, y, vx, vy))

# Skapa ett antal atomer vid start (t.ex. 5 stycken)
initial_atoms = 5
for _ in range(initial_atoms):
    add_atom()

def draw():
    """Ritar ut rutans nuvarande tillstånd i konsolen."""
    # Skapa en tom 2D-lista för rutan
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for atom in atoms:
        ix = int(atom.x)
        iy = int(atom.y)
        if 0 <= ix < WIDTH and 0 <= iy < HEIGHT:
            grid[iy][ix] = 'O'
    
    # Rita ut rutans kant
    print('+' + '-' * WIDTH + '+')
    for row in grid:
        print('|' + ''.join(row) + '|')
    print('+' + '-' * WIDTH + '+')
    print("Antal atomer:", len(atoms))
    print("Tryck '+' för att lägga till en atom, '-' för att ta bort en atom, 'q' för att avsluta.")

# Tidssteg för simuleringen
dt = 0.1

# Huvudloopen
while True:
    # Uppdatera varje atoms position
    for atom in atoms:
        atom.update(dt)

    # Kolla efter kollisioner mellan atomer och utför fission
    # Om två atomer kommer inom ett visst avstånd (här < 1.0) sker en fissionhändelse med 50 % chans.
    to_add = []         # Lista för nya atomer (fissionprodukter)
    removal_indices = set()  # Index på atomer som ska tas bort p.g.a. fission

    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            a = atoms[i]
            b = atoms[j]
            dx = a.x - b.x
            dy = a.y - b.y
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < 1.0:
                # Fission sker med 50 % sannolikhet vid kollision
                if random.random() < 0.5:
                    # Välj att fissionera den ena atomen (här: atom a)
                    if i not in removal_indices:
                        removal_indices.add(i)
                        # Vid fission skapas två nya atomer med slumpmässiga riktningar
                        for _ in range(2):
                            angle = random.uniform(0, 2 * math.pi)
                            speed = random.uniform(1, 3)
                            vx = math.cos(angle) * speed
                            vy = math.sin(angle) * speed
                            to_add.append(Atom(a.x, a.y, vx, vy))
    
    # Ta bort de atomer som fissionerats
    atoms = [atom for idx, atom in enumerate(atoms) if idx not in removal_indices]
    # Lägg till de nya atomerna
    atoms.extend(to_add)

    # Rensa konsolen (använd 'cls' på Windows, 'clear' på Unix-system)
    os.system('cls' if os.name == 'nt' else 'clear')
    draw()

    # Kontrollera om användaren trycker på någon tangent
    if has_msvcrt:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            # För att kunna läsa in bokstavstecken på rätt sätt (både stora och små)
            try:
                key_char = key.decode('utf-8')
            except:
                key_char = ''

            if key_char == '+':
                add_atom()
            elif key_char == '-':
                if atoms:
                    atoms.pop()  # Ta bort en atom (sista i listan)
            elif key_char.lower() == 'q':
                break

    time.sleep(dt)
