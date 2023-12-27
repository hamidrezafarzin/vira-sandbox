class Errors:
    def generate_error(msg):
        # return {"detail": msg}
        return msg

    # ===========================================================  User related errors
    INVALID_PHONE_NUMBER_PATTERN = generate_error(
        "Invalid Phone Number pattern (regex)"
    )
    INVALID_OTP_PATTERN = generate_error("Invalid otp code pattern (regex)")
    INVALID_OTP_CODE = generate_error("Invalid otp code")
    OTP_BLANK = generate_error("OTP cant be blank")
    OTP_SPAM = generate_error("Please wait for a while to resend and try again")
    FAILED_TO_SEND_OTP = generate_error("Failed to send otp sms panel Error")
    XSS_ATTACK_DETECTION = generate_error(
        "XSS protection activate, dont use html tags in fields"
    )
    PASSWORD_MISMATCH = generate_error("Passwords does not match")

    USER_ALREADY_EXIST = generate_error("The User Already Registered")
    USER_NOT_FOUND = generate_error("user not found.")

    INVALID_ETHEREUM_PATTERN = generate_error("Invalid ethereum account (regex)")
    INVALID_IBAN_PATTERN = generate_error("Invalid Iban (sheba) (regex)")
