def main():
    number_of_tests = int(input())

    for test in range(0, number_of_tests):
        number_of_digits = int(input())
        digits = [int(num) for num in input().split(" ")]
        print(is_pyramid(digits))


def is_pyramid(my_list: list):
    # cube = max(my_list[0],my_list[-1])
    vertical_stack = []
    while len(my_list) > 0:
        if my_list[0] > my_list[-1]:
            cube = my_list.pop(0)
        else:
            cube = my_list.pop(-1)

        if len(vertical_stack) > 0 and cube <= vertical_stack[-1]:
            vertical_stack.append(cube)
        elif len(vertical_stack) == 0:
            vertical_stack.append(cube)
        else:
            return "No"
    return "Yes"


if __name__ == "__main__":
    main()
