import time

def huffman(chars, freq):
    nodes = []

    # Create leaf nodes
    for i in range(len(chars)):
        nodes.append([freq[i], chars[i], None, None])

    # Build Huffman tree
    while len(nodes) > 1:

        # Find smallest frequency
        min1 = 0
        for i in range(1, len(nodes)):
            if nodes[i][0] < nodes[min1][0]:
                min1 = i

        left = nodes.pop(min1)

        # Find second smallest frequency
        min2 = 0
        for i in range(1, len(nodes)):
            if nodes[i][0] < nodes[min2][0]:
                min2 = i

        right = nodes.pop(min2)

        # Combine the two nodes
        parent = [left[0] + right[0], "", left, right]
        nodes.append(parent)

    # Generate Huffman codes
    codes = {}

    def generate_codes(node, code):
        if node[2] is None and node[3] is None:
            codes[node[1]] = code if code else "0"
            return

        generate_codes(node[2], code + "0")
        generate_codes(node[3], code + "1")

    generate_codes(nodes[0], "")
    return codes


# Main program
n = int(input("Enter number of characters: "))

chars = []
freq = []

for i in range(n):
    chars.append(input("Enter character: "))
    freq.append(int(input("Enter frequency: ")))

if n <= 0 or len(set(chars)) != n or any(f <= 0 for f in freq):
    print("Invalid input")
else:
    start = time.perf_counter()

    codes = huffman(chars, freq)

    end = time.perf_counter()

    print("Huffman Codes:")
    for ch in chars:
        print(ch, ":", codes[ch])

    print("Execution time:", end - start, "seconds")