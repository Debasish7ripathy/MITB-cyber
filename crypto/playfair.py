#basic rules
'''
1.we have to create a matrix
2.we have to fill the matrix with all the non filled character after filling the key
3.split the plain texty into pairs 
    a.if repetation of word occure then we have to add a buffer character
    b.else continue
4.now follow the below 3
    a.if pair is in same column then shift down(a[i][j]==a[i][(j+1)%rows])\
    b.if pair is in same row then shift right(a[i][j]==a[(i+1)%columns][j])
    c.if pair forms a rectangle then swap row remain same column changes ie a[i][j] and b[k][l] will become a[i][l] and b[k][j]
'''
def create_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    matrix += ''.join(chr(i) for i in range(65, 91) if chr(i) not in matrix and chr(i) != 'J')
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(letter, matrix):
    for r, row in enumerate(matrix):
        for c, char in enumerate(row):
            if char == letter:
                return r, c

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = ''.join(plaintext.upper().replace('J', 'I').split())
    prepared_text = [plaintext[i:i+2] if plaintext[i] != plaintext[i+1] else plaintext[i] + 'X'
                     for i in range(0, len(plaintext), 2)]
  
    ciphertext = []
    for digraph in prepared_text:
        if len(digraph) < 2: digraph += 'X'  # Handle odd lengths
        r1, c1 = find_position(digraph[0], matrix)
        r2, c2 = find_position(digraph[1], matrix)
        if r1 == r2:  # Same row
            ciphertext.extend([matrix[r1][(c1 + 1) % 5], matrix[r2][(c2 + 1) % 5]])
        elif c1 == c2:  # Same column
            ciphertext.extend([matrix[(r1 + 1) % 5][c1], matrix[(r2 + 1) % 5][c2]])
        else:  # Rectangle
            ciphertext.extend([matrix[r1][c2], matrix[r2][c1]])
    return ''.join(ciphertext)

# Example usage
key = "PLAYFAIR EXAMPLE"
plaintext = "HIDE THE GOLD IN THE TREE"
encrypted = playfair_encrypt(plaintext, key)
print("Encrypted Message:", encrypted)
