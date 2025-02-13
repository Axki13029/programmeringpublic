import pygame
import math
import random
import sys

# --- Konfiguration ---
WIDTH, HEIGHT = 800, 600         # Fönsterstorlek
FPS = 60                         # Uppdateringsfrekvens

# Bränsle (fuel) – vi skapar ett antal stationära bränsleelement.
NUM_FUEL = 20

# Fissionsegenskaper:
FISSION_PROBABILITY = 0.7        # Sannolikhet att en fission utlöses vid neutron-kollision
FISSION_YIELD = 2                # Antal nya neutroner som slås ut vid en fission
NEUTRON_SPEED = 200              # Neutronens hastighet i pixel/s

# Kontrollstav:
# Om kontrollstavarna är insatta (toggla med mellanslag) absorberas alla neutroner i ett område.
CONTROL_ROD_ACTIVE = False       # Globalt läge (kan ändras med mellanslag)
# Definiera kontrollstavsområdet (rektangel)
CONTROL_ROD_RECT = pygame.Rect(0, 0, WIDTH, HEIGHT // 3)

# Fysik:
# Neutronerna studsar mot väggarna.
# Bränsleelementen är stationära.

# Färger
BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY   = (100, 100, 100)

# --- Klasser ---

class FuelPellet:
    """Ett stationärt bränsleelement. Det ritas som en cirkel och har en viss radie."""
    def __init__(self, pos, radius=20, color=YELLOW):
        self.pos = pygame.Vector2(pos)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), int(self.radius))

class Neutron:
    """En neutron som rör sig runt i reaktorn."""
    def __init__(self, pos, vel):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.radius = 3  # Liten partikel

    def update(self, dt):
        self.pos += self.vel * dt

        # Studsa mot väggarna
        if self.pos.x - self.radius < 0:
            self.pos.x = self.radius
            self.vel.x *= -1
        if self.pos.x + self.radius > WIDTH:
            self.pos.x = WIDTH - self.radius
            self.vel.x *= -1
        if self.pos.y - self.radius < 0:
            self.pos.y = self.radius
            self.vel.y *= -1
        if self.pos.y + self.radius > HEIGHT:
            self.pos.y = HEIGHT - self.radius
            self.vel.y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.pos.x), int(self.pos.y)), self.radius)

# --- Hjälpfunktion: Fission (kollision mellan neutron och bränsle) ---
def attempt_fission(neutron, fuel):
    """
    Om en neutron kolliderar med ett bränsleelement, 
    med viss sannolikhet utlöses fission som släpper ut FISSION_YIELD nya neutroner.
    """
    # Kolla om neutronen träffar bränslet
    dist = (neutron.pos - fuel.pos).length()
    if dist <= fuel.radius + neutron.radius:
        if random.random() < FISSION_PROBABILITY:
            new_neutrons = []
            for _ in range(FISSION_YIELD):
                # Skapa en ny neutron med riktning slumpmässigt runt 360 grader.
                angle = random.uniform(0, 2 * math.pi)
                vel = pygame.Vector2(NEUTRON_SPEED * math.cos(angle), NEUTRON_SPEED * math.sin(angle))
                new_neutrons.append(Neutron(fuel.pos, vel))
            return new_neutrons
    return []

# --- Hjälpfunktion: Hantera kollision mellan neutroner (elastisk kollision) ---
def elastic_collision(n1, n2):
    delta = n1.pos - n2.pos
    dist = delta.length()
    if dist == 0:
        return
    normal = delta / dist
    rel_vel = n1.vel - n2.vel
    vel_along_normal = rel_vel.dot(normal)
    if vel_along_normal >= 0:
        return
    # Antag enhetsmassa för neutroner (eller mass=1)
    impulse = 2 * vel_along_normal  # Eftersom m1 = m2 = 1
    n1.vel -= impulse * normal
    n2.vel += impulse * normal
    # Separera neutronerna lite för att undvika att de "klibbar"
    overlap = (n1.radius + n2.radius) - dist
    if overlap > 0:
        correction = normal * (overlap / 2)
        n1.pos += correction
        n2.pos -= correction

