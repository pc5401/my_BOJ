n, k = map(int, input().split())

actions = [input().strip() for _ in range(n)]

bullets = 0
saved = None

for action in actions:
    if action == 'save':
        saved = bullets
    elif action == 'load':
        if saved is not None:
            bullets = saved
        else:
            bullets = 0
    elif action == 'shoot':
        bullets -= 1
    elif action == 'ammo':
        bullets += k

    print(bullets)