class Pizza:
    empty_list = []

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.init_list = []

    def __repr__(self):
        return f"Pizza({self.ingredients!r})"

    def __str__(self):
        return self.empty_list.append(self.ingredients)

    def update_init_collections(self):
        self.init_list.append(self.ingredients)
        return self.init_list

    @classmethod
    def update_cls_collections(cls, ingredients):
        cls.empty_list.append(ingredients)
        return cls.empty_list

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])


if __name__ == "__main__":
    pizza_instance = Pizza('["salt", "pepper"]')
    pizza_init_instance = pizza_instance.update_init_collections()
    print("Output1 ==>", pizza_init_instance)

    pizza_instance = Pizza('["oranges", "bananas"]')
    pizza_init_instance = pizza_instance.update_init_collections()
    print("Output2 ==>", pizza_init_instance)

    pizza_cls_instance1 = Pizza.update_cls_collections(["salt", "pepper"])
    print("Output3 ==>", pizza_cls_instance1)
    pizza_cls_instance2 = Pizza.update_cls_collections(["oranges", "bananas"])
    print("Output4 ==>", pizza_cls_instance2)
