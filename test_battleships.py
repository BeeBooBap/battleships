import pytest
from battleships import *

# ------------------------------------------------------

s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})

def test_is_sunk1():
    assert is_sunk(s) == True

def test_ship_type1():
    assert ship_type(s) == "cruiser"

def test_is_open_sea1():
    assert is_open_sea(9, 3, [s]) == True

# ------------------------------------------------------

s2 = (5, 5, False, 4, {(5, 5)})
f1 = [s, s2]

def test_is_sunk2():
    assert is_sunk(s2) == False

def test_ship_type2():
    assert ship_type(s2) == "battleship"

def test_is_open_sea2():
    assert is_open_sea(5, 4, f1) == False

def test_ok_to_place_ship_at1():
    assert ok_to_place_ship_at(6, 3, True, 2, f1) == False

def test_ok_to_place_ship_at2():
    assert ok_to_place_ship_at(6, 3, False, 2, f1) == True

def test_place_ship_at1():
    actual = place_ship_at(6, 3, True, 2, f1)
    actual.sort()
    # specification of place_ship_at does not mandate any order on ships in a fleet, so we need
    # to sort expected and actual fleets in order to use == safely
    expected = [s, s2, (6, 3, True, 2, set())]
    expected.sort()
    assert expected == actual

# ------------------------------------------------------

s3 = (0, 0, False, 2, {(0, 0), (1, 0)})

def test_ship_type3():
    assert ship_type(s3) == "destroyer"

def test_is_open_sea3():
    assert is_open_sea(2, 0, [s3]) == False

def test_is_sunk3():
    assert is_sunk(s3) == True

# ------------------------------------------------------

s4 = (0, 9, False, 1, {(0, 9)})
f2 = [s3, s4]

def test_ship_type4():
    assert ship_type(s4) == "submarine"

def test_is_open_sea4():
    assert is_open_sea(0, 7, [s4]) == True

def test_is_sunk4():
    assert is_sunk(s4) == True

def test_ok_to_place_ship_at3():
    assert ok_to_place_ship_at(0, 5, True, 4, f2) == False

def test_ok_to_place_ship_at4():
    assert ok_to_place_ship_at(0, 3, True, 4, f2) == True

def test_place_ship_at2():
    assert place_ship_at(0, 3, True, 4, f2) == [s3, s4, (0, 3, True, 4, set())]

def test_is_sunk5():
    s = (0, 0, True, 4, {(0, 0), (0, 1), (0, 2)})
    assert is_sunk(s) == False

# ------------------------------------------------------

f3 = [(0, 0, True, 4, set()), (0, 9, False, 3, set()), (2, 1, True, 3, set()), (2, 6, False, 2, set()),
      (4, 0, False, 2, set()), (9, 8, True, 2, set()), (6, 4, True, 1, set()), (5, 9, True, 1, set()),
      (9, 1, True, 1, set())]

def test_is_open_sea5():
    assert is_open_sea(7, 0, f3) == True

def test_ship_type5():
    ship = f3[6]
    assert ship_type(ship) == "submarine"

def test_ok_to_place_ship_at5():
    assert ok_to_place_ship_at(7, 0, True, 1, f3) == True

def test_place_ship_at3():
    assert place_ship_at(7, 0, True, 1, f3) == [(0, 0, True, 4, set()), (0, 9, False, 3, set()), (2, 1, True, 3, set()),
                                                (2, 6, False, 2, set()), (4, 0, False, 2, set()), (9, 8, True, 2, set())
                                                , (6, 4, True, 1, set()), (5, 9, True, 1, set()), (9, 1, True, 1, set())
                                                , (7, 0, True, 1, set())]

# ------------------------------------------------------

f4 = [(1, 1, True, 3, set()), (1, 6, False, 2, set()), (2, 9, False, 2, set()), (3, 0, True, 1, set()),
      (3, 2, True, 3, set()), (5, 1, True, 2, {(5, 2)}), (5, 4, True, 1, set()), (5, 7, True, 1, set()),
      (6, 9, False, 4, set()), (9, 0, True, 1, set())]


def test_check_if_hits1():
    assert check_if_hits(5, 1, f4) == True

