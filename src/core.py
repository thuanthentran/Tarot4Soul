from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Literal, TypedDict

Orientation = Literal["Xuôi", "Ngược"]


class CardResult(TypedDict):
    name: str
    orientation: Orientation
    meaning: str


@dataclass(frozen=True)
class CardDefinition:
    name: str
    upright_meaning: str
    reversed_meaning: str


MINOR_SUIT_LABELS = {
    "Wands": "Gậy",
    "Cups": "Cốc",
    "Swords": "Kiếm",
    "Pentacles": "Tiền",
}


MINOR_SUIT_THEMES = {
    "Wands": "động lực, sáng tạo và hành động",
    "Cups": "cảm xúc, quan hệ và trực giác",
    "Swords": "tư duy, quyết định và sự thật",
    "Pentacles": "vật chất, công việc và sự ổn định",
}


MINOR_RANK_THEMES = {
    "Ace": "một khởi đầu mạnh mẽ",
    "Two": "một lựa chọn hoặc sự cân bằng",
    "Three": "sự mở rộng và hợp tác",
    "Four": "nền tảng, cấu trúc và sự ổn định",
    "Five": "xung đột, thử thách hoặc thay đổi",
    "Six": "sự hỗ trợ, tiến triển và chữa lành",
    "Seven": "kiên trì, đánh giá lại và thử thách nội tâm",
    "Eight": "tiến bước, kỷ luật và nhịp độ",
    "Nine": "sự hoàn thiện gần kề và bài học cá nhân",
    "Ten": "một giai đoạn đạt đỉnh hoặc khép lại",
    "Page": "tin tức mới, học hỏi và tò mò",
    "Knight": "hành động nhanh và đà tiến mạnh",
    "Queen": "sự chín chắn, nuôi dưỡng và hiểu biết",
    "King": "quyền chủ động, trách nhiệm và tầm nhìn",
}


MAJOR_ARCANA = {
    "The Fool": CardDefinition(
        name="The Fool",
        upright_meaning="Khởi đầu mới, niềm tin và sự tự do khám phá.",
        reversed_meaning="Thiếu chuẩn bị, bốc đồng hoặc sợ bước ra khỏi vùng an toàn.",
    ),
    "The Magician": CardDefinition(
        name="The Magician",
        upright_meaning="Biến ý tưởng thành hành động và tận dụng nguồn lực sẵn có.",
        reversed_meaning="Lạm dụng kỹ năng, phân tán năng lượng hoặc tự nghi ngờ.",
    ),
    "The High Priestess": CardDefinition(
        name="The High Priestess",
        upright_meaning="Trực giác mạnh và những điều cần lắng nghe bên trong.",
        reversed_meaning="Bỏ qua trực giác, thông tin bị che giấu hoặc quá thụ động.",
    ),
    "The Empress": CardDefinition(
        name="The Empress",
        upright_meaning="Sự nuôi dưỡng, sáng tạo và cảm giác đủ đầy.",
        reversed_meaning="Cạn kiệt năng lượng, phụ thuộc cảm xúc hoặc thiếu chăm sóc bản thân.",
    ),
    "The Emperor": CardDefinition(
        name="The Emperor",
        upright_meaning="Kỷ luật, cấu trúc và khả năng dẫn dắt.",
        reversed_meaning="Quá kiểm soát, cứng nhắc hoặc thiếu ranh giới rõ ràng.",
    ),
    "The Hierophant": CardDefinition(
        name="The Hierophant",
        upright_meaning="Học hỏi từ truyền thống, cố vấn và hệ giá trị chung.",
        reversed_meaning="Nghi ngờ khuôn mẫu cũ hoặc muốn tự tìm con đường riêng.",
    ),
    "The Lovers": CardDefinition(
        name="The Lovers",
        upright_meaning="Sự gắn kết, lựa chọn quan trọng và sự hòa hợp giá trị.",
        reversed_meaning="Mâu thuẫn trong lựa chọn, lệch giá trị hoặc thiếu cam kết.",
    ),
    "The Chariot": CardDefinition(
        name="The Chariot",
        upright_meaning="Ý chí tiến lên, tự chủ và chiến thắng qua tập trung.",
        reversed_meaning="Mất kiểm soát, thiếu hướng đi hoặc quá tải vì muốn thắng mọi thứ.",
    ),
    "Strength": CardDefinition(
        name="Strength",
        upright_meaning="Sức mạnh nội tâm, sự kiên nhẫn và lòng trắc ẩn.",
        reversed_meaning="Thiếu tự tin, năng lượng bị nén hoặc phản ứng quá mạnh.",
    ),
    "The Hermit": CardDefinition(
        name="The Hermit",
        upright_meaning="Tạm lùi lại để soi sáng sự thật và tìm câu trả lời bên trong.",
        reversed_meaning="Cô lập quá mức, tránh né kết nối hoặc không dám nghe tiếng nói bên trong.",
    ),
    "Wheel of Fortune": CardDefinition(
        name="Wheel of Fortune",
        upright_meaning="Bước ngoặt, chu kỳ mới và sự thay đổi của vận may.",
        reversed_meaning="Kháng cự thay đổi hoặc mắc kẹt trong một chu kỳ lặp lại.",
    ),
    "Justice": CardDefinition(
        name="Justice",
        upright_meaning="Sự công bằng, cân bằng và hệ quả rõ ràng.",
        reversed_meaning="Thiên lệch, thiếu trung thực hoặc đánh giá chưa khách quan.",
    ),
    "The Hanged Man": CardDefinition(
        name="The Hanged Man",
        upright_meaning="Tạm dừng để đổi góc nhìn và chấp nhận sự hy sinh cần thiết.",
        reversed_meaning="Kẹt lại vì trì hoãn hoặc không chịu buông cách nhìn cũ.",
    ),
    "Death": CardDefinition(
        name="Death",
        upright_meaning="Kết thúc tự nhiên của một giai đoạn để mở đường cho điều mới.",
        reversed_meaning="Chống lại sự chuyển hóa hoặc kéo dài một điều đã hết hạn.",
    ),
    "Temperance": CardDefinition(
        name="Temperance",
        upright_meaning="Điều độ, hòa hợp và phối hợp nhịp nhàng.",
        reversed_meaning="Mất cân bằng, quá tay hoặc thiếu sự tiết chế.",
    ),
    "The Devil": CardDefinition(
        name="The Devil",
        upright_meaning="Ràng buộc, cám dỗ và những thói quen khó buông.",
        reversed_meaning="Bắt đầu thoát khỏi kiểm soát, phụ thuộc hoặc nỗi sợ cũ.",
    ),
    "The Tower": CardDefinition(
        name="The Tower",
        upright_meaning="Sự thật làm sụp đổ cấu trúc cũ để giải phóng điều phù hợp hơn.",
        reversed_meaning="Kháng cự biến động hoặc chỉ né tránh thay đổi tất yếu.",
    ),
    "The Star": CardDefinition(
        name="The Star",
        upright_meaning="Hy vọng, chữa lành và cảm hứng mới.",
        reversed_meaning="Mất niềm tin hoặc khó nhìn thấy tia sáng phía trước.",
    ),
    "The Moon": CardDefinition(
        name="The Moon",
        upright_meaning="Mơ hồ, trực giác và những điều chưa lộ diện hoàn toàn.",
        reversed_meaning="Sự mơ hồ đang tan, nhưng cũng có thể là lo lắng bị phóng đại.",
    ),
    "The Sun": CardDefinition(
        name="The Sun",
        upright_meaning="Rõ ràng, thành tựu và nguồn năng lượng tích cực.",
        reversed_meaning="Niềm vui bị trì hoãn hoặc tự che bớt ánh sáng của mình.",
    ),
    "Judgement": CardDefinition(
        name="Judgement",
        upright_meaning="Thức tỉnh, đánh giá lại và một lời gọi mới.",
        reversed_meaning="Tự phán xét nặng nề hoặc bỏ lỡ cơ hội được làm mới.",
    ),
    "The World": CardDefinition(
        name="The World",
        upright_meaning="Hoàn tất trọn vẹn, tích hợp kinh nghiệm và sẵn sàng sang trang.",
        reversed_meaning="Chưa khép lại hoàn toàn hoặc còn một bước cuối cần hoàn thành.",
    ),
}


