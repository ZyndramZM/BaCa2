from pathlib import Path
from re import findall, split
from BaCa2.settings import BASE_DIR

#any non-empty value is allowed
def isAny(val):
    return bool(val)

#check if val is None
def isNone(val):
    return val is None

#check if val can be converted to int
def isInt(val):
    if type(val) == float:
        return False
    try:
        int(val)
        return True
    except ValueError:
        return False

#check if val is a int value between a and b
def isIntBetween(val, a: int, b: int):
    if isInt(val):
        if a <= val < b:
            return True
    return False

#check if val can be converted to float
def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

#check if val is a float value between a and b
def isFloatBetween(val, a: int, b: int):
    if isFloat(val):
        if a <= val < b:
            return True
    return False

#check if val can be converted to string
def isStr(val):
    if type(val) == str:
        return True
    return False

#check if val is exacly like schema
def is_(val, schema: str):
    if isStr(val):
        return val == schema
    return False

#check if val is in args
def isIn(val, *args):
    return val in args

#check if val is string and has len < len(l)
def isShorter(val, l: int):
    if isStr(val):
        return len(val) < l
    return False

#check if val has dict type
def isDict(val):
    return type(val) == dict

#check if val is path in package_dir
def isPath(val):
    if val is None:
        return False
    try:
        val = Path(val)
        if val.exists():
            return True
        return False
    except ValueError:
        return False

#takes the validator function with arguments, and check that if validator function is true for arg (other arguments for func)
def resolve_validator(func_list, arg):
    func_name = str(func_list[0])
    func_arguments_ext = ',' + ','.join(func_list[1:])
    return eval(func_name + '("' + str(arg) + '"' + func_arguments_ext + ')')

#check if val has structure provided by struct and fulfills validators functions from struct
def hasStructure(val, struct: str):
    validators = findall("<.*?>", struct)
    validators = [i[1:-1].split(',') for i in validators]
    constant_words = findall("[^<>]{0,}<", struct) + findall("[^>]{0,}$", struct)
    constant_words = [i.strip("<") for i in constant_words]
    if len(validators) == 1:
        values_to_check = [val]
    else:
        # words_in_pattern = [i for i in constant_words if i != '|' and i != '']
        # regex_pattern = '|'.join([i for i in constant_words if i != '|' and i != ''])
        values_to_check = split('|'.join([i for i in constant_words if i != '|' and i != '']), val)
    if struct.startswith('<') == False:
        values_to_check = values_to_check[1:]
    valid_idx = 0
    const_w_idx = 0
    values_idx = 0
    temp_alternative = False
    result = True
    while valid_idx < len(validators) and values_idx < len(values_to_check):
        temp_alternative |= resolve_validator(validators[valid_idx], values_to_check[values_idx])
        if constant_words[const_w_idx] == '|':
            if constant_words[const_w_idx + 1] != '|':
                values_idx += 1
        else:
            if constant_words[const_w_idx + 1] != '|':
                values_idx += 1
                result &= temp_alternative
                temp_alternative = False
        valid_idx += 1
        const_w_idx += 1
    return result

#do memory converting from others units to bytes  --> do wyci??gni??cia z tego pliku
def memory_converting(val: str):
    if val[-1] == 'B':
        return int(val[0:-1])
    elif val[-1] == 'K':
        return int(val[0:-1]) * 1024
    elif val[-1] == 'M':
        return int(val[0:-1]) * 1024 * 1024
    elif val[-1] == 'G':
        return int(val[0:-1]) * 1024 * 1024 * 1024

#check if first is smaller than second considering memory
def valid_memory_size(first: str, second: str):
    if memory_converting(first) <= memory_converting(second):
        return True
    return False

#check if val has structure like <isInt><isIn, 'B', 'K', 'M', 'G'>
def isSize(val :str, max_size: str):
    val = val.strip()
    return hasStructure(val[:-2], "<isInt>") and hasStructure(val[-1], "<isIn, 'B', 'K', 'M', 'G'>") and valid_memory_size(val, max_size)

#check if val is a list and every element from list fulfill at least one validator from args
def isList(val, *args):
    if type(val) == list:
        result = False
        for i in val:
            for j in args:
                result |= hasStructure(i, j)
            if not result:
                return result
    return True