__all__ = ['typeHead', 'typeBody', 'returner']

from .addons import iF

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
    return isinstance(x, list or tuple)

def returnTypescript(x:any)->str:
    typed = type(x)
    if typed == str:
        return "string"
    elif typed == int or typed == float:
        return "number"
    elif typed == type(isFunc):
        return "() => void"
    elif typed == bool:
        return "boolean"
    elif typed == type(None):
        return "null"
    
    
    # add more types here
    else :
        return ''

def returner(*set:any) -> str:
    return ' '.join(set)
def typeBody(x, y):
    text = ''
    space = "\t" * y
    if isDist(x):
        flag = False
        text += "{"
        for key, value in x.items():
            if not flag:
                text += "\n"
                flag = True

            if isDist(value):
                text += returner(space + key + ":", typeBody(value, y + 1) + ",\n")
            elif isArray(value):
                text += returner(space + key + ":", typeBody(value[0], y + 1) + "[]" + ",\n")
            else:
                text += returner(space + key + ":",returnTypescript(value) + ",\n")
        text += iF(flag, space + "}", "}")

    else:
        if isArray(x):
            text += returner(space, typeBody(x[0], y), "[]")
        else:
            text += returnTypescript(x)

    return text