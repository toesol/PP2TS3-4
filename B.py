def letter_s():
    letters=input()
    letter_list=list(letters)
    list_size = len(letter_list)

    for i in range(0,list_size):
        for j in range(i+1,list_size):
            if letter_list[i]>letter_list[j]:
                letter_list[i],letter_list[j] = letter_list[j],letter_list[i]
    print("".join(letter_list))


if __name__ == '__main__':
    letter_s()