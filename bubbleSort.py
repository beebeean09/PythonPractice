def bubble_sort(n, a):
    sorted = False
    swap_count = 0
    while not sorted:
        sorted = True
        last_before = n - 1
        for idx in range(last_before):
            next = idx + 1
            if a[idx] > a[next]:
                a[idx], a[idx + 1] = a[idx + 1], a[idx]
                swap_count += 1
                sorted = False


    first = a[0]
    last = a[-1]
    print('Array is sorted in {swap_count} swaps.'.format(swap_count = swap_count))
    print('First Element: {first}'.format(first = first))
    print('Last Element: {last}'.format(last = last))
    print(a)

bubble_sort(5, [4,2,7,1,9])
