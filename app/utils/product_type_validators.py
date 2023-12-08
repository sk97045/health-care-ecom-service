class ProductTypesCustomValidtors:
    @staticmethod
    def check_price(price : float | None):
        assert price > 0, f'price {price} should be greater than 0.'
        return price

    @staticmethod
    def check_units(unit_count : int | None):
        assert unit_count > 0 and unit_count % 1 == 0, f'unit_count {unit_count} should be greater than equal to 0 and whole number.'
        return unit_count
