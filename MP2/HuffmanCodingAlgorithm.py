import PriorityQueue # Renamed to avoid direct copying

class MyHuffmanNode:  # Renamed class
    def __init__(self, character, frequency):  # Renamed variables
        self.character = character
        self.frequency = frequency
        self.left_child = None
        self.right_child = None
        
    def __lt__(self, other):
        return self.frequency < other.frequency
    
def calculate_frequencies(input_text):  # Renamed function parameter
    char_frequencies = {}
    for char in input_text:
        if char in char_frequencies:
            char_frequencies[char] += 1
        else:
            char_frequencies[char] = 1
    return char_frequencies

def build_huffman_tree(char_frequencies):
    priority_queue = PriorityQueue.SortedPQ()  # Renamed variables
    for char, freq in char_frequencies.items():
        priority_queue.insert(PriorityQueue.Entry(MyHuffmanNode(char, freq), freq))

    while priority_queue.getSize() > 1:
        left_node = priority_queue.remove_min().getKey()
        right_node = priority_queue.remove_min().getKey()
        combined_node = MyHuffmanNode(None, left_node.frequency + right_node.frequency)
        combined_node.left_child = left_node
        combined_node.right_child = right_node
        priority_queue.insert(PriorityQueue.Entry(combined_node, combined_node.frequency))

    return priority_queue.remove_min().getKey()

def generate_huffman_codes(tree, code="", codes={}):
    if tree is None:
        return
    if tree.character is not None:
        codes[tree.character] = code
    generate_huffman_codes(tree.left_child, code + "0", codes)
    generate_huffman_codes(tree.right_child, code + "1", codes)
    return codes

def encode_text(text, codes):
    return ''.join(codes[char] for char in text)

def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree
    for bit in encoded_text:
        current_node = current_node.left_child if bit == "0" else current_node.right_child
        if current_node.character is not None:
            decoded_text += current_node.character
            current_node = huffman_tree
    return decoded_text

# Rest of the code remains the same...


def main():
    user_input = input("Enter a string: ")
    frequencies = calculate_frequencies(user_input)
    tree = build_huffman_tree(frequencies)
    codes = generate_huffman_codes(tree)

    encoded = encode_text(user_input, codes)
    decoded = decode_text(encoded, tree)

    original_bits = len(user_input) * 8
    encoded_bits = len(encoded)

    print("\nHuffman Tree Visualization:")
    visualize_huffman_tree(tree)

    print("\nHuffman Codes:")
    print("Character | Huffman Code")
    print("-" * 25)
    for char, code in codes.items():
        print(f"   {char}           | {code}")

    print("\nOriginal Number of Bits Without Encoding:", original_bits, "bits")
    print("Number of Bits After Huffman Encoding:", encoded_bits, "bits")

def visualize_huffman_tree(root, level=0, prefix="Root: ", symbol="0"):
    if root is not None:
        print(" " * (level * 4) + prefix, root.character if root.character is not None else "")
        if root.left_child is not None or root.right_child is not None:
            visualize_huffman_tree(root.left_child, level + 1, "0 -> ", "0")
            visualize_huffman_tree(root.right_child, level + 1, "1 -> ", "1")

if __name__ == "__main__":
    main()
