def rule4(pword: int) -> bool:
    str_password = str(pword)
    if str_password[0] <= str_password[1] <= str_password[2] <= str_password[3] <= str_password[4] <= str_password[5]:
        return True


def rule3(pword: int) -> bool:
    str_password = str(pword)
    if str_password[0] == str_password[1] or str_password[1] == str_password[2] or str_password[2] == str_password[3] or \
            str_password[3] == str_password[4] or str_password[4] == str_password[5]:
        return True


day1counter: int = 0
for password in range(134792, 675810):
    if rule3(password) and rule4(password):
        day1counter += 1
print(day1counter)
