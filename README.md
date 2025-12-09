
# 🚀 **Starfighter Invasion**

A fast-paced space shooter built in Python with Pygame, featuring chaotic enemy AI, swooping TIE fighters, and a dynamic starfield background.

---

## 🎮 **About the Game**

**Starfighter Invasion** began as an expansion of the *Alien Invasion* project from **Python Crash Course (3rd Edition)** by Eric Matthes.

Key Enhancements Beyond Python Crash Course:

* **New enemy types**
* **Custon artwork (X-Wing + TIE Fighters sprites)**
* **Chaotic randomized AI motion**
* **Vertical swooping attacks**
* **Animated starfield background**
* **Difficulty scaling based on level**
* **More dynamic gameplay than the tutorial version**

You pilot an **X-Wing fighter**, defending space against waves of **rogue TIE Fighters** that fly, bounce, swoop, and accelerate as the chaos intensifies.

Your mission:
🔥 Survive
🔥 Score points
🔥 Beat the galactic high score

---

## 🧠 **Gameplay Features**

### ⭐ Player Mechanics

* Smooth mouse-controlled X-Wing positioning
* High-speed laser fire
* Collision detection with enemy sprites
* Limited lives with visual ship counter

### ⭐ Enemy AI & Difficulty

* Randomized chaotic horizontal and vertical movement
* Velocity wobble and direction changes
* **Swooping attacks** from off-screen above
* Speed increases each level
* Chaos multiplier scaling per wave
* Screen-edge bouncing behavior

### ⭐ Visual & UI Upgrades

* Fully transparent PNG sprites
* Image scaling for both game and scoreboard displays
* Animated starfield background (random stars every frame)
* Bright laser effects
* Smooth score, level, and high score display

### ⭐ Core Game Systems

* Persistent high score (saved to JSON)
* Bullet collision handling
* Level progression and difficulty scaling
* Restart button and mouse capture controls

---

## 🧬 **Technical Enhancements vs. Original Tutorial**

| Original Crash Course Game        | Starfighter Invasion Modifications                        |
| --------------------------------- | --------------------------------------------------------- |
| BMP sprites with white background | Transparent PNG assets & custom scaling                   |
| Fleets move left/right and drop   | Free-moving chaotic AI with screen bouncing               |
| No vertical motion                | Full screen travel + off-screen swooping attacks          |
| Static background                 | Animated starfield simulation                             |
| Simple speed scaling              | Independent scaling for speed, chaos, and swoop intensity |
| Lives shown as text               | Lives shown as miniature X-Wing sprite icons              |
| Keyboard movement                 | Mouse-tracking ship control                               |

These changes show a deep understanding of:

* sprite motion physics
* randomization
* velocity clamping
* state tracking
* image rendering
* collision systems
* game loop structure

---

## 🧩 **File Structure**

```
starfighter_invasion/
│
├── starfighter_invasion.py      # Main game loop & event handling
├── settings.py                  # Difficulty scaling, tuning, screen configs
├── xwing.py                     # Player ship logic and mouse movement
├── tiefighter.py                # Randomized enemy AI and swooping behavior
├── bullet.py                    # Laser mechanics and collisions
├── button.py                    # Play button creation
├── game_stats.py                # Score, high score, lives, and persistence
├── scoreboard.py                # Score, level, lives display
│
├── high_score.json              # Persistent high score storage
│
└── images/
    ├── xwing.png                # Player sprite
    └── tiefighter.png           # Enemy sprite
```

---

## 🕹️ **How to Play**

### Install Python & Pygame:

```
pip install pygame
```

### Run the game:

```
python starfighter_invasion.py
```

### Controls:

* 🖱 **Mouse** — Move your ship left/right
* 🟢 **Left click** — Fire lasers
* ❌ **Q** — Quit
* ▶️ **Play button** — Start or restart game

---

## 💡 **Credits**

Created by **Michael Mann**

Based on the original *Alien Invasion* project from **Python Crash Course**, 3rd Edition by Eric Matthes — but heavily expanded with original gameplay systems, movement AI, artwork, and rendering improvements.

---

# 🛠️ **Tech Stack**

* 🧠 Written in **Python**
* 🎨 Rendered with **Pygame**
* 📁 JSON for persistent scoring
* 🪐 Custom visual assets and physics logic

 
## 📸 Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/28c349cc-6de8-4842-aea0-a161a8c7f7f7" width="750">
  <br>
  <em>Chaotic TIE fighter movement with starfield rendering</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/834d3834-1477-41ba-8c2f-4736dc52689f" width="750">
  <br>
  <em>Player ship and score UI with rapid laser fire</em>
</p>


## 🌟 Future Enhancements

- Enemy types with unique movement styles
- Boss encounters or multi-wave levels
- Explosions and particle effects
- Power-ups (spread shot, shield, rapid fire)
- Sound effects and music
- Game menu and difficulty settings
- Pause system and settings screen


