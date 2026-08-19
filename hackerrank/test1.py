if __name__ == "__main__":
    N = int(input())
    my_list = []
    for i in range(0, N):
        command = input()
        command_list = command.split(" ")
        match command_list[0]:
            case "insert":
                my_list.insert(int(command_list[1]), int(command_list[2]))
            case "print":
                print(my_list)
            case "remove":
                my_list.remove(int(command_list[1]))
            case "append":
                my_list.append(int(command_list[1]))
            case "sort":
                my_list.sort()
            case "pop":
                my_list.pop()
            case "reverse":
                my_list.reverse()
            case _:
                print("Wrong command")
