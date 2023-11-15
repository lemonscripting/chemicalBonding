import math

table = {
    #element name:chemical name, valency, group number, molar mass
    "hydrogen":["H", 1, 1, 1.0078],
    "carbon":["C", 4, 4, 12.011],
    "oxygen":["O", 2, 6, 15.999],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[],
    "":[]
}

def check_type(input_str):
    #if digits and alphabets exists at the same time
    if any(char.isdigit() for char in input_str) and any(char.isalpha() for char in input_str):
        status = "formula"
    #if full alphabets or alphabets with space
    elif any(char.isalpha() for char in input_str) and any(char.isspace() or char.isalpha() for char in input_str):
        status = "name"
    else:
        status = "undefined"
    return status

while True:

    first_line_un = input()
    first = first_line_un.split()
    first_element = first[0]
    second_element = first[1]

    valency_first_element = table[first_element][1]
    valency_second_element = table[second_element][1]

    type_first_element = check_type(first_element)
    type_second_element = check_type(second_element)
    
    if (not type_first_element == "formula"):
        first_element = table[first_element][0]
        print("mod", first_element)

    if (not type_second_element == "formula"):
        second_element = table[second_element][0]
        print("mod", second_element)

    if (valency_first_element == valency_second_element):
        output = first_element + second_element
        print("the bonded chemical formula is", output)
        continue
    
    if (not valency_first_element == valency_second_element):
        greatest_common_divisor = math.gcd(valency_first_element, valency_second_element)
        valency_first_element /= greatest_common_divisor
        valency_second_element /= greatest_common_divisor

        if (not valency_first_element == 1):
            if (any(char.isdigit() for char in valency_first_element)):
                first_element = "("+first_element+")"+valency_first_element
            else:
                first_element = first_element+valency_first_element
        
        if (not valency_second_element == 1):
            if (any(char.isdigit() for char in valency_second_element)):
                second_element = "("+second_element+")"+valency_second_element
            else:
                second_element = second_element+valency_second_element

        print("the bonded chemical formula is", first_element, second_element)

    if (type(first[0]) == str):

        print("string")
    elif (type(first[0]) == int):

        print("int")



    count = int(first[0])
    mana = int(first[1])
#access table["test"][0]

#add subscript
def translate_subscript(text):
    subscript_translation = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    subscripted_text = text.translate(subscript_translation)
    return subscripted_text

#usage - subscripted_formula = translate_subscript("H2O")





