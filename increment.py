from re import sub
def main(a):
    b = a.split("+=")
    return f"{b[0]}<- {b[0]} + {b[1]}"
def decrement(a):
    b = a.split("-=")
    return f"{b[0]}<- {b[0]} - {b[1]}"
