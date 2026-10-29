def format_error(message, status=400):
    return {"error": message}, status
