suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = [(rank, suit) for suit in suits for rank in ranks]
total_cards = len(deck)

red_cards = [card for card in deck if card[1] in ["hearts", "diamonds"]]
p_red = len(red_cards) / total_cards

heart_cards = [card for card in red_cards if card[1] == "hearts"]
p_heart_given_red = len(heart_cards) / len(red_cards)

face_cards = [card for card in deck if card[0] in ['Jack', 'Queen', 'King']]
diamond_faces = [card for card in face_cards if card[1] == "diamonds"]
p_diamond_given_face = len(diamond_faces) / len(face_cards)

spade_faces = [card for card in face_cards if card[1] == "spades"]
queens = [card for card in face_cards if card[0] == "Queen"]
spade_or_queen = set(spade_faces + queens)
p_spade_or_queen_given_face = len(spade_or_queen) / len(face_cards)

print(f"Probability of drawing a red card: {p_red:.2f}")
print(f"Probability of heart given red card: {p_heart_given_red:.2f}")
print(f"Probability of diamond given face card: {p_diamond_given_face:.2f}")
print(f"Probability of spade or queen given face card: {p_spade_or_queen_given_face:.2f}")
