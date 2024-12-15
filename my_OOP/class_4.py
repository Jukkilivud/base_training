from class_2 import Sample
# Базовый класс


class Distance:
    """Определение расстояний"""

    def distance(self, s1: Sample, s2: Sample) -> float:
        pass


# Эвклидово расстояние
class ED(Distance):
    def distance(self, s1: Sample, s2: Sample) -> float:
        return hypot(
            s1.sepal_length - s2.sepal_length,
            s1.sepal_width - s2.sepal_width,
            s1.pental_length - s2.pental_length,
            s1.pental_width - s2.pental_width,
        )


# Манхэттенское расстояние
class MD(Distance):
    def distance(self, s1: Sample, s2: Sample) -> float:
        return sum(
            [
                abs(s1.sepal_length - s2.sepal_length),
                abs(s1.sepal_width - s2.sepal_width),
                abs(s1.pental_length - s2.pental_length),
                abs(s1.pental_width - s2.pental_width),
            ]
        )


# Расстояние Чебышева
class CD(Distance):
    def distance(self, s1: Sample, s2: Sample) -> float:
        return sum(
            [
                abs(s1.sepal_length - s2.sepal_length),
                abs(s1.sepal_width - s2.sepal_width),
                abs(s1.pental_length - s2.pental_length),
                abs(s1.pental_width - s2.pental_width),
            ]
        )


# Расстояние Соренсена
class SD(Distance):
    def distance(self, s1: Sample, s2: Sample) -> float:
        return sum(
            [
                abs(s1.sepal_length - s2.sepal_length),
                abs(s1.sepal_width - s2.sepal_width),
                abs(s1.pental_length - s2.pental_length),
                abs(s1.pental_width - s2.pental_width),
            ]
        ) / sum(
            [
                s1.sepal_length + s2.sepal_length,
                s1.sepal_width + s2.sepal_width,
                s1.pental_length + s2.pental_length,
                s1.pental_width + s2.pental_width,
            ]
        )
