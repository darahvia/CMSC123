import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    priority_queue = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def generate_huffman_codes(root, current_code, codes):
    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        generate_huffman_codes(root.left, current_code + "0", codes)
        generate_huffman_codes(root.right, current_code + "1", codes)

def huffman_encoding(data):
    root = build_huffman_tree(data)
    codes = {}
    generate_huffman_codes(root, "", codes)

    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, codes

def main():
    user_input = input("Enter a string: ")
    encoded_data, codes = huffman_encoding(user_input)

    original_bits = len(user_input) * 8
    encoded_bits = len(encoded_data)

    print("\nHuffman Tree Visualization:")
    visualize_huffman_tree(build_huffman_tree(user_input))

    print("\nHuffman Codes:")
    print("Character | Huffman Code")
    print("-" * 25)
    for char, code in codes.items():
        print(f"   {char}           | {code}")

    print("\nOriginal Number of Bits Without Encoding:", original_bits, "bits")
    print("Number of Bits After Huffman Encoding:", encoded_bits, "bits")

def visualize_huffman_tree(root, level=0, prefix="Root: ", symbol="0"):
    if root is not None:
        print(" " * (level * 4) + prefix, root.char if root.char is not None else "")
        if root.left is not None or root.right is not None:
            visualize_huffman_tree(root.left, level + 1, "0 -> ", "0")
            visualize_huffman_tree(root.right, level + 1, "1 -> ", "1")

if __name__ == "__main__":
    main()
