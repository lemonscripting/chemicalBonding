import math

table = {
    #element name:chemical name, valency, group number, molar mass
    "hydrogen":["H", 1, 1],
    "carbon":["C", 4, 4],
    "oxygen":["O", 2, 6],
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
def translate_subscript(text):
    subscript_translation = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    subscripted_text = text.translate(subscript_translation)
    return subscripted_text

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
    
    first_element = first[0].lower()
    second_element = first[1].lower()

    valency_first_element = int(table[first_element][1])
    valency_second_element = int(table[second_element][1])

    print(valency_first_element)
    print(valency_second_element)
        
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
        subscripted_formula = translate_subscript(output)
        print("the bonded chemical formula is", subscripted_formula)
        continue
    
    if (not valency_first_element == valency_second_element):
        greatest_common_divisor = math.gcd(valency_first_element, valency_second_element)
        valency_first_element /= greatest_common_divisor
        valency_second_element /= greatest_common_divisor
        
        valency_first_element = int(valency_first_element)
        valency_second_element = int(valency_second_element)
        print(valency_first_element)
        print(valency_second_element)
        if (not valency_second_element == 1):
            if (any(char.isdigit() for char in first_element)):
                first_element = "("+first_element+")"+valency_second_element
                print("valency second", valency_second_element)
            else:
                first_element = first_element+str(valency_second_element)
        
        if (not valency_first_element == 1):
            if (any(char.isdigit() for char in second_element)):
                second_element = "("+second_element+")"+valency_first_element
                print("valency first", valency_first_element)
            else:
                second_element = second_element+str(valency_first_element)
        output = first_element + second_element
        subscripted_formula = translate_subscript(output)
        print("the bonded chemical formula is", subscripted_formula)
        continue