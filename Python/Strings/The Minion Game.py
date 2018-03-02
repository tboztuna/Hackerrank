def minion_game(string):
    vowels = "AEIOU"
    pts_kevin = 0
    pts_stuart = 0

    for i in range(len(string)):
        if string[i] in vowels:
            pts_kevin += len(string) - i  # Thanks to Anatoli Babenia's logic.
        else:
            pts_stuart += len(string) - i

    if pts_kevin > pts_stuart:
        print "Kevin", pts_kevin
    elif pts_stuart > pts_kevin:
        print "Stuart", pts_stuart
    else:
        print "Draw"


if __name__ == '__main__':
    s = raw_input()
    minion_game(s)