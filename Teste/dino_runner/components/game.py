import pygame


#CLOUD
from dino_runner.utils.constants import BG, ICON,ICON1, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, CLOUD

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.text_utils import draw_message_component

from dino_runner.components.powerups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.best_score = 0
        self.death_count = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0 #CLOUD
        self.y_pos_cloud = 50 #CLOUD
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.draw_background()
        self.draw_cloud() #CLOUD
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_upper_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width() 
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    #CLOUD
    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 900
        self.x_pos_cloud -= self.game_speed

    def draw_score(self):
        draw_message_component(
            f"score: {self.score} ",
            self.screen,
            pos_x_center = 1000,
            pos_y_center = 50
        )         

    def draw_power_upper_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen, 
                    font_size = 18,
                    pos_x_center = 150,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE 

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))  
        if self.death_count == 0:
            draw_message_component("Welcome to Aviator! Press any key to start.", self.screen, pos_y_center= 350)
            self.screen.blit(ICON1, (self.half_screen_width - 70, self.half_screen_height - 80))
        else:
            draw_message_component("You died! Press any key to try again.", self.screen, pos_y_center= 350)
            draw_message_component(
                f"Your score: {self.score - 1}",
                self.screen,
                pos_y_center = self.half_screen_height - 150
            )
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center=self.half_screen_height - 100
            )
            self.screen.blit(ICON, (self.half_screen_width - 60, self.half_screen_height - 50))
            self.show_best_score_of_session()
        pygame.display.flip()
        self.handle_events_on_menu()    
    
    def show_best_score_of_session(self):
        if self.score > self.best_score:
            self.best_score = self.score - 1

        draw_message_component(f"Best score: {self.best_score}", self.screen, pos_y_center = self.half_screen_height - 185)




