fuel: int = 0
total_fuel: int = 0
# 必要な燃料変数の初期化

def calc(mass: int) -> int:
    return int(mass) // 3 - 2
    # ３で割った商を切り捨て２を引く関数


with open("day1.txt", "r") as f:
    for line in f:
        while True:
            fuel = calc(line)
            if fuel > 0:
                total_fuel += fuel
                line = fuel
            else:
                break

print(total_fuel)
