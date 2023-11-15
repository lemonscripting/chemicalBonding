#---Other dependencies-----------------------------------------
import math

def translate_subscript(text):
    subscript_translation = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    subscripted_text = text.translate(subscript_translation)
    return subscripted_text

def check_type(input_str):
    if any(char.isdigit() for char in input_str) and any(char.isalpha() for char in input_str):
        status = "formula"
    elif any(char.isalpha() for char in input_str) and any(char.isspace() or char.isalpha() for char in input_str):
        status = "name"
    else:
        status = "undefined"
    return status

table = {
    "hydrogen":["H", 1, 1, 1.0078],
    "carbon":["C", 4, 4, 12.011],
    "oxygen":["O", 2, 6, 15.999],
}

#--------------------------------------------------------------

def bond(x,y):
    first_element = x.lower()
    second_element = y.lower()
    valency_first_element = int(table[first_element][1])
    valency_second_element = int(table[second_element][1])
    type_first_element = check_type(first_element)
    type_second_element = check_type(second_element)
    if (not type_first_element == "formula"):
        first_element = table[first_element][0]
    if (not type_second_element == "formula"):
        second_element = table[second_element][0]
    if (valency_first_element == valency_second_element):
        output = first_element + second_element
        subscripted_formula = translate_subscript(output)
        return subscripted_formula
    if (not valency_first_element == valency_second_element):
        greatest_common_divisor = math.gcd(valency_first_element, valency_second_element)
        valency_first_element /= greatest_common_divisor
        valency_second_element /= greatest_common_divisor
        valency_first_element = int(valency_first_element)
        valency_second_element = int(valency_second_element)
        if (not valency_second_element == 1):
            if (any(char.isdigit() for char in first_element)):
                first_element = "("+first_element+")"+valency_second_element
            else:
                first_element = first_element+str(valency_second_element)
        if (not valency_first_element == 1):
            if (any(char.isdigit() for char in second_element)):
                second_element = "("+second_element+")"+valency_first_element
            else:
                second_element = second_element+str(valency_first_element)
        output = first_element + second_element
        subscripted_formula = translate_subscript(output)
        return subscripted_formula
result = bond("carbon", "oxygen")
print(result)