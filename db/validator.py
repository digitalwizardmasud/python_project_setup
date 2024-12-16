class Validator:
    def __init__(self, schema):
        self.schema = schema

    def validate(self, data):
        errors = []
        for field, constraints in self.schema.items():
            field_type = constraints.get('type')
            required = constraints.get('required')
            enum_values = constraints.get('enum')

            if field in data:
                if not isinstance(data[field], field_type):
                    errors.append(f"Field '{field}' must be of type {field_type.__name__}.")
                if enum_values and data[field] not in enum_values:
                    errors.append(f"Field '{field}' must be one of {enum_values}.")
            elif required:
                errors.append(f"Field '{field}' is required.")
        for field in data:
            if field not in self.schema:
                errors.append(f"Unexpected field '{field}' in data.")
        return errors