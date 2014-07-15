Usage
#####

Supported operations:

- Basic arithmetic: addition, subtraction, multiplication, division, bitwise operations, sorting

Math works mostly like you expect it to, except for the special cases
where we mix bitmath types with Number types, and operations where two
bitmath types would cancel out (such as dividing two bitmath
types)

Instantiating any bitmath type is simple:

    one_kib = KiB(1)
    KiB(1.0)

Likewise, if you want to represent the same thing in bytes:

    one_kib_as_byte = Byte(1024)
    Byte(1024.0)

In these examples ``one_kib`` and ``one_kib_as_byte`` are equivalent
if tested with the ``==`` operator.


See [Examples](#examples) for more examples of supported operations.
