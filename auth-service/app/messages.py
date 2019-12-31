class ValidationMessages(object):
    internal_error = "Internal error. Please try again later"
    data_required = "This field is required"


class LoginValidationMessages(ValidationMessages):
    email_format = "Please input a valid email format"
