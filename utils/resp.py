def success(message, data=None, routes=[]):
    return {
        "status" : "success",
        "message" : message,
        "data" : data,
        "routes": routes
    }

def error(message, error_code=None, error_details=None, routes=[]):
    return {
        "status" : "error",
        "message" : message,
        "error" : {
            "code" : error_code,
            "details": error_details
        },
        "routes": routes
    }

