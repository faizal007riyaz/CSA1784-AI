from itertools import permutations

def solve_cryptarithmetic():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')

    # Generate all possible digit assignments
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Convert words to numbers
        send = (mapping['S'] * 1000 +
                mapping['E'] * 100 +
                mapping['N'] * 10 +
                mapping['D'])

        more = (mapping['M'] * 1000 +
                mapping['O'] * 100 +
                mapping['R'] * 10 +
                mapping['E'])

        money = (mapping['M'] * 10000 +
                 mapping['O'] * 1000 +
                 mapping['N'] * 100 +
                 mapping['E'] * 10 +
                 mapping['Y'])

        # Check equation
        if send + more == money:
            print("Solution Found:")
            for letter, digit in sorted(mapping.items()):
                print(f"{letter} = {digit}")

            print("\nSEND  =", send)
            print("MORE  =", more)
            print("MONEY =", money)
            return

    print("No solution found")

# Run the program
solve_cryptarithmetic()
