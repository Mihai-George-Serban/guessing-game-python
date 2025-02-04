import random


numbers = []


def generate_list():
    for i in range(0, 10):
        n = random.randint(1, 99)
        numbers.append(n)
    return numbers


def get_guess():
    for i in range(0, 10):
        g = int(input("Enter an integer from 1 to 99: "))
        while numbers[i] != g:
            if g < numbers[i]:
                print("guess is low")
                g = int(input("Enter an integer from 1 to 99: "))
            elif g > numbers[i]:
                print("guess is high")
                g = int(input("Enter an integer from 1 to 99: "))
            else:
                break
        print("you guessed it!")


def main():
    generate_list()
    get_guess()


main()
