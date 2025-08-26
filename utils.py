import ast
import re

def clean_code(raw_code: str) -> str:
    """Remove markdown fences and leading comments."""
    # Remove ```python or ``` fences
    code = re.sub(r"```[a-zA-Z]*", "", raw_code)
    code = code.replace("```", "")

    # Remove lines starting with #
    lines = code.splitlines()
    cleaned = [line for line in lines if not line.strip().startswith("#")]
    return "\n".join(cleaned).strip()

def has_function_def(code: str, func_name="calculate_auc") -> bool:
    """Check if function exists in code using AST."""
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                return True
    except SyntaxError:
        return False
    return False