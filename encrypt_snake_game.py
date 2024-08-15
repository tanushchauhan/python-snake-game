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