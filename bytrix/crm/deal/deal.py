from bytrix.commons import UserField
from bytrix.helpers import BitrixApiMixin, bitrix_method

class Deal(BitrixApiMixin):
    def __init__(self, url):
        super().__init__(url)
        self.userfield = UserField(url, __package__)

    @bitrix_method
    def add(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def delete(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def fields(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def get(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def list(self, method, **params):
        return self.call_method(method, params)

    @bitrix_method
    def update(self, method, **params):
        return self.call_method(method, params)


