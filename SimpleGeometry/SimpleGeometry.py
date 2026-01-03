"""
Made by Tatpoato

This python library helps you with the math of different shapes:
Commands:
formulas(shape) -- formulas allows you to rewiew the formulas of either a square or a circle (if you forgot them)
allesumcircle(r=,d=,c=,a=) -- allesumcircle allows you to input either the radius (r) or the diameter (d) or the circumference (c) or the area (a) and gain access to all the other variables with the simple command. you can also turn printing off by doing Print=False.
allesumsquare(s=,a=,p=,d=, Print=False) -- allesumsquare allows you to input either the sides (s) or the area (a) or the perimeter (p) or the diagonal (d) and gain access to all the other variables. you can also turn printing off by doing Print=False.
Variables that come with this library:
pi -- the pi variable is just your standard pi (3.14159265358979323846264338)
"""


def formulas(shape):
    print("Info:")
    print("I currently give you all the ways to get to one base which i base the rest of the formulas off")
    print("translation:")
    print("-- / is to divide", "-- * is to multiply", "-- ** is to take something to the power of something else", "-- ** 0.5 is the square root of something", "", sep="\n")
    if shape == "circle":
        print("Circle:")
        print("Everything for the radius:")
        print("r = diameter / 2", "r = circumference / pi (3.14) / 2", "r = Area / pi (3.14)", sep="\n")
        print("Diameter formula")
        print("d = radius * 2 (the diameter is double the radius.)")
        print("Area formula")
        print("a = pi (3.14) * radius ** 2")
        print("Circumference formula")
        print("c = 2 * pi (3.14) * r")
    if shape == "square":
        print("Everything for the sides")
        print("s = Perimeter / 4", "s = Area ** 0.5", "s = diagonal / 2 ** 0.5")
        print("Perimeter formula")
        print("p = Side * 4")
        print("Area formula")
        print("a = side * side (side ** 2)")
        print("Diagonal formula (Pythagoras)")
        print("d = 2 ** 0.5 * s")


pi = 3.14159265358979323846264338


def allesumcircle(r=None, d=None,c=None,a=None, Print=True, Dict=False):
    actuallyinputtedstuff = True
    if r is not None:
        circ = 2 * pi * r
        diam = r * 2
        a = pi * r **2
        woah = (f"Circumference = {circ}\n"
                f"Radius = {r}\n"
                f"Diameter = {diam}\n"
                f"Area = {a}\n")
    elif d is not None:
        diam = d
        r = d / 2
        circ = 2 * pi * r
        a = pi * r ** 2
        woah = (f"Circumference = {circ}\n"
                f"Radius = {r}\n"
                f"Diameter = {diam}\n"
                f"Area = {a}\n")
    elif c is not None:
        diam = c / pi / 2
        r = diam / 2
        a = pi * r ** 2
        woah = (f"Circumference = {c}\n"
                f"Radius = {r}\n"
                f"Diameter = {diam}\n"
                f"Area = {a}\n")
    elif a is not None:
        r = a / pi
        r = r ** 0.5
        circ = 2 * pi * r
        diam = r * 2
        woah = (f"Circumference = {circ}\n"
                f"Radius = {r}\n"
                f"Diameter = {diam}\n"
                f"Area = {a}\n")
    else:
        woah = "D:"
        actuallyinputtedstuff = False

    if Print == False and Dict == False:
        return woah
    elif Print == True:
        print(woah)
    elif Dict == True and actuallyinputtedstuff != False:
        return {"radius": r, "diameter": diam, "circumference": circ, "area": a}
    else:
        woah = "How did you reach this?"





def allesumsquare(s=None, a=None, p=None, d=None, Print=True, Dict=False):
    actuallyinputtedstuff = True
    if s is not None:
        a = s * s
        p = s * 4
        d = 2 ** 0.5 * s
        woah = (f"Side = {s}\n"
                f"Area = {a}\n"
                f"Perimeter = {p}\n"
                f"Diagonal = {d}\n")


    elif a is not None:
        s = a ** 0.5
        p = s * 4
        d = 2 ** 0.5 * s
        woah = (f"Side = {s}\n"
                f"Area = {a}\n"
                f"Perimeter = {p}\n"
                f"Diagonal = {d}\n")


    elif p is not None:
        s = p / 4
        a = s * s
        d = 2 ** 0.5 * s
        woah = (f"Side = {s}\n"
                f"Area = {a}\n"
                f"Perimeter = {p}\n"
                f"Diagonal = {d}\n")

    elif d is not None:
        s = d / 2 ** 0.5
        a = s * s
        p = s * 4
        woah = (f"Side = {s}\n"
                f"Area = {a}\n"
                f"Perimeter = {p}\n"
                f"Diagonal = {d}\n")


    else:
        woah = "D:"
        actuallyinputtedstuff = False

    if Print == False and Dict == False:
        return woah
    elif Print == True:
        print(woah)
    elif Dict == True and actuallyinputtedstuff != False:
        return {"side": s, "area": a, "perimeter": p, "diagonal": d}
    else:
        print("How did you reach this?")
