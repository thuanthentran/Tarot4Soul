from src.core import draw_three

spread = draw_three()

for position, card in spread.items():
    print(f"\n{position}")
    print("Lá bài:", card["name"])
    print("Chiều:", card["orientation"])
    print("Ý nghĩa:", card["meaning"])