MAJOR_ARCANA_ORDER = list(MAJOR_ARCANA.values())
MINOR_RANK_ORDER = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]
MINOR_SUIT_ORDER = ["Wands", "Cups", "Swords", "Pentacles"]


def _build_deck() -> list[CardDefinition]:
    deck = list(MAJOR_ARCANA_ORDER)
    for suit in MINOR_SUIT_ORDER:
        suit_label = MINOR_SUIT_LABELS[suit]
        suit_theme = MINOR_SUIT_THEMES[suit]
        for rank in MINOR_RANK_ORDER:
            rank_theme = MINOR_RANK_THEMES[rank]
            deck.append(
                CardDefinition(
                    name=f"{rank} of {suit}",
                    upright_meaning=f"{rank_theme} của bộ {suit_label} nhấn mạnh {suit_theme}.",
                    reversed_meaning=f"{rank_theme} của bộ {suit_label} đang bị lệch nhịp; cần điều chỉnh {suit_theme}.",
                )
            )
    return deck


def _format_card(card: CardDefinition, orientation: Orientation) -> CardResult:
    meaning = card.upright_meaning if orientation == "Xuôi" else card.reversed_meaning
    return {
        "name": card.name,
        "orientation": orientation,
        "meaning": meaning,
    }


class TarotDeck:
    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.SystemRandom()
        self._cards = _build_deck()

    def draw_card(self) -> CardResult:
        card = self._rng.choice(self._cards)
        orientation: Orientation = self._rng.choice(["Xuôi", "Ngược"])
        return _format_card(card, orientation)

    def draw_spread(self, positions: list[str] | tuple[str, ...]) -> dict[str, CardResult]:
        return {position: self.draw_card() for position in positions}


def draw_single(rng: random.Random | None = None) -> CardResult:
    return TarotDeck(rng).draw_card()


def draw_spread(positions: list[str] | tuple[str, ...], rng: random.Random | None = None) -> dict[str, CardResult]:
    return TarotDeck(rng).draw_spread(positions)


def draw_three(rng: random.Random | None = None) -> dict[str, CardResult]:
    return draw_spread(("Quá khứ", "Hiện tại", "Tương lai"), rng=rng)


def celtic_cross(rng: random.Random | None = None) -> dict[str, CardResult]:
    positions = (
        "1. Hiện tại",
        "2. Thử thách",
        "3. Nền tảng",
        "4. Quá khứ gần",
        "5. Mục tiêu",
        "6. Tương lai gần",
        "7. Bản thân",
        "8. Môi trường",
        "9. Hy vọng / nỗi sợ",
        "10. Kết quả",
    )
    return draw_spread(positions, rng=rng)


__all__ = [
    "CardResult",
    "TarotDeck",
    "celtic_cross",
    "draw_single",
    "draw_spread",
    "draw_three",
]