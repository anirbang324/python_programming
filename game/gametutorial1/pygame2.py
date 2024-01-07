#Main Pkgs
import pygame, random
#Initialization
pygame.init()
def main():
    #screen setup
    WIDTH = 900
    HEIGHT = 600
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("PyGame Foundations 2")
    screen.fill(pygame.Color("Gray"))

    #load images - outside of the game loop (avoid lag)
    cat = pygame.image.load("cat.jpg")
    cat = pygame.transform.scale(cat,(400,300)) #scale returns a "surface"
    dog = pygame.image.load("dog.jpg")
    dog = pygame.transform.scale(dog, (400,300)) #scale returns a "surface"
    puppy = pygame.image.load("puppy.jpg")
    puppy = pygame.transform.scale(puppy, (400,300)) #scale returns a "surface"
    kitten = pygame.image.load("kitten.jpg")
    kitten = pygame.transform.scale(kitten, (400,300)) #scale returns a "surface"
    images = {"dog":dog, "cat":cat, "puppy":puppy, "kitten":kitten}
    #img = dog
    img = random.choice([dog, puppy, kitten, cat])
    screen.blit(img,(0,0))
    imgX = 0
    imgY = 0

    #Input Box
    inputBox = InputBox(600, 100, 140, 32)

    #Variables
    running = True
    MAX_FPS = 60
    mouseStartX = mouseStartY = mouseEndX = mouseEndY = 0
    text = ''
    focus = None

    #clock setup
    clock = pygame.time.Clock()

    #Game Loop
    while running:

        #Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #imgX, imgY = pygame.mouse.get_pos()

                if img.get_rect().move(imgX, imgY).collidepoint(pygame.mouse.get_pos()):
                    focus = 'image'
                    mouseStartX, mouseStartY = pygame.mouse.get_pos()
                else:
                    focus = None
            elif focus == 'image' and event.type == pygame.MOUSEBUTTONUP:
                mouseEndX, mouseEndY = pygame.mouse.get_pos()
                deltaMouseX = mouseEndX - mouseStartX
                deltaMouseY = mouseEndY - mouseStartY
                imgX += deltaMouseX
                imgY += deltaMouseY


            # #single step (pixel) movement
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         imgY -= 1
            #     elif event.key == pygame.K_s:
            #         imgY += 1
            #     elif event.key == pygame.K_a:
            #         imgX -= 1
            #     elif event.key == pygame.K_d:
            #         imgX += 1


            #Continuous movement with key held down
            if focus == "image":
                keys = pygame.key.get_pressed() #returns the list of all keys [0,1]
                if keys[pygame.K_w]:
                    imgY -= 3
                if keys[pygame.K_s]:
                    imgY += 3
                if keys[pygame.K_a]:
                    imgX -= 3
                if keys[pygame.K_d]:
                    imgX += 3


            try:
                text = inputBox.handle_event(event).lower()
                if text in images:
                    img = images[text]
            except:
                pass
                


        #Update Objects
        inputBox.update()
                

        #Update Graphics
        screen.fill(pygame.Color("Gray"))
        screen.blit(img, (imgX, imgY))
        inputBox.draw(screen)
        pygame.display.flip()


        #Pause for frames
        clock.tick(MAX_FPS)





COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

#from https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    output = self.text
                    self.text = ''
                    self.txt_surface = FONT.render(self.text, True, self.color)
                    return output
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


main()