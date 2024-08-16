key = "6aa4aa2aa1aa3aa5aa7aa8"

def dosuff(text):
    global key
    try:
        temp_key = key.split("aa")
        key = []
        for i in temp_key:
            key.append(int(i))
    except:
        pass
    d = text
    user_input = text
    user_input = text_to_binary(user_input)
    user_input_list = user_input.split(" ")
    if d[0] == "-" and d[1] == "-" and d[2] == "9" and d[len(d)-3] == "9" and d[len(d)-2] == "-" and d[len(d)-1] == "-":
        jk = decrypt(make_long(d))
        return(jk)
    else:
        x = make_short(encryt(user_input_list,key))
        return(x)

def text_to_binary(s):
    return ' '.join(format(ord(c), '08b') for c in s)

def binary_to_text(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def encryt(text_in_binary_list, key):
    global encryted_text_in_binary
    global encryted_text_in_binary_list
    # Io = ["1", "0"]
    # user_nums = []
    # for i in range(12):
    #     f = ""
    #     for _ in range(8):
    #         f = f+random.choice(Io)
    #     user_nums.append(f)
    # user_nums_string = ""
    # for i in user_nums:
    #     user_nums_string += i
    encryted_text_in_binary_list = []
    for i in text_in_binary_list:
        user_final = i#+user_nums_string
        for x in key:
            encryted_text_in_binary_list.append(user_final[x-1])
        encryted_text_in_binary = ""
        for i in encryted_text_in_binary_list:
            encryted_text_in_binary += i
    return encryted_text_in_binary

def make_short(bin_str):
    def replace_pairs(data, pairs):
        for pair, replacement in pairs.items():
            indices = [i for i, x in enumerate(data) if x == pair]
            for i in indices:
                try:
                    data[i] = replacement
                except IndexError:
                    pass
        return data

    def split_to_pairs(data):
        pairs = []
        temp = ""
        for i in data:
            temp += str(i)
            if len(temp) == 2:
                pairs.append(temp)
                temp = ""
        return pairs

    z = split_to_pairs(bin_str)

    pair_replacements_1 = {"10": "a", "01": "b", "11": "c", "00": "d"}
    z = replace_pairs(z, pair_replacements_1)
    
    z = split_to_pairs(z)

    pair_replacements_2 = {
        "ab": "q", "ac": "w", "ad": "!", "ba": "e", "bc": "r", "bd": "g",
        "ca": "t", "cb": "%", "cd": "&", "aa": "@", "bb": "#", "cc": "o",
        "dc": "j", "db": "k", "da": "l"
    }
    z_2 = replace_pairs(z, pair_replacements_2)
    
    z_2.reverse()
    z_2.append("--9")
    z_2.reverse()
    z_2.append("9--")
    
    return ''.join(z_2)

def make_long(enc_text):
    # Check for valid start and end markers
    if enc_text.startswith("--9") and enc_text.endswith("9--"):
        # Strip off the identity markers
        enc_text = enc_text[3:-3]
        
        # Dictionary for first round of replacements
        replacements_1 = {
            "q": "ab", "w": "ac", "!": "ad", "e": "ba", "r": "bc", "g": "bd",
            "t": "ca", "%": "cb", "&": "cd", "@": "aa", "#": "bb", "o": "cc",
            "j": "dc", "k": "db", "l": "da"
        }
        
        # Perform first round of replacements
        z_2 = [replacements_1.get(char, char) for char in enc_text]
        
        # Join the result for the next processing step
        z_2_string = ''.join(z_2)
        
        # Dictionary for second round of replacements
        replacements_2 = {
            "a": "10", "b": "01", "c": "11", "d": "00"
        }
        
        # Perform second round of replacements
        z = [replacements_2.get(char, char) for char in z_2_string]
        
        # Return the final reconstructed binary string
        return ''.join(z)
    else:
        return False

def decrypt(bin):
    c = 0
    temp = ""
    z = []
    for i in bin:
        c += 1
        if len(temp) == 8:
            z.append(temp)
            temp = ""
            temp += str(i)
        else:
            temp += str(i)
            if len(temp) == 8:
                z.append(temp)
                temp = ""
    decrypted_text_in_binary_list = []
    for i in z:
        user_final = i
        for i in range(1,9):
            y = key.index(i)
            decrypted_text_in_binary_list.append(user_final[y])
    decrypted_text_in_binary = ""
    for i in decrypted_text_in_binary_list:
        decrypted_text_in_binary += i
    return binary_to_text(decrypted_text_in_binary)