N = 3  # размер игрового поля (можно увеличить)
limit = tuple(i for i in range(N))


def game_2_players():
    """Т.к.в задании не оговорено - игра для 2 игроков.
    """
    matrix = [['-' for i in range(N)] for j in range(N)]
    steps = 0

    def print_matrix():
        print(f'№\№| {" | ".join(str(j) for j in range(N))} |')
        for i in range(N):
            print(f' {i} | {" | ".join(matrix[i][j] for j in range(N))} |')

    def step(player):
        mark = 'X' if player == 1 else '0'
        name = '"Крестиками"' if player == 1 else '"Ноликами"'
        print(f'========== Ход игрока {name} ==========')
        print('Введите через пробел № строки и затем № столбца: ')
        while True:
            try:
                target = tuple(map(int, input().split()))
                if len(target) != 2:
                    raise TypeError
            except TypeError:
                print('Неверный формат (нужно 2 числа). Введите заново: ')
                continue
            if not (target[0] in limit and target[1] in limit):
                print('Неверный формат (диапазон). Введите заново: ')
                continue
            if matrix[target[0]][target[1]] != '-':
                print('Ячейка уже занята. Введите заново: ')
                continue
            matrix[target[0]][target[1]] = mark
            print(f'========== Ход {target} выполнен. ==========')
            nonlocal steps
            steps += 1
            break

    def game_over():
        if steps < N*2 - 1:
            return False
        for i in range(N):
            if set(matrix[i]) == {'X'}:
                print('Игра закончена. Победили "Крестики"!')
                return True
            if set(matrix[i]) == {'0'}:
                print('Игра закончена. Победили "Нолики"!')
                return True
        for j in range(N):
            if ''.join([matrix[i][j] for i in range(N)]) == 'XXX':
                print('Игра закончена. Победили "Крестики"!')
                return True
            if ''.join([matrix[i][j] for i in range(N)]) == '000':
                print('Игра закончена. Победили "Нолики"')
                return True
        diag = [matrix[i][i] for i in range(N)]
        rev_diag = [matrix[i][N-1-i] for i in range(N)]
        if set(diag) == {'X'} or set(rev_diag) == {'X'}:
            print('\n----- Игра закончена ----- Победили "Крестики"!')
            return True
        if set(diag) == {'0'} or set(rev_diag) == {'0'}:
            print('\n----- Игра закончена ----- Победили "Нолики"!')
            return True
        if steps == N**2:
            print('\n----- Игра закончена ----- Ничья.')
            return True

    print('\n---------- НОВАЯ ИГРА ---------- (смотрите схему).')
    print('Примечания: 1й ход - крестиками.')
    print_matrix()

    player = 1
    next_p = 0
    while True:
        step(player)
        print_matrix()
        player, next_p = next_p, player
        if game_over():
            break
    new()


def new():
    new_game = input('\n' + 'Новая игра? (y/n) (по умолчанию "n")): ')
    print('(прервать - "ctrl+c", размерность "N", перезапуск - "new()")')
    if new_game in ('y', 'Y'):
        game_2_players()


new()
