# <ins>WHERE (am i)</ins>

A barebone top down pixel art RPG game.  
  
This project is written in Python using mainly the pygame library.  
  
This project and source code can be made into a nice story-telling game since this is a barebone project.  

## <ins>Getting Started</ins>

Since this is a game made in python, there are many ways to start playing this. However, there are 2 ways I recommend.  

### <ins>Using Code Editors or IDEs</ins>

Whip up the code editor or IDE of your choice and clone the project to the directory you desire. Then, simply run the main.py.  

### <ins>Using the terminal (on Windows)</ins>

Clone the project into a directory of your choice:  
```plain
git clone https://github.com/h1kru-f14m3/WHERE-am-i.git
```
Then, simply run the main.py:  
```plain
python main.py
```

### <ins>Using the terminal (on Linux)</ins>

If you are on Linux, it is a little complicated but I will walk you through it.  
  
Create a virtual environment and activate it:  

```plain
python3 -m venv 

source /bin/activate
```

  
Install the dependencies:  

```plain
pip install pygame-ce
pip install pytmx
```

  
Run main.py:  

```plain
python3 main.py
```

  

## <ins>Features</ins>

Since this is a barebone project. It has all essential features of a game:  

*   Walking around
*   Collision Check
*   Keybinds
*   Player animation
*   Map
*   Menus
*   Buildings
*   Interiors
*   Y Sort (A little wonky but it works)
*   Background Music

### <ins>Walking around</ins>

This was a pretty easy thing to code. In the player.py, I checked for user input using pygame's get_pressed method. It returns a list of keys and their states. Using that, I checked for specific keys that the user has inputted for their keybinds. After that, depending on the direction the player moved along with the speed that's set in the Player class I've created, I set the player's position in the update method.
  
