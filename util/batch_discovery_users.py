import fileinput

def main():
    usernames = []

    for line in fileinput.input():
        username = line.strip()

        if not username:
            continue

        assert '\n' not in username, username
        assert '\r' not in username, username
        assert ',' not in username, username

        usernames.append(username)

        if len(usernames) >= 10:
            print('usernames:{}'.format(','.join(usernames)))
            usernames = []

    print('usernames:{}'.format(','.join(usernames)))


if __name__ == '__main__':
    main()

