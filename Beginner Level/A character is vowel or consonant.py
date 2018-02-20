def main():
    a=raw_input()
    if a in ('a','e','i','o','u','A','E','I','O','U'):
        print("Vowel")
    elif a in ('y','Y','h','H'):
        print("somtimes y and h acts as a vowel")
    else:
        print("Consonant")

if __name__ == '__main__':
    main()
