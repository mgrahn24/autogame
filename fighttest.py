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


# Create unit selection options
def create_unit_options():
    # Example unit pool
    unit_pool = [
        Unit("Knight", 3, 2, 1, "Shield Bash"),
        Unit("Archer", 2, 1, 3, "Double Shot"),
        Unit("Mage", 1, 3, 2, "Fireball"),
        Unit("Goblin", 1, 1, 1, "Sneak Attack"),
        Unit("Orc", 4, 1, 1, "Berserk"),
        Unit("Healer", 1, 4, 1, "Healing Touch"),
    ]
    
    # Select 5 random units for the player to choose from
    return random.sample(unit_pool, 5)

# Unit selection phase allowing the player to select up to 3 units
def unit_selection_phase(screen, player_team):
    unit_options = create_unit_options()  # 3 units to choose from
    selected_units = []  # Track selected units

    while len(selected_units) < 3:
        draw_unit_selection(screen, unit_options, selected_units)

        # Wait for user input to select units (1, 2, or 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    selected_unit = unit_options[event.key - pygame.K_1]
                    
                    # Add unit to the team if there's space
                    if selected_unit not in selected_units and len(player_team) < 3:
                        selected_units.append(selected_unit)
                        player_team.append(selected_unit)

        # Check if player already selected 3 units
        if len(selected_units) == 3:
            return player_team

# Updated draw function to show selected units
def draw_unit_selection(screen, unit_options, selected_units):
    font = pygame.font.Font(None, 24)
    screen.fill((255, 255, 255))  # White background
    y_offset = 50
    for i, unit in enumerate(unit_options):
        text = f"{i + 1}. {unit.name}: Health {unit.health}, Attack {unit.attack}, Range {unit.attack_range}"
        screen.blit(font.render(text, True, (0, 0, 0)), (50, y_offset))
        y_offset += 50
    
    screen.blit(font.render("Choose units (1-3) to add to your team:", True, (0, 0, 0)), (50, y_offset + 30))

    # Display selected units
    selected_text = "Selected Units: " + ", ".join([unit.name for unit in selected_units])
    screen.blit(font.render(selected_text, True, (0, 0, 0)), (50, y_offset + 60))
    
    pygame.display.flip()


# Shop system to buy and upgrade units
class Shop:
    def __init__(self, currency):
        self.currency = currency
        self.available_units = self.generate_shop()

    def generate_shop(self):
        # Generate a few random units for the player to buy
        return [
            Unit("Swordsman", 3, 2, 1, "Slash"),
            Unit("Mage", 2, 3, 2, "Fireball"),
            Unit("Healer", 2, 1, 1, "Heal"),
        ]
    
    def buy_unit(self, player_team, unit_index):
        # Simplified purchase system
        unit = self.available_units[unit_index]
        player_team.append(unit)
        self.currency -= 3  # Assume each unit costs 3 currency

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

# Battle system (using the player's and enemy's teams)
def run_battle(screen, player_team, enemy_team):

    print("Player Team:", [unit for unit in player_team])
    print("Enemy Team:", [(unit.name, unit.health) for unit in enemy_team])
    battle_log = ""
    result_message = ""
    clock = pygame.time.Clock()

    while True:  # Main loop continues until the battle is over
        # Player's turn
        player_index = 0
        while player_index < len(player_team):  # Loop through player team
            player = player_team[player_index]
            if player.is_alive():
                # Check for valid targets
                valid_targets = [
                    enemy_index
                    for enemy_index, enemy in enumerate(enemy_team)
                    if enemy.is_alive() and abs(player_index + enemy_index + 1) == player.attack_range
                ]
                if valid_targets:
                    target_index = max(valid_targets)
                    target_enemy = enemy_team[target_index]
                    damage = player.attack_enemy(target_enemy)
                    battle_log = f"{player.name} attacks {target_enemy.name} for {damage} damage!"
                else:
                    battle_log = f"{player.name} is waiting for a target!"
                draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
                pygame.display.flip()
                pygame.time.delay(ACTION_DELAY)

            # Remove dead enemies after the player's attack
            enemy_team = [enemy for enemy in enemy_team if enemy.is_alive()]  # Remove dead enemies
            if not enemy_team:  # If all enemies are dead
                result_message = "Player Team Wins!"
                draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
                pygame.display.flip()
                pygame.time.delay(3000)
                return "win"
            
            player_index += 1  # Move to the next player unit
        
        # Enemy's turn
        enemy_index = 0
        while enemy_index < len(enemy_team):  # Loop through enemy team
            enemy = enemy_team[enemy_index]
            if enemy.is_alive():
                # Check for valid targets
                valid_targets = [
                    player_index
                    for player_index in range(len(player_team))
                    if player_team[player_index].is_alive() and abs(enemy_index + player_index + 1) == enemy.attack_range
                ]
                if valid_targets:
                    target_index = max(valid_targets)
                    target_player = player_team[target_index]
                    damage = enemy.attack_enemy(target_player)
                    battle_log = f"{enemy.name} attacks {target_player.name} for {damage} damage!"
                else:
                    battle_log = f"{enemy.name} is waiting for a target!"
                draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
                pygame.display.flip()
                pygame.time.delay(ACTION_DELAY)

            # Remove dead players after the enemy's attack
            player_team = [player for player in player_team if player.is_alive()]  # Remove dead players
            if not player_team:  # If all players are dead
                result_message = "Enemy Team Wins!"
                draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
                pygame.display.flip()
                pygame.time.delay(3000)
                return "loss"
            
            enemy_index += 1  # Move to the next enemy unit

        # Ensure the battle state is properly updated after each turn
        draw_battle_results(screen, player_team, enemy_team, battle_log, result_message)
        pygame.display.flip()
        clock.tick(FPS)


# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Roguelike Autobattler")

    running = True
    player_team = []  # Start with an empty player team

    while running:
        # Unit selection phase
        selected_unit = unit_selection_phase(screen,player_team)
        #player_team.append(selected_unit)  # Add the selected unit to the player team

        print(player_team)
        # Create enemy team for the battle
        enemy_team = [
            Unit("Goblin", 3, 1, 1, "Sneak Attack"),
            Unit("Orc", 4, 1, 1, "Berserk"),
            Unit("Mage", 2, 1, 3, "Fireball"),
        ]

        # Proceed to battle after selection
        result = run_battle(screen, player_team, enemy_team)
        if result == "win":
            print("You won the battle!")
        else:
            print("You lost the battle!")

        # Continue the loop or end the game based on conditions (e.g., lose condition)
        # For now, let's end after one battle
        running = False

    pygame.quit()

if __name__ == "__main__":
    main()
