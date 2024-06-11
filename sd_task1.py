def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9 / 5) - 459.67


def convert_temperature(value, unit):
    if unit.lower() == 'c':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit.lower() == 'f':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit.lower() == 'k':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        raise ValueError("Invalid unit of measurement. Please enter 'C', 'F', or 'K'.")


def main():
    try:
        temp_value = float(input("Enter the temperature value: "))
        temp_unit = input("Enter the unit of the temperature (C, F, K): ")
        converted_values = convert_temperature(temp_value, temp_unit)

        if temp_unit.lower() == 'c':
            print(
                f"{temp_value} degrees Celsius is equal to {converted_values[0]:.2f} degrees Fahrenheit and {converted_values[1]:.2f} Kelvin.")
        elif temp_unit.lower() == 'f':
            print(
                f"{temp_value} degrees Fahrenheit is equal to {converted_values[0]:.2f} degrees Celsius and {converted_values[1]:.2f} Kelvin.")
        elif temp_unit.lower() == 'k':
            print(
                f"{temp_value} Kelvin is equal to {converted_values[0]:.2f} degrees Celsius and {converted_values[1]:.2f} degrees Fahrenheit.")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
