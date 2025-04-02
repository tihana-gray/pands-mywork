# program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Tihana Gray

def sqrt(number):
    guess = number / 2
    tolerance = 0.00001

    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2

    return guess

def main():
    try:
        number = float(input("Please enter a positive number: "))
        if number <= 0:
            print("Number must be positive.")
            return
        result = sqrt(number)
        print(f"The square root of {number} is approx. {result:.1f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
