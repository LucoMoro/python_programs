def emojis_converter(message):
    words = message.split(' ')

    emojis = {
        ":)" : "hehe",
        ":(" : "sadge"
    }


    output= ""
    for word in words: 
        output  += emojis.get(word, word) + " "
    return output

message = input(">")
emoji_output = emojis_converter(message)
print(emoji_output)