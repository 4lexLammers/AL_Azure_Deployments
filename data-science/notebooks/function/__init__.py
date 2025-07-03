import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function App v1 - HTTP Trigger
    Returns a simple JSON response with test data
    """
    logging.info("Python HTTP trigger function processed a request.")

    try:
        # Get optional parameters from query string or request body
        name = req.params.get("name")
        if not name:
            try:
                req_body = req.get_json()
            except ValueError:
                req_body = None
            else:
                if req_body:
                    name = req_body.get("name")

        # Create simple test data instead of using pandas
        test_data = [
            {"id": 1, "value": 42.5, "category": "A"},
            {"id": 2, "value": 38.2, "category": "B"},
            {"id": 3, "value": 45.8, "category": "C"},
            {"id": 4, "value": 33.1, "category": "A"},
            {"id": 5, "value": 51.3, "category": "B"},
        ]

        # Prepare response
        if name:
            response_data = {
                "message": f"Hello {name}! Here's your test data:",
                "data": test_data,
                "rows": len(test_data),
                "status": "success",
            }
        else:
            response_data = {
                "message": "Function executed successfully!",
                "data": test_data,
                "rows": len(test_data),
                "status": "success",
            }

        logging.info(f"Successfully generated response with {len(test_data)} rows")

        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
        )

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        error_response = {
            "error": "Internal server error",
            "message": f"Failed to process request: {str(e)}",
        }
        return func.HttpResponse(
            json.dumps(error_response),
            status_code=500,
            headers={"Content-Type": "application/json"},
        )
