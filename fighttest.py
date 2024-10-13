import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
FONT_SIZE = 24
ACTION_DELAY = 1000  # Delay in milliseconds between actions

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Unit class
class Unit:
    def __init__(self, name, health, attack, attack_range, special_ability):
        self.name = name
        self.health = health
        self.attack = attack
        self.attack_range = attack_range
    
    def is_alive(self):
        return self.health > 0
    
    def attack_enemy(self, enemy):
        if self.is_alive() and enemy.is_alive():
            damage = self.attack
            enemy.health -= damage
            return damage
        return 0

# Create player and enemy teams
def create_teams():
    player_team = [
        Unit("Shield", 5, 0, 1, "Charge"),
        Unit("Knight", 2, 2, 1, "Charge"),
        Unit("Archer", 2, 1, 3, "Double Shot"), 
    ]
    
    enemy_team = [
        Unit("Goblin", 3, 1, 1, "Sneak Attack"),
        Unit("Orc", 4, 1, 1, "Berserk"),
        Unit("Mage", 2, 1, 3, "Fireball"),
    ]
    
    return player_team, enemy_team

# Draw the battle results on the screen
def draw_battle_results(screen, player_team, enemy_team, battle_log, result_message):
    font = pygame.font.Font(None, FONT_SIZE)
    screen.fill(WHITE)

    # Draw player team status (left side)
    x_offset = 300
    for unit in player_team:
        color = GREEN if unit.is_alive() else RED
        stats_text = f"{unit.attack} / {unit.health}"
        screen.blit(font.render(unit.name, True, color), (x_offset, 50))
        screen.blit(font.render(stats_text, True, color), (x_offset, 80))
        x_offset -= 70

    # Draw enemy team status (right side)
    x_offset = 400 
    for unit in enemy_team:
        color = GREEN if unit.is_alive() else RED
        stats_text = f"{unit.attack} / {unit.health}"
        screen.blit(font.render(unit.name, True, color), (x_offset, 50))
        screen.blit(font.render(stats_text, True, color), (x_offset, 80))
        x_offset += 70

    # Draw battle log
    screen.blit(font.render(battle_log, True, BLACK), (50, 300))

    # Draw result message
    if result_message:
        screen.blit(font.render(result_message, True, BLACK), (50, 350))

# Main function
def main():
    global screen  # Make the screen variable global to use in run_battle
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Roguelike Autobattler Prototype")
    
    clock = pygame.time.Clock()
    running = True
    
    # Create teams
    player_team, enemy_team = create_teams()
    battle_log = ""
    result_message = ""
    
    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player's turn
        for player_index in range(len(player_team)):
            player = player_team[player_index]
            if player.is_alive():
                # Check for valid targets
                valid_targets = [
                    enemy_index
                    for enemy_index, enemy in enumerate(enemy_team)
                    if enemy.is_alive() and abs(player_index + enemy_index + 1) == player.attack_range
                ]
                if valid_targets:
                    # Select the furthest valid enemy target
                    target_index = max(valid_targets)
                    target_enemy = enemy_team[target_index]
                    damage = player.attack_enemy(target_enemy)
                    battle_log = f"{player.name} attacks {target_enemy.name} for {damage} damage!"
                else:
                    battle_log = f"{player.name} is waiting for a target!"
                
                # Update the display after each attack
                draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
                pygame.display.flip()
                pygame.time.delay(ACTION_DELAY)  # Delay to make it readable
                
        # Check if enemy team is defeated after player's turn
        if all(not unit.is_alive() for unit in enemy_team):
            result_message = "Player Team Wins!"
            draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
            pygame.display.flip()
            pygame.time.delay(3000)  # Show result for a while before quitting
            break

        # Enemy's turn
        for enemy_index in range(len(enemy_team)):
            enemy = enemy_team[enemy_index]
            if enemy.is_alive():
                # Check for valid targets
                valid_targets = [
                    player_index
                    for player_index in range(len(player_team))
                    if player_team[player_index].is_alive() and abs(enemy_index + player_index + 1) == enemy.attack_range
                ]
                if valid_targets:
                    # Select the furthest valid player target
                    target_index = max(valid_targets)
                    target_player = player_team[target_index]
                    damage = enemy.attack_enemy(target_player)
                    battle_log = f"{enemy.name} attacks {target_player.name} for {damage} damage!"
                else:
                    battle_log = f"{enemy.name} is waiting for a target!"
                
                # Update the display after each attack
                draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
                pygame.display.flip()
                pygame.time.delay(ACTION_DELAY)  # Delay to make it readable
        
        # Check if player team is defeated after enemy's turn
        if all(not unit.is_alive() for unit in player_team):
            result_message = "Enemy Team Wins!"
            draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
            pygame.display.flip()
            pygame.time.delay(3000)  # Show result for a while before quitting
            break
        
        # Check for dead units and remove them
        player_team = [unit for unit in player_team if unit.is_alive()]
        enemy_team = [unit for unit in enemy_team if unit.is_alive()]

        # Draw battle results
        draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()




if __name__ == "__main__":
    main()
