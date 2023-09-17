# MemoryBlinkr
Ever wanted to challenge your memory? Or maybe improve it because your memory fades in the blink of an eye? MemoryBlinkr is here to help – a game where you only have until your next blink to remember an image or text and replicate it as accurately as possible.

![menu](https://github.com/angelaw7/htn-2023/assets/74735037/2b626879-4d44-40f3-ba82-55c7377b1b22)


## Inspiration
We wanted a chance to work with computer vision and game development, and since the final product is essentially a collection of minigames with a common theme, it was perfect for learning a variety of new systems.

## What it does
The project is a memory game where the user has to memorize something on the screen as quickly as possible, as it disappears when they blink and they have to reproduce it. We implemented a few versions as individual minigames:
- Grid game: A grid of black and white squares appears on the screen. Each level gets harder as the grid size increases and the goal is to advance as far as possible.
- Image game: A random image appears on the screen and the goal is to replicate the image by drawing on a canvas.
- Phrase game: The player inputs a topic, which is used to generate a short sentence. The sentence is presented briefly and the goal is to reinput the phrase given.

## Setup

Clone the repo and enter its directory
```bash
git clone git@github.com:angelaw7/htn-2023.git
cd htn-2023
```

Create virtual environment and install requirements; ensure that pip in installed already
```bash
python venv -m venv venv
venv\Scripts\Activate  // Windows
pip install -r requirements.txt
```

Run the app!
```bash
flask run
```
