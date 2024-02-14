def check_intent(text):
    if 'buy' in text.lower() and 'sell' in text.lower():
        return 'both buying and selling'
    elif 'buy' in text.lower():
        return 'buying'
    elif 'sell' in text.lower():
        return 'selling'
    else:
        return 'none of them!'


text1 = "I want to buy a new phone and I have some items for sell"
text2 = "I am looking for a laptop to buy"
text3 = "I have some furniture for sale"
text4 = "I want to sell my car"

intent1 = check_intent(text1)
intent2 = check_intent(text2)
intent3 = check_intent(text3)
intent4 = check_intent(text4)

print("Intent 1:", intent1)
print("Intent 2:", intent2)
print("Intent 3:", intent3)  
print("Intent 4:", intent4) 
