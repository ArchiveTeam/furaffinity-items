def main():
    min_id = 1
    max_id = 16220530
    batch_size = 50
    batch = []

    for num in range(min_id, max_id + 1):
        batch.append(num)
        
        if len(batch) >= batch_size:
            batch = tuple(sorted(batch))
            print('submission:{}-{}'.format(batch[0], batch[-1]))
            batch = []

    if batch:
        batch = tuple(sorted(batch))
        print('submission:{}-{}'.format(batch[0], batch[-1]))


if __name__ == '__main__':
    main()

