#PureForWhite create a string encryption program with Toy Encryption Algorithm
#The source code will be in the link description below
#Follow me on reddit, subscribe my youtube channel, like this video and share it thanks!
#creating decryption function
def decryption(s):
    s = list(s)

    for i in range(len(s)):
        if s[i] == "_":
            s[i] = " "

    first = s[:len(s)//2]
    second = s[len(s)//2:]
    second = second[::-1]

    result = [" "] * (len(s) + 1)
    for i in range(len(first)):
        result[i * 2] = first[i]

    for j in range(len(second)):
        result[j * 2 + 1] = second[j]

    print("".join(result))

#creating encryption function
def encryption(s):
    s = list(s)
    first = []
    second = []

    for i in range(len(s)):
        if s[i] == " ":
            s[i] = "_"

        if i % 2 == 0:
            first.append(s[i])
        else:
            second.append(s[i])

    second = second[::-1]

    print("".join(first) + "".join(second))

#creating the main function
def main():
    themode = "off"
    while True:
        try:
            print("Current themode:", themode)
            if themode == "off":
                themode = input("themode(dec - decryption, enc - encryption)> ")
            else:
                s = input("String> ")
                if s == "#c":
                    themode = "off"
                elif s == "#q":
                    break
                elif themode == "dec":
                    print(decryption(s))
                elif themode == "enc":
                    print(encryption(s))
            print()

            if themode == "#q":
                break
        except:
            break

if __name__ == "__main__":
    main()
