from snake_class import Snake


snake_game = Snake()
snake_game.set_window("black", 600, 600)
snake_game.update_segments()

snake_game.positions_update()
snake_game.move()









snake_game.window.exitonclick()

