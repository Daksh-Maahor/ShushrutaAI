import pygame
pygame.init()

SIZE = 640

WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Shushruta")
ICON = pygame.image.load('icon.jpg')
pygame.display.set_icon(ICON)

BANNER = pygame.transform.scale((temp := pygame.image.load('banner.jpg').convert()), (temp.get_width() // (3/2), temp.get_height() // (3/2)))

DMAP = [
    {
        "disease" : 'Arthritis',
        "symptoms" : 0b11111110000000000000,
        "descp" : """Arthritis is the swelling and tenderness 
                     of one or more joints. The main symptoms 
                     of arthritis are joint pain and stiffness, 
                     which typically worsen with age. The most 
                     common types of arthritis are 
                     osteoarthritis and rheumatoid arthritis. 
                     Osteoarthritis causes cartilage — the 
                     hard, slippery tissue that covers the ends 
                     of bones where they form a joint — to 
                     break down. Rheumatoid arthritis is a 
                     disease in which the immune system attacks 
                     the joints, beginning with the lining of 
                     joints.""",
    },
    {
        "disease" : 'Backache',
        "symptoms" : 0b01111110000000000000,
        "descp" : """Back pain can have causes that aren\'t due 
                     to underlying disease. Examples include 
                     overuse such as working out or lifting too 
                     much, prolonged sitting and lying down, 
                     sleeping in an uncomfortable position or 
                     wearing a poorly fitting backpack.""",
    },
    {
        "disease" : 'Hypotension',
        "symptoms" : 0b00000011111100000000,
        "descp" : """Causes of hypotension include dehydration, 
                     long-term bed rest, pregnancy, certain 
                     medical conditions and some medications. 
                     This type of low blood pressure is common 
                     in older adults. Postprandial hypotension. 
                     This drop in blood pressure occurs 1 to 2 
                     hours after eating.""",
    },
    {
        "disease" : 'Chikungunya',
        "symptoms" : 0b11111110000011110000,
        "descp" : """Chikungunya virus is spread to people by 
                     the bite of an infected mosquito. The most 
                     common symptoms of infection are fever and 
                     joint pain. Other symptoms may include 
                     headache, muscle pain, joint swelling, or 
                     rash. Outbreaks have occurred in countries 
                     in Africa, Americas, Asia, Europe, and the 
                     Caribbean, Indian and Pacific Oceans. 
                     There is a risk the virus will be spread 
                     to unaffected areas by infected travelers. 
                     There is currently no vaccine to prevent 
                     or medicine to treat chikungunya virus 
                     infection. Travelers can protect 
                     themselves by preventing mosquito bites. 
                     When traveling to countries with 
                     chikungunya virus, use insect repellent; 
                     wear long-sleeved shirts and pants; and 
                     stay in places with air conditioning or 
                     that use window and door screens.""",
    },
    {
        "disease" : 'Chickenpox',
        "symptoms" : 0b00000110000000111000,
        "descp" : """Chickenpox is an infection caused by the 
                     varicella-zoster virus. It causes an itchy 
                     rash with small, fluid-filled blisters. 
                     Chickenpox is highly contagious to people 
                     who haven\'t had the disease or been 
                     vaccinated against it. Today, a vaccine is 
                     available that protects children against 
                     chickenpox. Routine vaccination is 
                     recommended by the U.S. Centers for Disease 
                     Control and Prevention (CDC).""",
    },
    {
        "disease" : 'Diarrhea',
        "symptoms" : 0b00000101000000000100,
        "descp" : """Diarrhea — loose, watery and possibly more-
                     frequent bowel movements — is a common 
                     problem. It may be present alone or be 
                     associated with other symptoms, such as 
                     nausea, vomiting, abdominal pain or weight 
                     loss. Luckily, diarrhea is usually short-
                     lived, lasting no more than a few days. But 
                     when diarrhea lasts beyond a few days into 
                     weeks, it usually indicates that there\'s 
                     another problem — such as irritable bowel 
                     syndrome (IBS) or a more serious disorder, 
                     including persistent infection, celiac 
                     disease or inflammatory bowel disease (IBD).""",
    },
    {
        "disease" : 'Malaria',
        "symptoms" : 0b00000101000100000100,
        "descp" : """Malaria is a disease caused by a parasite. 
                     The parasite is spread to humans through 
                     the bites of infected mosquitoes. People 
                     who have malaria usually feel very sick 
                     with a high fever and shaking chills. While 
                     the disease is uncommon in temperate 
                     climates, malaria is still common in 
                     tropical and subtropical countries. Each 
                     year nearly 290 million people are infected 
                     with malaria, and more than 400,000 people 
                     die of the disease.""",
    },
    {
        "disease" : 'Jaundice',
        "symptoms" : 0b00000101000000100010,
        "descp" : """Jaundice is a condition in which a 
                     yellowish tinge appears on the skin, mucous 
                     membranes, and the whites of the eye. Body 
                     fluids may also change color. Jaundice 
                     frequently indicates a problem with the 
                     liver or bile ducts. When the liver is not 
                     working properly, it can cause a waste 
                     material called bilirubin to build up in 
                     the blood. With moderate bilirubin levels, 
                     a person’s skin, eyes, and mucous 
                     membranes can turn yellow. As it progresses
                     , the color can also change from yellow to 
                     green. The green color occurs due to 
                     biliverdin, the green pigment present in 
                     bile. Jaundice can develop in people of all 
                     ages and is normally the result of an 
                     underlying condition. Newborns and older 
                     adults have the highest likelihood of 
                     developing jaundice.""",
    },
    {
        "disease" : 'Anemia',
        "symptoms" : 0b00000010010010100001,
        "descp" : """Anemia is a condition in which you lack 
                     enough healthy red blood cells to carry 
                     adequate oxygen to your body\'s tissues. 
                     Having anemia, also referred to as low 
                     hemoglobin, can make you feel tired and 
                     weak. It is commonly caused by deficiency 
                     of iron in diet. There are many forms of 
                     anemia, each with its own cause. Anemia can 
                     be temporary or long term and can range 
                     from mild to severe. In most cases, anemia 
                     has more than one cause. See your doctor if 
                     you suspect that you have anemia. It can be 
                     a warning sign of serious illness.""",
    }
]

SYMPTOMS_LIST = [
    'Swelling',
    'Joint Inflammation',
    'Stiffness',
    'Tenderness',
    'Weight Loss',
    'Fever',
    'Weakness',
    'Pain',
    'Malfunctioning in Brain',
    'Shortness of Breath',
    'Fast Breathing',
    'Cold',
    'Faint',
    'Bodyache',
    'Headache',
    'Maculopapular Rash',
    'Red Bumps',
    'Vomiting',
    'Coloration of Skin and Eyes',
    'Fatigue or Tiredness',
]

#fonts

FONT = pygame.font.SysFont('comicsans', 30)

#COLORS

WHITE = 255, 255, 255
GRAY = 128, 128, 128
DARKGRAY = 64, 64, 64
BLACK = 0, 0, 0

#constants

SCROLL_VAL = 0
NUM_DISEASES = 5

#method definitions

def changeState(state):...

def advance_process(num):...

def text_objects(text, surfaceH):...

#classes

class State:
    def tick(self, mouseX, mouseY, mouseClicked):
        pass
    
    def render(self):
        pass
    
class MenuState(State):
    def __init__(self):
        self.start_btn = pygame.rect.Rect(SIZE // 2 - 100, SIZE // 2 - 30 + 150, 200, 60)
        self.btn_color = GRAY
    
    def tick(self, mouseX, mouseY, mouseClicked):
        if self.start_btn.collidepoint(mouseX, mouseY):
            self.btn_color = DARKGRAY
            
            if mouseClicked:
                changeState(APPSTATE)
        else:
            self.btn_color = GRAY
    
    def render(self):
        pygame.draw.rect(WINDOW, WHITE, (0, 0, SIZE, SIZE))
        
        WINDOW.blit(BANNER, ((SIZE - BANNER.get_width())//2, 50))
        pygame.draw.rect(WINDOW, self.btn_color, self.start_btn)
        WINDOW.blit((line := FONT.render("Diagnose", 1, WHITE)), (self.start_btn[0] + (self.start_btn[2] - line.get_width())//2, self.start_btn[1] + (self.start_btn[3] - line.get_height())//2, line.get_width(), line.get_height()))
        
class AppState(State):
    def __init__(self) -> None:
        self.symptom_counter = 0
        
        self.response = 0
        
        self.yes_button = pygame.rect.Rect(60, 400, 200, 50)
        self.no_button = pygame.rect.Rect(380, 400, 200, 50)
        
        self.y_btn_color = GRAY
        self.n_btn_color = GRAY
    
    def tick(self, mouseX, mouseY, mouseClicked):
        if self.yes_button.collidepoint(mouseX, mouseY):
            self.y_btn_color = DARKGRAY
        else:
            self.y_btn_color = GRAY
            
        if self.no_button.collidepoint(mouseX, mouseY):
            self.n_btn_color = DARKGRAY
        else:
            self.n_btn_color = GRAY
        
        if mouseClicked:
            if (self.yes_button.collidepoint(mouseX, mouseY)):
                
                if self.symptom_counter < len(SYMPTOMS_LIST):
                    self.response *= 2
                    self.response += 1
                    
                self.symptom_counter += 1
            elif (self.no_button.collidepoint(mouseX, mouseY)):
                
                if self.symptom_counter < len(SYMPTOMS_LIST):
                    self.response *= 2
                    
                self.symptom_counter += 1
                
        
        if self.symptom_counter >= len(SYMPTOMS_LIST):
            changeState(DIAGNOSISSTATE)
    
    def render(self):
        global SIZE
        pygame.draw.rect(WINDOW, WHITE, (0, 0, SIZE, SIZE))
        
        WINDOW.blit((line := FONT.render("Are you experiencing?", 1, BLACK)), ((SIZE - line.get_width())//2, 90, SIZE, SIZE))
        line = FONT.render(SYMPTOMS_LIST[self.symptom_counter], 1, BLACK)
        WINDOW.blit(line, ((SIZE - line.get_width()) // 2, 300, SIZE, SIZE))
        
        pygame.draw.rect(WINDOW, self.y_btn_color, self.yes_button)
        WINDOW.blit(FONT.render("Yes", 1, WHITE), (self.yes_button[0] + 75, self.yes_button[1], self.yes_button[2], self.yes_button[3]))
        pygame.draw.rect(WINDOW, self.n_btn_color, self.no_button)
        WINDOW.blit(FONT.render("No", 1, WHITE), (self.no_button[0] + 75, self.no_button[1], self.no_button[2], self.no_button[3]))
        
    def reset(self):
        self.symptom_counter = 0
        self.response = 0
        
class DiagnosisState(State):
    def __init__(self) -> None:
        self.btn = pygame.rect.Rect((SIZE-200)//2, (SIZE-50)//2, 200, 50)
        
        self.btn_color = GRAY
        
    def tick(self, mouseX, mouseY, mouseClicked):
        global RESULTSTATE
        if self.btn.collidepoint(mouseX, mouseY):
            self.btn_color = DARKGRAY
            
            if mouseClicked:
                RESULTSTATE.and_values = advance_process(APPSTATE.response)
                changeState(RESULTSTATE)
        else:
            self.btn_color = GRAY
    
    def render(self):
        global SIZE
        pygame.draw.rect(WINDOW, WHITE, (0, 0, SIZE, SIZE))
        
        WINDOW.blit((line := FONT.render('Your diagnosis is ready', True, BLACK)), ((SIZE - line.get_width())//2, 90, SIZE, SIZE))
        
        pygame.draw.rect(WINDOW, self.btn_color, self.btn)
        WINDOW.blit((line := FONT.render("Show Results", 1, WHITE)), (self.btn[0] + (self.btn[2] - line.get_width())//2, self.btn[1] + (self.btn[3] - line.get_height())//2, line.get_width(), line.get_height()))
        
        
class ResultState(State):
    def __init__(self) -> None:
        self.and_values = None
        self.current_idx = 0
        
        self.left_btn = pygame.rect.Rect(20, 500, 50, 50)
        self.right_btn = pygame.rect.Rect(570, 500, 50, 50)
        self.home_btn = pygame.rect.Rect((SIZE - 100)//2, 500, 100, 50)
        
        self.left_col = GRAY
        self.right_col = GRAY
        self.home_col = GRAY
        self.current_symptom = None
        
    def tick(self, mouseX, mouseY, mouseClicked):
        global SCROLL_VAL, NUM_DISEASES
        
        if (self.left_btn.collidepoint(mouseX, mouseY)):
            self.left_col = DARKGRAY
        else:
            self.left_col = GRAY
            
        if (self.right_btn.collidepoint(mouseX, mouseY)):
            self.right_col = DARKGRAY
        else:
            self.right_col = GRAY
            
        if (self.home_btn.collidepoint(mouseX, mouseY)):
            self.home_col = DARKGRAY
        else:
            self.home_col = GRAY
            
        if mouseClicked:
            if (self.left_btn.collidepoint(mouseX, mouseY)):
                if self.current_idx > 0:
                    self.current_idx -= 1
                else:
                    self.current_idx = min(NUM_DISEASES, len(self.and_values)) - 1
                SCROLL_VAL = 0
            elif (self.right_btn.collidepoint(mouseX, mouseY)):
                if self.current_idx < min(NUM_DISEASES, len(self.and_values)) - 1:
                    self.current_idx += 1
                else:
                    self.current_idx = 0
                SCROLL_VAL = 0
            elif (self.home_btn.collidepoint(mouseX, mouseY)):
                SCROLL_VAL = 0
                APPSTATE.reset()
                changeState(MENUSTATE)
    
    def render(self):
        global SCROLL_VAL, SIZE
        
        self.current_symptom = self.and_values[self.current_idx]
        pygame.draw.rect(WINDOW, WHITE, (0, 0, SIZE, SIZE))
        
        pygame.draw.rect(WINDOW, self.left_col, self.left_btn)
        WINDOW.blit((line := FONT.render('<', True, WHITE)), (self.left_btn[0] + (self.left_btn[2] - line.get_width())//2, self.left_btn[1] + (self.left_btn[3] - line.get_height())//2, line.get_width(), line.get_height()))
        pygame.draw.rect(WINDOW, self.right_col, self.right_btn)
        
        WINDOW.blit((line := FONT.render(f'You may be suffering from {self.current_symptom[1]}', 1, BLACK)), ((SIZE - line.get_width())//2, 0, 100, 30))
        WINDOW.blit((line := FONT.render('>', True, WHITE)), (self.right_btn[0] + (self.right_btn[2] - line.get_width())//2, self.right_btn[1] + (self.right_btn[3] - line.get_height())//2, line.get_width(), line.get_height()))
        
        pygame.draw.rect(WINDOW, self.home_col, self.home_btn)
        WINDOW.blit((line := FONT.render('Home', True, WHITE)), (self.home_btn[0] + (self.home_btn[2] - line.get_width())//2, self.home_btn[1] + (self.home_btn[3] - line.get_height())//2, line.get_width(), line.get_height()))
        
        descrp = self.current_symptom[2]
        
        WINDOW.blit(text_objects(descrp, SCROLL_VAL, h := 400), (0, 70, 640, h))
    

#methods

CURRENTSTATE = None

MENUSTATE = MenuState()
APPSTATE = AppState()
DIAGNOSISSTATE = DiagnosisState()
RESULTSTATE = ResultState()

def render():
    global CURRENTSTATE
    
    CURRENTSTATE.render()
    
    pygame.display.update()

def update(mouseClicked, mousePos):
    global CURRENTSTATE
    
    CURRENTSTATE.tick(mousePos[0], mousePos[1], mouseClicked)
    
    render()
    
def changeState(state):
    global CURRENTSTATE
    
    CURRENTSTATE = state

def main():
    global CURRENTSTATE, SCROLL_VAL
    
    running = True
    clock = pygame.time.Clock()
    
    CURRENTSTATE = MENUSTATE
    
    mouseClicked = False
    
    mousePos = 0, 0
    
    while running:
        'print(SCROLL_VAL)'
        clock.tick(60)
        mouseClicked = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    mouseClicked = True
            elif event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEWHEEL:
                if CURRENTSTATE == RESULTSTATE:
                    SCROLL_VAL = min(max(SCROLL_VAL - event.y, 0), 10) #generates a scroll value bw 0 and 10
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    SCROLL_VAL = max(SCROLL_VAL - 1, 0)
                elif event.key == pygame.K_DOWN:
                    SCROLL_VAL = min(SCROLL_VAL + 1, 10)
                
        update(mouseClicked, mousePos)
                
    pygame.quit()
    
def advance_process(num):
    and_values = []
    
    for disease in DMAP:
        and_values.append((num & disease['symptoms'], disease['disease'], disease['descp'].replace('                     ', '')))
        
    and_values.sort(key=lambda x : len(bin(x[0]).split('1')) - 1, reverse=True)
    
    return and_values

def text_objects(text : str, scrollVal, surfaceH):
    paragraphSize = (640, surfaceH)
    fontSize = FONT.get_height()

    # Step 1
    paragraphSurface = pygame.Surface(paragraphSize) 

    #Set colorkey to fake transparent paragraph surface
    paragraphSurface.fill((255, 255, 255))
    paragraphSurface.set_colorkey((255, 255, 255))

    # Step 2
    splitLines = text.splitlines()
    #extra below
    lines_per_win = (surfaceH // fontSize)
    
    max_scrolled_val = len(splitLines) - lines_per_win
    
    threshold = (scrollVal * max_scrolled_val) // 10
    
    idxStart = min(threshold, max_scrolled_val) if max_scrolled_val > 0 else 0
    
    splitLines = splitLines[idxStart:]
    #extra above
    #Step 4
    for idx, line in enumerate(splitLines):
        currentTextline = FONT.render(line, 1, (0, 0, 0))
        currentPostion = ((paragraphSize[0] - currentTextline.get_width()) // 2, idx * fontSize)
        paragraphSurface.blit(currentTextline, currentPostion)

    #Step 5
    return paragraphSurface

if __name__ == "__main__":
    main()
