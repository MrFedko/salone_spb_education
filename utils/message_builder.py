class MessageBuilder:
    def __init__(self):
        self.names = {
            "info": "Информация",
            "ingredients": "Ингредиенты",
            "method": "Метод приготовления",
            "glass": "Посуда",
            "file_link": "Ссылка на файл",
            "description": "Описание",
            "extra_info": "Дополнительная информация",
            "vintage": "Год выпуска",
            "country": "Страна",
            "includes": "Состав",
            "price": "Цена",
            "about": "Описание",
            "taste": "Вкус",
        }
        self.EXCLUDED_KEYS = {"name", "id", "photo_link"}

    def message_return(self, sheet_name: str):
        types_messages = {
            "cocktails": self.cocktails_message,
            "info": self.info_message,
            "cuisine": self.cuisine_message,
            "salumeria": self.salumeria_message,
            "wine": self.wine_message,
        }
        return types_messages[sheet_name]

    def cocktails_message(self, info: dict) -> str:
        text = f"""<b>{info['name']}</b>\n\n"""
        for key, value in info.items():
            if key not in self.EXCLUDED_KEYS and value:
                text += f"<b>{self.names[key]}:</b>\n{value}\n\n"
        return text

    def info_message(self, info: dict) -> str:
        text = f"""<b>{info['name']}</b>\n\n"""
        for key, value in info.items():
            if key not in self.EXCLUDED_KEYS and value:
                if key == "file_link":
                    text += f"<b>{self.names[key]}:</b>\n<a href='{value}'>Скачать файл</a>\n\n"
                else:
                    text += f"<b>{self.names[key]}:</b>\n{value}\n\n"
        return text

    def cuisine_message(self, info: dict) -> str:
        text = f"""<b>{info['name']}</b>\n\n"""
        for key, value in info.items():
            if key not in self.EXCLUDED_KEYS and value:
                text += f"<b>{self.names[key]}:</b>\n{value}\n\n"
        return text

    def salumeria_message(self, info: dict) -> str:
        text = f"""<b>{info['name']}</b>\n\n"""
        for key, value in info.items():
            if key not in self.EXCLUDED_KEYS and value:
                text += f"<b>{self.names[key]}:</b>\n{value}\n\n"
        return text

    def wine_message(self, info: dict) -> str:
        text = f"""<b>{info['name']}</b>\n\n"""
        for key, value in info.items():
            if key not in self.EXCLUDED_KEYS and value:
                text += f"<b>{self.names[key]}:</b>\n{value}\n\n"
        return text
