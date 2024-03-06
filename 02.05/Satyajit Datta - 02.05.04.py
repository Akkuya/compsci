length = int(input("Enter the material length (m): "))

three_metre_lengths = length // 3

excess = length % 3 * 100

print(str(length) + "m fabric will result in", three_metre_lengths, "3-metre-lengths with", str(excess) + "cm left over.")