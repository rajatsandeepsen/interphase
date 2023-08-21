__all__ = ['typeHead', 'typeBody']

def typeHead(x, export, interface):
    variant:str
    if interface:
         variant = "interface " + x
    else:
        variant = "type " + x + " ="

    if export:
        return "export " + variant
    else:
        return variant

def isFunc(x):
    return isinstance(x, function)

def isDist(x):
    return isinstance(x, dict)

def isArray(x):
    return isinstance(x, list)

def returnTypescript(x:any)->str:
    typed = type(x)
    if typed == str:
        return "string"
    elif typed == int:
        return "number"
    elif typed == type(isFunc):
        return "() => void"
    elif typed == bool:
        return "boolean"
    # add more types here
    else :
        return ''

def returner(*set:any) -> str:
    sum = ''
    for i in set:
        sum += i + " "
    return sum

def typeBody(x, y):
    text = ''
    space = "\t" * y
    if isDist(x):
        text += returner(space,"{\n")
        for key, value in x.items():
            if isDist(value):
                text += returner(key + ":", typeBody(value, y + 1) + ",\n")
            elif isArray(value):
                text += returner(key + ":", typeBody(value[0], y + 1) + "[]" + ",\n")
            else:
                text += returner(space + key + ":",returnTypescript(value) + ",\n")
        text += returner("}")

    else:
        if isArray(x):
            text += returner(typeBody(x[0], y), "[]")
        else:
            text += " " + returnTypescript(x)

    return text