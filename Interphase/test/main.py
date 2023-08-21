from Interphase import Interphase

x = Interphase("./types", d_ts = True)
print(x)

x.write("type", "test", {"hh": "test"}, False)
x.write("type", "test", ["bhb"], False)
x.write("type", "", {"dsf": "test"}, False)
x.write("", "dd", {"sdfs": "test"}, False)