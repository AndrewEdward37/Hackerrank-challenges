Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':
    N = int(raw_input())
    list = []
    for i in range(N):
        s= raw_input().split()
        command = s[0]
        if command == "insert":
            list.insert(int(s[1]), int(s[2]))
        elif command == "remove":
            list.remove(int(s[1]))
        elif command == "append":
            list.append(int(s[1]))
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        elif command == "print":
            print list

            
#LISTS CHALLANGE
