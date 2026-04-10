from src.core import celtic_cross

spread = celtic_cross()

for position, card in spread.items():
    print(f"\n{position}")
    print("Lá bài:", card["name"])
    print("Chiều:", card["orientation"])
    print("Ý nghĩa:", card["meaning"])