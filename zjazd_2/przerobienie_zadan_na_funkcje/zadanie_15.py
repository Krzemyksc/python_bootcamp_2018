from random import randint

# Losowanie położenia
s_x = randint(1, 10)
s_y = randint(1, 10)

g_x = randint(1, 10)
g_y = randint(1, 10)
# Przypisanie położenia
gracz = g_x, g_y
skarb = s_x, s_y
minimalna_liczba_krokow_po_wylosowaniu = abs(s_x - g_x) + abs(s_y - g_y)
liczba_ruchow = 0
while True:
    min_l_ruch_przed = abs(s_x - g_x) + abs(s_y - g_y)

    ruch = input("wykonaj ruch [wasd]: ")
    if ruch == 'w':
        g_y += 1
    if ruch == 's':
        g_y -= 1
    if ruch == 'a':
        g_x -= 1
    if ruch == 'd':
        g_x = + 1
    liczba_ruchow += 1

    # przerwanie gry
    if g_x > 10 or g_y > 10 or g_x < 1 or g_y < 1:
        break

    mini_l_ruch_po = abs(s_x - g_x) + abs(s_y - g_y)
    if mini_l_ruch_po > min_l_ruch_przed:
        print("Zimno")
    if mini_l_ruch_po < min_l_ruch_przed:
        print("Ciepło")
    if mini_l_ruch_po == 0:
        print("Wygrałeś")
        break
    if liczba_ruchow > 2 * minimalna_liczba_krokow_po_wylosowaniu:
        s_x = randint(1, 10)
        s_y = randint(1, 10)
print(f"Położenie skarbu: x = {s_x}, y = {s_y}")
print(f"Położenie gracza: x = {g_x}, y = {g_y}")
print(f'minimalna liczba kroków: {minimalna_liczba_krokow_po_wylosowaniu}')
