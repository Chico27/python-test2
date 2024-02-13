init_block = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 1,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}

def bingo_check(block):
    # 横に揃う
    if block['1'] and block['2'] and block['3']:
        return True
    if block['4'] and block['5'] and block['6']:
        return True
    if block['7'] and block['8'] and block['9']:
        return True
    # 縦に揃う
    if block['1'] and block['4'] and block['7']:
        return True
    if block['2'] and block['5'] and block['8']:
        return True
    if block['3'] and block['6'] and block['9']:
        return True
    # 斜めに揃う
    if block['1'] and block['5'] and block['9']:
        return True
    if block['3'] and block['5'] and block['7']:
        return True
    # どこもビンゴにならない
    return False

check_list = []
# try_check_num_list
layer_1_ct = 0
layer_2_ct = 0
ret = 0
for i in range(1, 10):
    if init_block[str(i)] == 1:
        continue
    block1 = init_block.copy()
    block1[str(i)] = 1
    for j in range(i, 10):
        if block1[str(j)] == 1:
            continue
        check_ct = 1
        block2 = block1.copy()
        block2[str(j)] = 1
        layer_1_ct += 1
        if bingo_check(block2):
            check_list.append(check_ct)
            continue
        for k in range(1, 10):
            if block2[str(k)] == 1:
                continue
            block3 = block2.copy()
            block3[str(k)] = 1
            for l in range(k, 10):
                if block3[str(l)] == 1:
                    continue
                check_ct = 2
                block4 = block3.copy()
                block4[str(l)] = 1
                layer_2_ct += 1
                if bingo_check(block4):
                    check_list.append(check_ct)
                    continue
                for m in range(1, 10):
                    if block4[str(m)] == 1:
                        continue
                    block5 = block4.copy()
                    block5[str(m)] = 1
                    for n in range(m, 10):
                        if block5[str(n)] == 1:
                            continue
                        check_ct = 3
                        block6 = block5.copy()
                        block6[str(n)] = 1
                        if bingo_check(block6):
                            check_list.append(check_ct)
                            continue

print('1回でビンゴになる確率')
once_result = check_list.count(1)/layer_1_ct
print(once_result * 100, '%')
print('2回目までにビンゴになる確率')
print((once_result + (1 - once_result) * check_list.count(2)/layer_2_ct) * 100, '%')
