import pygame, sys, random

# --- CONSTANTS ---
SIZE = WIDTH, HEIGHT = 600, 800
FPS = 60

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0

# --- Set up pygame window ---
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("FOOTBALL")
clock = pygame.time.Clock()


radius = 100
gravity = 0
xvel = 0
yvel = 0
x, y = WIDTH//2, HEIGHT-radius

font = pygame.font.Font(None, 70)

def draw_ball(x, y):
	pygame.draw.circle(screen, RED, (x, y), radius, 0)


# --- Game loop ---
score = 0
highscore = [0]
with open("highscore.txt","r") as t:
	t = t.readline()
	t = t.split(" ")
	print(t)
	h = [int(i) for i in t if i.isdigit()]
	highscore += h
	print(highscore)
while True:
	# --- Code that executes on each frame ---
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			with open("highscore.txt", "a") as f:
				f.write(str(max(highscore))+" ")
				f.close()
			pygame.quit(); sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mousex, mousey = pygame.mouse.get_pos()
			distance = (((mousex - x)**2) + ((mousey - y)**2))**0.5
			if distance < radius:
				score = score + 1
				yvel = random.randrange(-20, -10)
				xvel = (x - mousex)/4
				gravity = 0.3
				highscore.append(score)

	if x <= radius or x >= WIDTH-radius:
		xvel = -xvel

	if y > HEIGHT - radius:
		gravity = 0
		score = 0
		xvel = 0
		yvel = 0
		x, y = WIDTH//2, HEIGHT-radius

	text = font.render("Current: {} High: {}".format(score, max(highscore)), True, WHITE)
	text_pos = text.get_rect(center=(WIDTH/2, 50))
	screen.blit(text, text_pos)


	# --- Game logic here ---
	yvel += gravity
	x += xvel
	y += yvel
	draw_ball(int(x), int(y))

	# --- Update the screen (Draw to the screen) ---
	pygame.display.update()
	clock.tick(FPS)