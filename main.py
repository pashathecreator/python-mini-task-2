def my_zip(a_list: list, b_list: list) -> list[tuple]:
    min_len = min(len(a_list), len(b_list))
    zipped = [0] * min_len
    for i in range(min_len):
        zipped[i] = (a_list[i], b_list[i])
    return zipped

def main():
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    zipped = my_zip(a_list, b_list)
    print(zipped)
    
if __name__ == "__main__":
    main()