def f(cnt):
    sequence = [0, 1]
    sequence_even = [0]
    print(sequence)
    while len(sequence_even) < cnt:
        new = sequence[len(sequence)-1] + sequence[len(sequence)-2]
        sequence.append(new)
        if new % 2 == 0:
            sequence_even.append(new)
    
    print(sequence)
    print(sequence_even)

f(100)
