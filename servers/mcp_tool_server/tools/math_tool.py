from typing import Any, Dict, Union

class MathTool:
    """
    MCP Tool: Math operations
    - Supports: add, subtract, multiply, divide, power
    """

    name = "math_tool"
    description = "Perform basic math operations (add, subtract, multiply, divide, power)."

    @staticmethod
    def run(params: Dict[str, Any]) -> Dict[str, Union[str, float]]:
        """
        Execute a math operation.
        :param params: dict with keys {operation, a, b}
        :return: dict with result or error
        """
        try:
            operation = params.get("operation")
            a = params.get("a")
            b = params.get("b")

            if operation not in ["add", "subtract", "multiply", "divide", "power"]:
                return {"error": f"Unsupported operation: {operation}"}

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                return {"error": "Parameters 'a' and 'b' must be numbers."}

            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return {"error": "Division by zero."}
                result = a / b
            elif operation == "power":
                result = a ** b

            return {
                "operation": operation,
                "a": a,
                "b": b,
                "result": result
            }

        except Exception as e:
            return {"error": str(e)}
