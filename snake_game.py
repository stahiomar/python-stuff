import curses
import random

#initialize the screen
screen = curses.initscr()

curses.curs_set(0)

window_width, window_height = screen.getmaxyx()

#create new window
window = curses.newwin(window_height, window_width, 0, 0)

#allow window to receive inputs from the keyboard
window.keypad(True)

#set the delay of screen update
window.timeout(100)

#set the coordinate of initial position of the snake
snk_x = window_width // 4
snk_y = window_height // 2

#define the body of the snake
snake = [
    [snk_y, snk_x],  #head
    [snk_y, snk_x - 1],  #body
    [snk_y, snk_x - 2]  #tail
]

#define the food
food = [window_height // 2, window_width // 2]
window.addch(food[0], food[1],
             curses.ACS_DIAMOND)  #available after initscr() has been called

#set initial direction movement to the right
key = curses.KEY_RIGHT

#create a for loop that stops when the player lose
while True:
  next_key = window.getch()
  key = key if next_key == -1 else next_key
  if snake[0][0] in [0, window_height] or snake[0][1] in [
      0, window_width
  ] or snake[0] in snake[1:]:
    curses.endwin()  #close the window
    quit()  #exit the game
  new_head = [snake[0][0], snake[0][1]]
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1
  snake.insert(0, new_head)

  if snake[0] == food:
    food = None

    while food is None:
      new_food = [
          random.randint(1, window_height - 1),
          random.randint(1, window_width - 1)
      ]
      food = new_food if new_food not in snake else None
    window.addch(food[0], food[1], curses.ACS_DIAMOND)

  else:
    #remove tail and put space instead
    tail = snake.pop()
    window.addch(tail[0], tail[1], ' ')

  window.addch(snake[0][0], snake[0][1], curses.ACS_BLOCK)
