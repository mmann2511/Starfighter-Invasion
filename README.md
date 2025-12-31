# 🚀 **Starfighter Invasion**

A fast-paced 2D space shooter built in **Python** using **Pygame**, featuring player-aimed combat, diving enemy fighters, burst-fire lasers, and a dynamic starfield background.

This project is an extended and modified version of the *Alien Invasion* tutorial from **Python Crash Course (3rd Edition)**, used as a sandbox to experiment with enemy behavior, movement, and real-time game systems.

---

## 🎮 **About the Game**

**Starfighter Invasion** began as a learning project and gradually evolved through experimentation and refactoring.

Rather than focusing on complex AI immediately, the game emphasizes:

* clear movement logic
* readable code
* controlled difficulty
* incremental feature additions

You pilot an **X-Wing**, defending space against waves of **TIE fighters** that dive toward your position and unleash burst-fire laser attacks.

**Your objective:**
🔥 Survive
🔥 Destroy enemy fighters
🔥 Beat the persistent high score

---

## 🧠 **Gameplay Features**

### ⭐ Player Mechanics

* Mouse-controlled X-Wing movement
* Dual angled laser fire
* Collision detection with enemies and projectiles
* Limited lives with visual ship counter
* Score, level, and high-score tracking

### ⭐ Enemy Fighters

* 1–3 TIE fighters on screen (testing configuration)
* Fighters spawn above the screen and **dive toward the player’s position**
* Burst-fire attack pattern (double-shot followed by cooldown)
* Slightly angled enemy lasers for spread
* Fighters are removed once they exit the screen

### ⭐ Visual & UI Elements

* Transparent PNG sprites
* Animated starfield background (random stars rendered each frame)
* Bright laser effects
* Clean scoreboard UI with score, level, and lives display

### ⭐ Core Game Systems

* Persistent high score stored in JSON
* Bullet collision handling
* Level progression and speed scaling
* Restart system with mouse capture and Play button

---

## 🧬 **How This Differs from the Original Tutorial**

| Python Crash Course Version | Starfighter Invasion       |
| --------------------------- | -------------------------- |
| Static background           | Animated starfield         |
| Simple fleet movement       | Independent diving enemies |
| Keyboard ship movement      | Mouse-controlled ship      |
| No enemy projectiles        | Enemy burst-fire lasers    |
| Text-based lives display    | Sprite-based life counter  |
| No persistent score         | High score saved to JSON   |

---

## 🧩 **Project Structure**

```
starfighter_invasion/
│
├── starfighter_invasion.py   # Main game loop & event handling
├── settings.py               # Screen size, speed tuning, difficulty scaling
├── xwing.py                  # Player ship logic
├── tiefighter.py             # Enemy movement & firing behavior
├── bullet.py                 # Player and enemy laser logic
├── button.py                 # Play button UI
├── game_stats.py             # Score, lives, high score persistence
├── scoreboard.py             # On-screen UI rendering
│
├── high_score.json           # Persistent high score storage
│
└── images/
    ├── xwing.png             # Player sprite
    └── tiefighter.png        # Enemy sprite
```

---

## 🕹️ **How to Run**

### Install dependencies

```bash
pip install pygame
```

### Run the game

```bash
python starfighter_invasion.py
```

### Controls

* 🖱 **Mouse** — Move the X-Wing
* 🟢 **Left Click** — Fire lasers
* ❌ **Q** — Quit
* ▶️ **Play Button** — Start or restart the game

---

## 📸 **Screenshots**

<p align="center">
  <img src="https://github.com/user-attachments/assets/28c349cc-6de8-4842-aea0-a161a8c7f7f7" width="750">
  <br>
  <em>TIE fighters diving toward the player with starfield rendering</em>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/834d3834-1477-41ba-8c2f-4736dc52689f" width="750">
  <br>
  <em>X-Wing combat with dual lasers and score UI</em>
</p>

---

## 🛠️ **Tech Stack**

* **Python**
* **Pygame**
* JSON for persistent scoring
* Custom sprites and movement logic

---

## 🌟 **Future Ideas**

* Additional enemy movement patterns
* Boss encounters
* Particle effects and explosions
* Power-ups (spread shot, shields, rapid fire)
* Sound effects and music
* Pause menu and difficulty settings

---

## 💡 **Credits**

Created by **Michael Mann**

Based on the *Alien Invasion* project from **Python Crash Course (3rd Edition)** by Eric Matthes, and expanded through independent experimentation and iteration.

---




