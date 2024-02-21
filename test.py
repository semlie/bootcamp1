intent_to_sell_words = [
    "Wts", "For sale", "Selling", "Offer", "Sell", "Available",
    "Clearing out", "Disposing of", "Offloading", "Auctioning",
    "Liquidating", "Putting up for sale", "Unloading", "Offering up", "Letting go"
]

intent_to_buy_words = [
    "Wtb", "Looking for", "Seeking", "Buying", "Wanting", "Purchasing",
    "In search of", "Interested in", "Acquiring", "Needing", "Hunting for",
    "Requesting", "Shopping for", "Hoping to buy", "Wanting to acquire","buy",
    "Looking to buy","purchase"
]

both_intent_words = [
    "Trading", "Bartering", "Exchange", "Swap", "Trade-in", "Deal",
    "Negotiating", "Transaction", "Dealings", "Business", "Commerce",
    "Market", "Exchange", "Offer", "Bid","For sale or buying","Selling or buying"
]

def check_intent(text):
    intent_to_sell = any(word.lower() in text.lower() for word in intent_to_sell_words)
    intent_to_buy = any(word.lower() in text.lower() for word in intent_to_buy_words)
    both_intent = any(word.lower() in text.lower() for word in both_intent_words)

    if both_intent:
        return 'both buying and selling'
    elif intent_to_sell:
        return 'selling'
    elif intent_to_buy:
        return 'buying'
    else:
        return 'none of them!'


def check_matching_errors(data):
    error_count = 0
    for item in data:
        content = item["massage_content"]
        category = item["category"]
        inferred_intent = check_intent(content)
        if (category == "sale" and inferred_intent != "selling") or (category == "buy" and inferred_intent != "buying") or (category == "both" and inferred_intent != "both buying and selling"):
            error_count += 1
    return error_count


text5 = [
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "sale",
        "massage_content": "Wts\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "buy",
        "massage_content": "Looking to buy\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "sale",
        "massage_content": "For sale\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "buy",
        "massage_content": "Interested in purchasing\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "both",
        "massage_content": "For sale or buying\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "sale",
        "massage_content": "Selling\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "buy",
        "massage_content": "Want to purchase\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "both",
        "massage_content": "Selling or buying\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "sale",
        "massage_content": "Available for sale\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    },
    {
        "created_at": "2023-09-12 10:50:56",
        "category": "buy",
        "massage_content": "Seeking to buy\nSamsung Arabic \n\nM54 8/256\nMoq\n\nReady Fze",
        "massage_type": "text",
        "phone_id_new": "663"
    }
]

for item in text5:
    content = item["massage_content"]
    intent = check_intent(content)
    print("Message content:", content)
    print("Intent:", intent)
    print("--------------")

error_count = check_matching_errors(text5)
total_items = len(text5)
print("Total items:", total_items)
print("Matching errors:", error_count)
print("Percentage of matching errors: {}%".format(int((error_count / total_items) * 100)))