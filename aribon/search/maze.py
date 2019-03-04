"""
Tasks:
    大きさN*Mの迷路が与えられる．
    迷路は通路と壁からできていて，1ターンで隣接する上下左右4マスの通路に移動できる．
    スタートからゴールまで移動するのに必要な最小のターン数を求めよ．

Solution:
    幅優先探索．


Sample input:
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#

expected output:
22
"""