from django.core.validators import RegexValidator

name_validator = RegexValidator(
    regex=r"^[A-Za-z][A-Za-z'’\-]{1,49}$",
    message='Name must start with a letter and contain letters, apostrophes, or hyphens. '
            'Length must be between 2 to 50 characters.',
)

nickname_validator = RegexValidator(
    regex=r"^[A-Za-z0-9_’\-]{3,50}$",
    message="Nickname must be between 3 and 50 characters long and can include letters, numbers, underscores, "
            "and hyphens."
)

phone_number_validator = RegexValidator(
    regex=r'^\+?\d{9,12}$',
    message='Phone number must be between 9 and 12 digits long, can start with +, and contain only digits.',
)
