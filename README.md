# Roguelike Autobattler Game

## Overview
This is a roguelike autobattler where players manage a small team of units placed into (how many?) slots. Each round, the team automatically fights an enemy team based on unit attributes such as attack, health, range, and special abilities. Between battles, players can upgrade units, recruit new ones, or sell existing units to adjust their strategy.

## Gameplay Loop
1. **Battle Phase**: 
   - Teams automatically battle based on unit attributes and positions.
   - Outcomes are determined by the remaining health of each team's units.

2. **Purchase Phase**:
   - Players are presented with a selection of new units (and items?).
   - Combine duplicate units to upgrade them (3 copies for next level? Stats better and ability enhanced).
   - Sell units to make room for new ones or generate currency.
   - Manage unit positioning and composition.

3. **Progression**:
   - New, more powerful units become available as the game progresses (could be gradually unlocked or just have the probabilities of them appearing shift?).
   - Players must decide between upgraded early units or stronger late-game units.
   - Player should have to balance short term power with scaling

---

## Gameplay Concept Ideas
- **Unit Types**: Define potential unit categories (melee, ranged, support, etc.).
- **Synergies**: Concepts for unit combinations or team bonuses. could be implicit, like they just work well together, or explicit, like there is a category and you get a bonus for 3,4,5 all from that category
- **Difficulty Scaling**: Fixed sequence of enemies OR dynamic sequence of enemies (based on player choice?) OR random enemy team generation? Best might be random selection from a curated pool?

---

## Key Design Questions

- What are the most effective ways to balance unit progression and power scaling?
- What elements if any should carry over between runs? Something small for variation? Or something significant so you go futher every time?
- How will randomness (e.g., unit selection, enemy selection) impact strategy?
- How big should the pool of units be?
- Should health carry over between battles, or units reset
- How will the player lose (eg. some finite lives or health that gets depleted by a lost battle? Or just if the team dies at all?)
- How many options to give at purchase? Should you be able to reroll. How should purchases be limited (currency, set amount each round?)
- Theme?
- Aesthetic?
- Story?

## Smaller Design Questions
- How should unit abilities trigger? could have: on attack, an being damaged, on combat start, on death, on turn x etc, persistent (eg. all allies +1 attack)
- How should range work, eg should ranged unit only hit 2 slots away, or up to 2 slots? maybe anything is possible (configure a range like an array of allowed slot distances)
---

## Units
- **[Unit Name]**:
  - **Attack**: [Value]
  - **Health**: [Value]
  - **Range**: [Short/Medium/Long]
  - **Special Ability**: [Ability Description]
  
  _(Add more units as they are designed)_

---

## Abilities
- **[Ability Name]**:
  - **Effect**: [Description of how the ability works]
  - **Trigger**: [Condition or frequency the ability activates]

---

## Items
- **[Item Name]**:
  - **Effect**: [Boosts, buffs, or special effects on units]

---

## User Experience & Interface
- **Gameflow**: Notes on how the player interacts with the game (e.g., unit selection, upgrades).
- **UI Mockups**: Ideas or images for how the user interface should look.
- **Feedback Systems**: How will the game provide feedback to the player (e.g., health bars, damage numbers, win/loss results)?

---

## Random Ideas / extensions
- More than 1D board, small grid? funnel?
- Instead of distinct units you gain and replace you have persisent characters that you upgrade, give abilities and items to

