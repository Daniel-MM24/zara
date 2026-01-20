class OOPSymbolTable:
    def __init__(self):
        self.classes = {} # {className: {parent: name, methods: {}, fields: {}}}

    def define_class(self, name, parent=None):
        self.classes[name] = {
            "parent": parent,
            "methods": {},
            "fields": {}
        }
        print(f"Class Defined: {name}" + (f" inheriting from {parent}" if parent else ""))

    def add_method(self, class_name, method_name, params):
        if class_name in self.classes:
            self.classes[class_name]["methods"][method_name] = params
            print(f"  Method Added: {class_name}.{method_name}")

    def resolve_method(self, class_name, method_name):
        """Checks current class and parent for method (Inheritance)"""
        current = class_name
        while current:
            if method_name in self.classes[current]["methods"]:
                return current
            current = self.classes[current]["parent"]
        return None