class Grayscale:
    def __init__(self, value=0):
        self._value = 0
        self.from_int(value)

    def from_int(self, new_value):
        """
        :param int new_value: Integer between 0 and 255
        :return:
        """
        assert isinstance(new_value, int) and 0 <= new_value <= 255

        self._value = new_value

    def from_rgb(self, new_value):
        """
        :param RGB new_value: RGB instance
        :return:
        """
        assert isinstance(new_value, RGB)

        self._value = new_value.avg()

    def from_fraction(self, new_value):
        """
        :param float new_value: Float between 0 and 1
        :return:
        """
        assert isinstance(new_value, float) and 0.0 <= new_value <= 1.0

        self._value = int(round(new_value * 255))

    def to_int(self):
        """
        :return int: Int between 0 and 255
        """
        return self._value

    def to_fraction(self):
        """
        :return float: Float between 0 and 1
        """
        return self._value / 255

    def to_rgb(self):
        """
        :return RGB: New RGB instance where r, g, b are equal to the grayscale value
        """
        rgb = RGB()
        rgb.from_grayscale(self)
        return rgb

    def add_grayscale(self, other):
        """
        Add other's value to self's
        :param Grayscale other: Grayscale instance
        :return:
        """
        assert isinstance(other, Grayscale)

        self._value = clamp(self._value + other.to_int(), 0, 255)

    def subtract_grayscale(self, other):
        """
        Subtract other's value from self's
        :param Grayscale other: Grayscale instance
        :return:
        """
        assert isinstance(other, Grayscale)

        self._value = clamp(self._value - other.to_int(), 0, 255)

    def __str__(self):
        return "Grayscale ({})".format(self._value)


class RGB:
    def __init__(self, r=0, g=0, b=0):
        self._r = 0
        self._g = 0
        self._b = 0
        self.from_int(r, g, b)

    def from_int(self, new_r, new_g, new_b):
        """
        :param int new_r: Int between 0 and 255
        :param int new_g: Int between 0 and 255
        :param int new_b: Int between 0 and 255
        :return:
        """
        assert isinstance(new_r, int) and 0 <= new_r <= 255
        assert isinstance(new_g, int) and 0 <= new_g <= 255
        assert isinstance(new_b, int) and 0 <= new_b <= 255

        self._r, self._g, self._b = new_r, new_g, new_b

    def from_fractions(self, new_r, new_g, new_b):
        """
        :param float new_r: Float between 0 and 1
        :param float new_g: Float between 0 and 1
        :param float new_b: Float between 0 and 1
        :return:
        """
        assert isinstance(new_r, float) and 0.0 <= new_r <= 1.0
        assert isinstance(new_g, float) and 0.0 <= new_g <= 1.0
        assert isinstance(new_b, float) and 0.0 <= new_b <= 1.0

        self._r = int(round(new_r * 255))
        self._g = int(round(new_g * 255))
        self._b = int(round(new_b * 255))

    def from_grayscale(self, new_value):
        """
        :param Grayscale new_value: Grayscale instance
        :return:
        """
        assert isinstance(new_value, Grayscale)

        self._r = new_value.to_int()
        self._g = new_value.to_int()
        self._b = new_value.to_int()

    def to_grayscale(self):
        """
        :return Grayscale: Grayscale instance where value is equal to the average of r, g, b
        """
        return Grayscale(value=self.avg())

    def avg(self):
        """
        :return int: Average of r, g, b
        """
        return int(round((self._r + self._g + self._b) / 3))

    def __str__(self):
        return "RGB ({}, {}, {})".format(self._r, self._g, self._b)


def clamp(n, lower, upper):
    """
    :param n: Number to clamp
    :param lower: Lower bound
    :param upper: Upper bound
    :return: Clamped number
    """
    return max(lower, min(n, upper))
