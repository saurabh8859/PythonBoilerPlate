#this is my python boiler plate
def testingInput():
    get_str = lambda: input()
    get_int = lambda: int(input())
    get_list_int = lambda: [*map(int,input().split())]
    get_list_int_newLine = lambda n: [int(input()) for i in range(n)]
    get_2D_list_int = lambda n,m: [[*map(int,input().split())] for i in range(n)]
    get_list_char = lambda: input().split()
    get_list_comma_seprated_int = lambda: [*map(int,input().split(","))]
    convert_str_to_list = lambda str1: list(str1)
    convert_str_to_int = lambda str1: int(str1)
    convert_int_to_str = lambda int1: str(int1)