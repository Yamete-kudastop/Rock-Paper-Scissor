def get_player_name():
    name = input("Your name (Name 'Player') : ").strip()
    return name if name else "Player"
