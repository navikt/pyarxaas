


class SetAttributeType:

    def __init__(self):
        self._intenal_dict = {}


    def __call__(self, field, value):
        self._intenal_dict[field] = value


    def __setitem__(self, key, value):
        self._intenal_dict[key] = value







new_obj = SetAttributeType()

new_obj("age", 1)
new_obj["age"] = "SENSITIVE"