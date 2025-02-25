class Material:

    def __init__(self, article_number, material_name, stored_at, material_type):
        self.article_number = article_number
        self.material_name = material_name
        self.stored_at = stored_at
        self.material_type = material_type
        self.total_quantity = 0

    def add_material(self, amount):
        self.total_quantity += amount

    def subtract_material(self, amount):
        self.total_quantity -= amount

    def report_material_quantity(self):
        return self.total_quantity

