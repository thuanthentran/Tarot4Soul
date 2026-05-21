# Tarot4Soul

Tarot4Soul là một bộ script Python đơn giản để rút và in kết quả bài tarot ra terminal. Repository hiện có 3 entrypoint tương ứng với 3 kiểu trải bài:

- Rút 1 lá
- Rút 3 lá
- Celtic Cross

## Yêu cầu

- Python 3.10+.
- Module `src.core` phải tồn tại và cung cấp các hàm `draw_single()`, `draw_three()` và `celtic_cross()`.


## Cách chạy

Chạy trực tiếp từng script bằng Python:

```bash
python drawsingle.py
python drawthree.py
python drawcelticcross.py
```

## Dùng như thư viện

Sau khi cài ở chế độ phát triển, bạn có thể import trực tiếp API rút bài:

```bash
pip install -e .
```

```python
from src.core import TarotDeck, draw_single, draw_three, celtic_cross

card = draw_single()
spread = draw_three()
cross = celtic_cross()

deck = TarotDeck()
custom_spread = deck.draw_spread(["Vấn đề", "Lời khuyên", "Kết quả"])
```

## Kết quả in ra

### `drawsingle.py`

Script này rút một lá và in ra:

- Tên lá bài
- Chiều lá bài
- Ý nghĩa

### `drawthree.py`

Script này rút 3 lá và in ra kết quả theo từng vị trí, mỗi vị trí gồm:

- Tên lá bài
- Chiều lá bài
- Ý nghĩa

### `drawcelticcross.py`

Script này rút trải bài Celtic Cross và in kết quả theo từng vị trí, mỗi vị trí gồm:

- Tên lá bài
- Chiều lá bài
- Ý nghĩa

## Cấu trúc hiện tại

```text
.
├── drawsingle.py
├── drawthree.py
├── drawcelticcross.py
└── .gitignore
```

## Ghi chú

Nếu bạn muốn mở rộng repo sau này, có thể tách logic rút bài vào `src/core.py` và giữ các file ở root làm entrypoint chạy nhanh từ terminal.