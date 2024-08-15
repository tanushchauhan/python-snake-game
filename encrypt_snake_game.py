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
    if enc_text[0] == "-" and enc_text[1] == "-" and enc_text[2] == "9" and enc_text[len(enc_text)-3] == "9" and enc_text[len(enc_text)-2] == "-" and enc_text[len(enc_text)-1] == "-":
        enc_text_list = []
        for i  in enc_text:
            enc_text_list.append(i)
        enc_text_list[0] = ""
        enc_text_list[1] = ""
        enc_text_list[2] = ""
        enc_text_list[len(enc_text)-3] = ""
        enc_text_list[len(enc_text)-2] = ""
        enc_text_list[len(enc_text)-1] = ""
        z_2 = enc_text_list
        indices_ab = [i for i, x in enumerate(enc_text_list) if x == "q"]
        for i in indices_ab:
            try:
                z_2[i] = "ab"
            except:
                pass
        indices_ac = [i for i, x in enumerate(enc_text_list) if x == "w"]
        for i in indices_ac:
            try:
                z_2[i] = "ac"
            except:
                pass
        indices_ad = [i for i, x in enumerate(enc_text_list) if x == "!"]
        for i in indices_ad:
            try:
                z_2[i] = "ad"
            except:
                pass
        indices_ba = [i for i, x in enumerate(enc_text_list) if x == "e"]
        for i in indices_ba:
            try:
                z_2[i] = "ba"
            except:
                pass 
        indices_bc = [i for i, x in enumerate(enc_text_list) if x == "r"]
        for i in indices_bc:
            try:
                z_2[i] = "bc"
            except:
                pass
        indices_bd = [i for i, x in enumerate(enc_text_list) if x == "g"]
        for i in indices_bd:
            try:
                z_2[i] = "bd"
            except:
                pass
        indices_ca = [i for i, x in enumerate(enc_text_list) if x == "t"]
        for i in indices_ca:
            try:
                z_2[i] = "ca"
            except:
                pass
        indices_cb = [i for i, x in enumerate(enc_text_list) if x == "%"]
        for i in indices_cb:
            try:
                z_2[i] = "cb"
            except:
                pass
        indices_cd = [i for i, x in enumerate(enc_text_list) if x == "&"]
        for i in indices_cd:
            try:
                z_2[i] = "cd"
            except:
                pass
        indices_aa = [i for i, x in enumerate(enc_text_list) if x == "@"]
        for i in indices_aa:
            try:
                z_2[i] = "aa"
            except:
                pass
        indices_bb = [i for i, x in enumerate(enc_text_list) if x == "#"]
        for i in indices_bb:
            try:
                z_2[i] = "bb"
            except:
                pass
        indices_cc = [i for i, x in enumerate(enc_text_list) if x == "o"]
        for i in indices_cc:
            try:
                z_2[i] = "cc"
            except:
                pass
        indices_dc = [i for i, x in enumerate(enc_text_list) if x == "j"]
        for i in indices_dc:
            try:
                z_2[i] = "dc"
            except:
                pass
        indices_db = [i for i, x in enumerate(enc_text_list) if x == "k"]
