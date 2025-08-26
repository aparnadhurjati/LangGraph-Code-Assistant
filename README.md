# LangGraph-Code-Assistant

A Python project demonstrating automated code generation, testing, and documentation using LangGraph agents and OpenAI's GPT models.

## 🚀 Overview

This project implements a multi-agent system that:
1. **Generates Python code** based on problem descriptions
2. **Creates comprehensive test cases** for the generated code
3. **Tests the code** against the generated test cases
4. **Generates documentation** for successful implementations
5. **Retries with improvements** if tests fail

## 🏗️ Architecture

The system uses LangGraph to orchestrate four specialized agents:

- **CoderAgent**: Generates Python functions using OpenAI GPT
- **TestGeneratorAgent**: Creates meaningful unit tests
- **TesterAgent**: Executes tests and validates code
- **DocAgent**: Generates markdown documentation

## 📁 Project Structure

```
LangGraph-Code-Assistant/
├── code_assistant_agents.py    # Agent implementations and workflow logic
├── run_agents.py              # Main execution script and graph definition
├── utils.py                   # Utility functions (code cleaning, AST parsing)
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore patterns
├── output/                   # Generated code files (auto-created)
├── documentation/            # Generated documentation (auto-created)
└── README.md                # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- OpenAI API key

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/aparnadhurjati/LangGraph-Code-Assistant.git
   cd LangGraph-Code-Assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

3. **Create required directories**
   ```bash
   mkdir -p output documentation
   ```

## 🚀 Usage

### Basic Usage
```python
from run_agents import graph

# Define your problem
problem_state = {
    "problem": "Implement a recursive Fibonacci function that returns the nth Fibonacci number.",
    "func_name": "fibonacci"
}

# Run the workflow
final_output = graph.invoke({
    "problem": problem_state["problem"], 
    "func_name": problem_state["func_name"]
})
print(final_output)
```

### Example Problems

The system works well with various types of problems:

#### Classification Functions
```python
problem_state = {
    "problem": "Implement a function calculate_f1_score(y_true, y_pred) that returns the F1 score.",
    "func_name": "calculate_f1_score"
}
```

**⚠️ Note**: Classification functions (like ROC AUC, F1 score) require additional robustness upgrades:
- Enhanced test validation to ensure diverse class distributions
- Better error handling for edge cases (single class, invalid probabilities)
- Improved test generation prompts for meaningful classification scenarios
- Fallback test data when LLM-generated tests are insufficient

#### Mathematical Functions
```python
problem_state = {
    "problem": "Implement a recursive Fibonacci function that returns the nth Fibonacci number.",
    "func_name": "fibonacci"
}
```

#### Array/List Functions
```python
problem_state = {
    "problem": "Implement a function merge_sorted_arrays(arr1, arr2) that merges two sorted arrays.",
    "func_name": "merge_sorted_arrays"
}
```

## 🔧 Configuration

### Model Settings
- **Model**: `gpt-4o-mini` (configurable in `code_assistant_agents.py`)
- **Temperature**: 0.2 (low randomness for consistent code generation)
- **Max Retries**: 5 (configurable in `run_agents.py`)

### Output Directories
- **Generated Code**: `output/` directory
- **Documentation**: `documentation/` directory
- **Temporary Files**: Automatically cleaned up after execution

## 🔄 Workflow

1. **Code Generation**: `CoderAgent` creates Python functions based on problem descriptions
2. **Test Creation**: `TestGeneratorAgent` generates comprehensive test cases
3. **Code Testing**: `TesterAgent` executes tests and validates functionality
4. **Documentation**: `DocAgent` creates markdown documentation for successful code
5. **Retry Logic**: If tests fail, the system retries with improvements (up to 5 times)

## 🧪 Testing Features

### Automatic Test Generation
- Generates 3-5 meaningful test cases
- Ensures test data diversity and edge cases
- Validates test quality automatically

### Test Validation
- AST parsing to verify function existence
- Dynamic code execution in isolated environment
- Comprehensive error reporting and debugging

## 📚 Generated Output

### Code Files
- Generated functions are saved as `.py` files in the `output/` directory
- Files are named after the function (e.g., `calculate_auc.py`)

### Documentation
- Markdown documentation in the `documentation/` directory
- Includes function descriptions, examples, and usage notes

## 🚨 Error Handling

The system includes robust error handling:
- **API Failures**: Graceful fallbacks and retry mechanisms
- **Code Generation Errors**: Automatic retry with improved prompts
- **Test Failures**: Detailed error reporting and debugging information
- **Resource Cleanup**: Automatic cleanup of temporary files

## 🔒 Security Considerations

- **API Keys**: Never commit API keys to version control
- **Code Execution**: Generated code runs in isolated temporary environments
- **Input Validation**: All inputs are validated before processing

## 🚧 Limitations

- **OpenAI API Dependency**: Requires valid API key and internet connection
- **Code Quality**: Generated code quality depends on the LLM model
- **Test Coverage**: Test generation may not cover all edge cases
- **Performance**: LLM calls can be slow and expensive
- **Classification Functions**: Currently limited robustness for binary classification problems
  - May generate tests with insufficient class diversity
  - ROC AUC and similar metrics can fail with single-class data
  - Requires manual validation and fallback test data

## 🛠️ Development

### Adding New Agents
1. Implement the agent function in `code_assistant_agents.py`
2. Add the agent to the workflow in `run_agents.py`
3. Define appropriate edges and conditions

### Customizing Prompts
- Modify prompts in agent functions for different use cases
- Adjust temperature and model parameters for different code styles
- Customize test generation requirements

### Extending Test Validation
- Add new validation functions in `utils.py`
- Implement function-type-specific validation logic
- Enhance error reporting and debugging


## 📄 License

[Add your license information here]



## 🔮 Future Enhancements

- [ ] Support for multiple programming languages
- [ ] Integration with code quality tools (flake8, mypy)
- [ ] Web interface for problem submission
- [ ] Batch processing of multiple problems
- [ ] Integration with version control systems
- [ ] Performance benchmarking and optimization
- [ ] Support for different LLM providers

---

**Note**: This is a demonstration project. Generated code should be reviewed and tested before use in production environments.

---

**Repository**: [https://github.com/aparnadhurjati/LangGraph-Code-Assistant](https://github.com/aparnadhurjati/LangGraph-Code-Assistant)
