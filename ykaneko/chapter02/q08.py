for p in range(2, 101):  # 2から100までの数を順に調べる
    a = True  # 素数であると仮定しておく
    for k in range(2, p):  # 2からp-1までの数で割り切れるか調べる
        if p % k == 0:  # pがkで割り切れる場合
            a = False  # 素数ではないと判定
            break  # ループを抜ける
    if a:  # aがTrueのままならば
        print(p)  # pは素数なので出力する