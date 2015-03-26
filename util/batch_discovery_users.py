import fileinput

def main():
    usernames = []

    for line in fileinput.input():
        if not line.strip():
            continue

        usernames.append(line.strip())

        if len(usernames) >= 10:
            print('usernames:{}'.format(','.join(usernames)))
            usernames = []

    print('usernames:{}'.format(','.join(usernames)))


if __name__ == '__main__':
    main()