def test_hit1():
    (actual, s) = hit(5, 1, f4)
    actual.sort()
    expected = [(1, 1, True, 3, set()), (1, 6, False, 2, set()), (2, 9, False, 2, set()), (3, 0, True, 1, set()), \
                (3, 2, True, 3, set()), (5, 1, True, 2, {(5, 2), (5, 1)}), (5, 4, True, 1, set()),
                (5, 7, True, 1, set()), (6, 9, False, 4, set()), (9, 0, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (5, 1, True, 2, {(5, 2), (5, 1)}))

def test_are_unsunk_ships_left1():
    assert are_unsunk_ships_left(f4) == True

# ------------------------------------------------------

f5 = [(6, 9, False, 4, set()), (1, 1, True, 3, set()), (1, 6, False, 2, {(1, 6), (2, 6)})]

def test_check_if_hits2():
    assert check_if_hits(7, 9, f5) == True

def test_check_if_hits3():
    assert check_if_hits(5, 9, f5) == False

def test_check_if_hits4():
    assert check_if_hits(2, 6, f5) == False

def test_check_if_hits5():
    assert check_if_hits(9, 9, f5) == True

def test_hit2():
    assert hit(7, 9, f5) == ([(6, 9, False, 4, {(7, 9)}), (1, 1, True, 3, set()), (1, 6, False, 2, {(1, 6), (2, 6)})],
                             (6, 9, False, 4, {(7, 9)}))

def test_are_unsunk_ships_left2():
    assert are_unsunk_ships_left(f5) == True

# ------------------------------------------------------

f6 = [(1, 1, True, 3, set())]

def test_place_ship_at4():
    assert place_ship_at(4, 1, True, 2, f6) == [(1, 1, True, 3, set()), (4, 1, True, 2, set())]

def test_place_ship_at5():
    assert place_ship_at(8, 1, False, 1, f6) == [(1, 1, True, 3, set()), (4, 1, True, 2, set()),
                                                 (8, 1, False, 1, set())]

def test_hit3():
    assert hit(1, 1, f6) == ([(1, 1, True, 3, {(1, 1)}), (4, 1, True, 2, set()), (8, 1, False, 1, set())],
                             (1, 1, True, 3, {(1, 1)}))

def test_hit4():
    assert hit(8, 1, f6) == (
    [(1, 1, True, 3, {(1, 1)}), (4, 1, True, 2, set()), (8, 1, False, 1, {(8, 1)})], (8, 1, False, 1, {(8, 1)}))

def test_hit5():
    assert hit(4, 2, f6) == (
    [(1, 1, True, 3, {(1, 1)}), (4, 1, True, 2, {(4, 2)}), (8, 1, False, 1, {(8, 1)})], (4, 1, True, 2, {(4, 2)}))

def test_hit6():
    assert hit(4, 1, f6) == (
    [(1, 1, True, 3, {(1, 1)}), (4, 1, True, 2, {(4, 2), (4, 1)}), (8, 1, False, 1, {(8, 1)})],
    (4, 1, True, 2, {(4, 2), (4, 1)}))

def test_are_unsunk_ships_left3():
    assert are_unsunk_ships_left(f6) == True

# ------------------------------------------------------

f7 =  [(1, 1, True, 3, {(1, 1), (1, 2), (1, 3)}), (4, 1, True, 2, {(4, 2), (4, 1)}), (8, 1, False, 1, {(8, 1)})]

def test_are_unsunk_ships_left4():
    assert are_unsunk_ships_left(f7) == False

# ------------------------------------------------------

f8 = [(4, 9, False, 4, {(4, 9), (5, 9), (6, 9), (7, 9)}), (1, 2, True, 3, {(1, 2), (1, 3), (1, 4)}),
      (5, 1, False, 3, {(5, 1), (7, 1), (6, 1)}), (6, 4, True, 2, {(6, 5)}), (3, 5, False, 2, {(4, 5), (3, 5)}),
      (8, 3, True, 2, {(8, 3), (8, 4)}), (8, 7, True, 1, {(8, 7)}), (0, 7, True, 1, {(0, 7)}),
      (1, 9, True, 1, {(1, 9)}), (3, 3, True, 1, {(3, 3)})]

def test_are_unsunk_ships_left5():
    assert are_unsunk_ships_left(f8) == True

def test_hit7():
    assert hit(6, 4, f8) == ([(4, 9, False, 4, {(4, 9), (5, 9), (6, 9), (7, 9)}),
    (1, 2, True, 3, {(1, 2), (1, 3), (1, 4)}), (5, 1, False, 3, {(5, 1), (7, 1), (6, 1)}),
    (6, 4, True, 2, {(6, 5), (6, 4)}), (3, 5, False, 2, {(4, 5), (3, 5)}), (8, 3, True, 2, {(8, 3), (8, 4)}),
    (8, 7, True, 1, {(8, 7)}), (0, 7, True, 1, {(0, 7)}), (1, 9, True, 1, {(1, 9)}), (3, 3, True, 1, {(3, 3)})],
    (6, 4, True, 2, {(6, 5), (6, 4)}))

def test_are_unsunk_ships_left6():
    assert are_unsunk_ships_left(f8) == False

# ------------------------------------------------------

f9 = [(0, 0, True, 2, set())]

def test_general1():
    for i in range(5):
        if i == 0:
            assert ok_to_place_ship_at(9, 9, True, 2, f9) is False
        if i == 1:
            assert ship_type(f9[0]) == "destroyer"
        if i == 2:
            assert check_if_hits(0, 1, f9) is True
            assert check_if_hits(-1, 1, f9) is False
        if i == 3:
            assert hit(0, 1, f9) == ([(0, 0, True, 2, {(0, 1)})], (0, 0, True, 2, {(0, 1)}))
            assert hit(0, 0, f9) == ([(0, 0, True, 2, {(0, 1), (0, 0)})], (0, 0, True, 2, {(0, 1), (0, 0)}))
        if i == 4:
            assert are_unsunk_ships_left(f9) is False
