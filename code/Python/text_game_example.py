#!/usr/bin/env python
# coding: utf-8

# 초기 상태 설정
player_name = input("당신의 이름은 무엇입니까? ")
health = 100
inventory = []

print(f"{player_name}님, 일주일간 던전 생존기에 오신 걸 환영합니다!")
print(f"초기 체력: {health}")
print("")

# 1일차 (월요일)
print("[월요일] 배고픈 아침입니다. 빵을 발견했습니다.")
eat_bread = input("빵을 먹겠습니까? (예/아니오): ")
if eat_bread == "예":
    health += 10
    inventory.append("빵")
    print("빵을 먹고 힘이 납니다! (체력 +10)")
else:
    health -= 10
    print("아침을 거르고 기운이 빠집니다... (체력 -10)")

print(f"현재 체력: {health}")
if health <= 0:
    print("😢 체력이 바닥나 쓰러졌습니다. 게임 오버")
else:
    print("")

# 2일차 (화요일)
if health > 0:
    print("[화요일] 독버섯이 널려 있습니다.")
    mushroom = input("독버섯을 피해가겠습니까? (예/아니오): ")
    if mushroom == "예":
        print("현명한 선택입니다! (체력 변동 없음)")
    else:
        health -= 30
        print("독버섯을 먹고 배탈이 났습니다... (체력 -30)")

    print(f"현재 체력: {health}")
    if health <= 0:
        print("😢 체력이 바닥나 쓰러졌습니다. 게임 오버")
    else:
        print("")

