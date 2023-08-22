from Interphase.interphase import Interphase

x = Interphase("./types", d_ts = True)
print(x)

# x.write("type", "test", {"hh": "test"}, False)
# x.write("type", "test", ["bhb"], False)
# x.write("type", "", {"dsf": "test"}, False)
# x.write("", "dd", {"sdfs": "test"}, False)

x.write("type", "test", {
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": "ksdhj"
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": False,
    "married": True,
    "name": {},
    "pets": None,
} , True)