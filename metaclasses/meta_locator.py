class MetaLocator(type):

    def __new__(cls, name, bases, attrs):
        # перебираем все атрибуты, переденные в класс
        for key, value in attrs.items():

            if isinstance(value, str):

                if value.startswith("//") or value.startswith(".//") or value.startswith("(//"):
                    # преобразуем строку в локатор, если она начинается с '//' XPath
                    attrs[key] = ("xpath", value)

                elif value.startswith(".") or value.startswith("#"):
                    # преобразуем строку в локатор, если она начинается с '.' или '#' CSS Selector
                    attrs[key] = ("css selector", value)

                return type.__new__(cls, name, bases, attrs)

