"""별 찍기 과제용 프로그램.

사용 방법:
1) 패턴 번호를 선택합니다.
2) 줄 수(양의 정수)를 입력합니다.
3) 선택한 형태의 별 패턴을 출력합니다.
"""


def draw_left_triangle(size: int) -> None:
    """왼쪽 정렬 직각삼각형 출력."""
    for i in range(1, size + 1):
        print("*" * i)


def draw_right_triangle(size: int) -> None:
    """오른쪽 정렬 직각삼각형 출력."""
    for i in range(1, size + 1):
        stars = "*" * i
        print(stars.rjust(size))


def draw_pyramid(size: int) -> None:
    """가운데 정렬 피라미드 출력."""
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def print_menu() -> None:
    print("=== 별 찍기 과제 ===")
    print("1. 왼쪽 삼각형")
    print("2. 오른쪽 삼각형")
    print("3. 피라미드")


def main() -> None:
    print_menu()
    pattern = input("패턴 번호를 입력하세요 (1~3): ").strip()
    size_text = input("줄 수를 입력하세요 (양의 정수): ").strip()

    if not size_text.isdigit() or int(size_text) <= 0:
        print("줄 수는 1 이상의 정수여야 합니다.")
        return

    size = int(size_text)

    if pattern == "1":
        draw_left_triangle(size)
    elif pattern == "2":
        draw_right_triangle(size)
    elif pattern == "3":
        draw_pyramid(size)
    else:
        print("패턴 번호는 1, 2, 3 중에서 선택해주세요.")


if __name__ == "__main__":
    main()