# --- Huvudprogram ---

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fissionssimulator med kontrollstavar")
clock = pygame.time.Clock()

# Skapa bränsleelementen (spridda över skärmen)
fuels = []
for i in range(NUM_FUEL):
    x = random.uniform(50, WIDTH - 50)
    y = random.uniform(50, HEIGHT - 50)
    fuels.append(FuelPellet((x, y), radius=random.uniform(15, 25)))

# Skapa initiala neutroner
neutrons = []
# Starta med några få neutroner
for _ in range(3):
    pos = (random.uniform(100, WIDTH - 100), random.uniform(100, HEIGHT - 100))
    angle = random.uniform(0, 2*math.pi)
    vel = pygame.Vector2(NEUTRON_SPEED * math.cos(angle), NEUTRON_SPEED * math.sin(angle))
    neutrons.append(Neutron(pos, vel))

# Variabel för att skydda mot runaway
reactivity = 1.0  # Om denna faktor ökar blir reaktionen "runaway"

running = True
while running:
    dt = clock.tick(FPS) / 1000.0  # dt i sekunder
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Tryck på mellanslag för att toggla kontrollstavar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                CONTROL_ROD_ACTIVE = not CONTROL_ROD_ACTIVE

    # Uppdatera neutronerna
    new_neutrons = []
    for neutron in neutrons:
        neutron.update(dt)
        new_neutrons.append(neutron)
    neutrons = new_neutrons

    # Kontrollera kollisioner mellan neutroner (elastisk kollision)
    for i in range(len(neutrons)):
        for j in range(i + 1, len(neutrons)):
            n1 = neutrons[i]
            n2 = neutrons[j]
            if n1.pos.distance_to(n2.pos) <= (n1.radius + n2.radius):
                elastic_collision(n1, n2)

    # Kontrollera fission vid kollision mellan neutroner och bränsle
    spawned_neutrons = []
    for neutron in neutrons:
        for fuel in fuels:
            new_ns = attempt_fission(neutron, fuel)
            if new_ns:
                # Öka reaktiviteten vid fission
                reactivity *= 1.05
            spawned_neutrons.extend(new_ns)
    neutrons.extend(spawned_neutrons)

    # Om kontrollstavar är aktiva, absorbera neutroner i CONTROL_ROD_RECT
    if CONTROL_ROD_ACTIVE:
        neutrons = [n for n in neutrons if not CONTROL_ROD_RECT.collidepoint(n.pos.x, n.pos.y)]
        # Minska reaktiviteten när kontrollstavarna är insatta
        reactivity *= 0.95

    # Skydda mot runaway: om antalet neutroner blir för högt, minska deras hastighet
    if len(neutrons) > 100:
        for n in neutrons:
            n.vel *= 0.9

    # Rita upp
    screen.fill(BLACK)

    # Rita bränsleelementen
    for fuel in fuels:
        fuel.draw(screen)

    # Rita neutronerna
    for neutron in neutrons:
        neutron.draw(screen)

    # Rita kontrollstavsområdet om aktivt (en halvtransparent rektangel)
    if CONTROL_ROD_ACTIVE:
        rod_surface = pygame.Surface((CONTROL_ROD_RECT.width, CONTROL_ROD_RECT.height))
        rod_surface.set_alpha(150)
        rod_surface.fill(GRAY)
        screen.blit(rod_surface, (CONTROL_ROD_RECT.x, CONTROL_ROD_RECT.y))

    # Visa statistik
    font = pygame.font.SysFont(None, 24)
    stats = f"Neutrons: {len(neutrons)}  Reactivity: {reactivity:.2f}  Control Rods: {'ON' if CONTROL_ROD_ACTIVE else 'OFF'}"
    text = font.render(stats, True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
