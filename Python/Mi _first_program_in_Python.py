import math

def calculate_square_root(numero):
    if numero < 0:
        print("You cannot calculate the square root of a negative number.")
        return None
    else:
        return math.sqrt(numero)


def main():
    numero = float(input("Enter a number to calculate its square root: "))
    resultado = calculate_square_root(numero)
    if resultado is not None:
        print(f"The square root of  {numero} is: {resultado}")

if __name__ == "__main__":
    main()