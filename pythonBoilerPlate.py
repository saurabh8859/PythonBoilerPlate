# this is my python boiler plate


class TestingInput:  # Class for input and conversion
    def __init__(self):
        pass

    def get_str(self):  # For string Input
        return input()

    def get_int(self):  # For integer Input
        return int(input())

    def get_list_int(self):  # For Integer List Input Space seprated
        return [*map(int, input().split())]

    def get_list_int_newLine(self, n):  # For Integer List Input Line By Line
        return [int(input()) for i in range(n)]

    def get_2D_list_int(self, n, m):  # For 2d list Input
        return [[*map(int, input().split())] for i in range(n)]

    def get_list_char(self):  # For character list input
        return input().split()

    def get_list_comma_seprated_int(self):  # For comma seprated list input
        return [*map(int, input().split(","))]

    def convert_str_to_list(self, str1):  # For str to list
        return list(str1)

    def convert_str_to_int(self, str1):  # For string to integer
        return int(str1)

    def convert_int_to_str(self, int1):  # For integer to string
        return str(int1)


class StringSearch(TestingInput):  # string match or pattern match
    def __init__(self):
        TestingInput.__init__(self)

    # Naive String Searching Algorithm
    # str1 is string and ptr is to match in str1
    def naiveStringSearching(self, str1, ptr):
        N = len(str1)  # length of string
        M = len(ptr)  # lenght of pattern
        for i in range(N-M+1):
            j = 0
            while j < M and ptr[j] == str1[i+j]:
                j += 1
            if j == M:
                return "Pattern Found At index " + self.convert_int_to_str(i)
        else:
            return "Pattern not found"
