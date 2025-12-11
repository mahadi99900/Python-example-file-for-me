user_data = input("enter your text: ").lower()

def man():
    return {
        "a":"chacs",
        "b":"vcja8w",
        "c":"jwjca",
        "d":"hchsb",
        "e":"73bcba",
        "f":"54kcnaj",
        "g":"bah64b",
        "i":"@72bwg",
        "j":"yeva",
        "k":"bwjx0",
        "l":"17bcha",
        "m":"hwvca",
        "n":"6136bsh",
        "o":"gwvxh",
        "p":"chsbd5",
        "q":"anfi0",
        "r":"amcjs",
        "s":"hchss",
        "t":"chshx32",
        "u":"aadsh6",
        "v":"wjxh23",
        "w":"dhwhw193",
        "x":"ychs9ae",
        "y":"qbdjxu3",
        "z":"wgstw3"
    }

def encrypt():
    data = man()
    result = ""
    for ch in user_data:
        if ch in data:
            result += data[ch]
        else:
            result += ch
    return result

print("Encrypted text: ",end="")
print(encrypt())
    