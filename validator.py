import sys
import inspect
import re


def class_and_func_matches(code):
    regex = "\nclass.*\(*\):|^class.*\(*\):|\ndef.*\(*\):|^def.*\(*\):"
    matches = re.findall(regex, code)
    return matches


def parse_and_divide_data(matches: list):
    """
    Parse and divide class and function
    Optional keyword arguments:
    matches: class and function matches
    return: tuple: 0-th index is list of functions name 1-th index is list of classes name
    """
    functions_name = []
    classes_name = []
    for match in matches:
        splited_match = match.split()
        name = splited_match[1].split("(")[0]

        if "class" == splited_match[0][-5:]:
            classes_name.append(name)
        else:
            functions_name.append(name)
    return functions_name, classes_name


def validate_functions_name(data: list):
    for name in data:
        if not name[0].isupper():
            print(1)
            sys.exit(1)


def validate_method_name(data: list):
    for cls_name in data:
        cls = globals()[cls_name]
        methods = dir(cls)
        for method in methods:
            if not method.startswith("__") and not method.endswith("__"):
                if not method[0].islower():
                    print(1)
                    sys.exit(1)


def main():
    code = inspect.getsource(file)
    matches = class_and_func_matches(code)
    func, cls = parse_and_divide_data(matches)
    validate_functions_name(func)
    validate_method_name(cls)
    print(0)
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        import_module = sys.argv[1][:-3]
    else:
        print('Please specify file. Input format should be "python3 validator.py <student file .py>')
    try:
        exec(f"from {import_module} import *")
        file = __import__(import_module)
    except:
        print(1)
        sys.exit(1)
    main()
