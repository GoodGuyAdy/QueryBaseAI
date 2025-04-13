def serializer_errors(errors):
    """
    Flattens DRF serializer.errors into a list of error strings
    """
    flat_errors = []

    if isinstance(errors, dict):
        for field, messages in errors.items():
            if isinstance(messages, list):
                for msg in messages:
                    if field == "non_field_errors":
                        flat_errors.append(str(msg))
                    else:
                        flat_errors.append(f"{field}: {msg}")
            else:
                if field == "non_field_errors":
                    flat_errors.append(str(messages))
                else:
                    flat_errors.append(f"{field}: {messages}")
    else:
        flat_errors.append(str(errors))

    return flat_errors
