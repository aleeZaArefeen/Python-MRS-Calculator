import sys
def main_program():
    print("------------------------------------------------------")
    print("---------------PYTHON MRS CALCULATOR------------------")
    print("------------------------------------------------------")
    print("--------Accepted Utility Functions and Formats--------")
    print("Cobb Douglas: ax^c * by^d")
    print("CES: ax^b + by^d")
    print("Perfect Substitutes: ax + by")
    print("Perfect Complements: min(ax^c, by^d)")
    print("Quasi-Linear: ax^c + y")
    print("------------------------------------------------------")
    print("-------------------Additional Notes-------------------")
    print("Please ensure you use x and y respectively so that the")
    print("program can function properly.")
    print("The 'y =' at the start is not needed, please just type")
    print("your utility function in the formats given above.")
    print("------------------------------------------------------")

    user_selection = str(input("Please enter the utility function you wish to calculate the MRS for, or 'EXIT' to exit. >>> "))

    if (user_selection.count("^") == 2) & (user_selection.__contains__("*")):
        print(MRS.cobb_douglas(user_selection))
        main_program()
    elif (user_selection.count("^") == 2):
        print(MRS.ces(user_selection))
        main_program()
    elif (user_selection.count("^") == 0) & (user_selection.__contains__("+")):
        print(MRS.p_subs(user_selection))
        main_program()
    elif (user_selection.startswith("min")):
        print(MRS.p_comps(user_selection))
        main_program()
    elif (user_selection.count("^") == 1):
        print(MRS.quasi_linear(user_selection))
        main_program()
    elif user_selection == "EXIT":
        print("Thanks for using the program, hope it was helpful!")
        sys.exit()
    else:
        print("Invalid Utility Function.")
        main_program()

def signed_coefficient(coefficient: float) -> float:
    """Helper function for parse_utility to rightfully assign a variable of 1 or -1 depending on the coefficient's sign.
    """
    if coefficient == "":
        coefficient = "1.0"
    elif coefficient == "-":
        coefficient = "-1.0"
    return coefficient

def parse_utility(utility_function: str) -> list:
    """Helper function to parse a given utility function.
       Returns a list with the coefficients and exponents for x and y.
    """
    x_coef = utility_function[:utility_function.find("x")]
    x_coef = signed_coefficient(x_coef) # check for signed coefficients
    y_coef = utility_function[utility_function.rfind(" ") + 1:utility_function.find("y")]
    y_coef = signed_coefficient(y_coef)

    x_exp = utility_function[utility_function.find("^") + 1:utility_function.find(" ")]
    y_exp = utility_function[utility_function.rfind("^") + 1:]

    return [x_coef, x_exp, y_coef, y_exp]

class MRS:
    def cobb_douglas(utility_function: str) -> float:
        """Calculates and returns the MRS for a Cobb Douglas as a float.
           Format: ax^c * by^d, where d = 1 - c
        """
        cd_values = parse_utility(utility_function)
        x_exp = float(cd_values[1])
        y_exp = float(cd_values[3])

        condition = 1 - float(x_exp)

        if float(y_exp) == condition: # check d =  1 - c condition
            return str((format((x_exp)/(y_exp), '.2f'))) + "(y/x)"
        return "Invalid Cobb Douglas utility function. Exponents must sum up to 1."

    def ces(utility_function: str) -> float:
        """Calculates and returns the MRS for a CES function as a float.
           Format: ax^c + by^d, where c = d
        """
        ces_values = parse_utility(utility_function)
        x_coef = float(ces_values[0])
        x_exp = float(ces_values[1])
        y_coef = float(ces_values[2])
        y_exp = float(ces_values[3])

        derivative_exp = -1*(x_exp - 1)

        if float(x_exp) == float(y_exp): # check c = d condition
            return str(format((x_coef*x_exp)/(y_coef*y_exp), '.2f')) + "(y/x)^" + str(derivative_exp)
        return "Invalid CES utility function. Exponents must be the same."

    def p_subs(utility_function: str) -> int:
        """Calculates the MRS for a Perfect Substitute function.
           Format: ax + by
        """
        p_subs_values = parse_utility(utility_function)
        x_coef = float(p_subs_values[0])
        y_coef = float(p_subs_values[2])

        return str(format((x_coef/y_coef), '.2f'))

    def p_comps(utility_function: str) -> int:
        """Calculates the MRS for a Perfect Complement function.
        Format: min(ax^c, by^d)
        """
        trim_utility = utility_function[4:-1] # split utility_function to omit "min(...)"
        p_comps_values = parse_utility(trim_utility)

        x_coef = float(p_comps_values[0])
        x_exp = trim_utility[trim_utility.find("^") + 1:trim_utility.find(",")] # new way to extract values, since format different
        if "x" in x_exp:
            x_exp = 1.0
        y_coef = float(p_comps_values[2])
        y_exp = trim_utility[trim_utility.rfind("^") + 1:]
        if "y" in y_exp:
            y_exp = 1.0

        return str(x_coef) + "x^" + str(x_exp) + " = " + str(y_coef) + "y^" + str(y_exp) + ", simplify for tangency condition."

    def quasi_linear(utility_function: str) -> int:
        """Calculates the MRS for a Quasi-Linear function.
        Format: ax^c + y
        """
        quasi_linear_values = parse_utility(utility_function)
        x_coef = float(quasi_linear_values[0])
        x_exp = float(quasi_linear_values[1])
        y_coef = float(quasi_linear_values[2])

        derivative_exp = x_exp - 1

        return str(format(((x_coef*x_exp)/y_coef), '.2f')) + "x^" + str(derivative_exp)

if __name__ == '__main__':
    main_program()