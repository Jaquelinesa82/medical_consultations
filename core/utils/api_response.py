def success_response(data, status=200):
    return {
        "success": True,
        "data": data,
        "status": status
    }


def error_response(errors, status=400):
    return {
        "success": False,
        "errors": errors,
        "status": status
    }