def calc_pos_of_grids():
    width = 0.13  # Width of Gird

    bottom = [
        (
            ((19 - 2 * i) - (20 - 4 * i) * width) / 18,
            1 - width / 2,
        )
        for i in range(10)
    ]
    bottom[0] = (1 - width / 2, 1 - width / 2)

    left = [
        (
            width / 2,
            ((19 - 2 * i) - (20 - 4 * i) * width) / 18,
        )
        for i in range(10)
    ]
    left[0] = (width / 2, 1 - width / 2)

    top = [
        (
            ((20 - 4 * i) * width - (1 - 2 * i)) / 18,
            width / 2,
        )
        for i in range(10)
    ]
    top[0] = (width / 2, width / 2)

    right = [
        (
            1 - width / 2,
            ((20 - 4 * i) * width - (1 - 2 * i)) / 18,
        )
        for i in range(10)
    ]
    right[0] = (1 - width / 2, width / 2)

    return bottom + left + top + right
