import heapq
from collections import Counter, namedtuple


# Define a Node for the Huffman tree
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq  # Required for heap comparisons


def build_huffman_tree(data):
    # Count frequency of each byte/character
    freq = Counter(data)
    heap = [Node(ch, f, None, None) for ch, f in freq.items()]
    heapq.heapify(heap)

    # Build tree by combining two smallest nodes repeatedly
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook


def compress(data):
    # Build tree and code mapping
    tree = build_huffman_tree(data)
    codes = build_codes(tree)

    # Encode the data
    encoded_data = ''.join(codes[ch] for ch in data)
    return encoded_data, tree, codes


def decompress(encoded_data, tree):
    result = []
    node = tree
    for bit in encoded_data:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            result.append(node.char)
            node = tree
    return ''.join(result)


# Example usage
if __name__ == "__main__":
    text = "huffman encoding is fun"
    encoded, tree, codes = compress(text)
    print("Codes:", codes)
    print("Encoded:", encoded)
    decoded = decompress(encoded, tree)
    print("Decoded:", decoded)
