# AvaEngine

**AvaEngine** is a modular, expandable 2D game engine written in Python—with a focus on flexibility, rapid prototyping, and creativity.

## Features

- 🎨 **Renderer/Graphics:** Built with Pygame, supports dynamic rendering, scaling, and smooth camera.
- 🗂️ **Modular Architecture:** Each core system (graphics, audio, assets, physics, scripting, UI, saving/export, etc.) is its own file and class—easy to expand or swap.
- 🔨 **Scene & World Editor:** Click to place and manage world objects (bushes, roads, enemies, more to come).
- 🧑 **Player & Enemies:** Player movement, enemy placement, collision detection, basic attacks & health system.
- 🛠️ **Expandable Catalog System:** Quickly prototype new object types; flexible to turn into a catalog/interface.
- 📝 **Development UI:** Hotkey-based catalog (1=Bush, 2=Road, 3=Enemy), with plans for in-window dev tools.
- 🚀 **Future Modules:** Physics, scriptable behaviors, plugins, networking, export tools, and more.
- 💾 **Export Support (planned):** Tools for saving, version control, and exporting playable projects.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/NuerovaSystems/AvaEngine.git
    cd AvaEngine
    ```
2. **Set up the Python environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install pygame
    ```
3. **Run the engine:**
    ```bash
    python engine.py
    ```

## Controls

- **Arrow keys / WASD:** Move the player
- **Mouse click:** Place selected object at that spot in the world
- **1:** Select Bush (green square)
- **2:** Select Road (tan square)
- **3:** Select Enemy (red square)
- **Spacebar:** Attack when touching an enemy
- **P:** Play (starts game mode)

## Code Structure

- `engine.py`: Main entry, manages game loop and connects all modules.
- `graphics.py`: Handles window, camera, and rendering (modular).
- `player.py`, `enemy.py`, `bush.py`, `road.py`, etc.: World object classes.
- `catalog.py`, `filesystem.py`, ...: Ready for new features and expansion.
- Every module/class is self-contained for future plug-and-play growth.

## Roadmap

- [ ] Add true UI for catalog and tools
- [ ] Polished scene/world editor
- [ ] Animations and sound
- [ ] Export to HTML5/native apps
- [ ] Script editor and plugin support
- [ ] Multiplayer/collaboration tools

## Contributing

Pull requests are welcome! Please open issues or ideas for improvements.

---

**AvaEngine is created by [Ava Hughes](https://github.com/NuerovaSystems) and is in active development.**

Every brick is open source—build along, fork, or help shape the engine’s future!
