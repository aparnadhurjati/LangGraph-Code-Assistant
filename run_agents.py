from code_assistant_agents import coder_agent, test_generator_agent, tester_agent, doc_agent, State
from langgraph.graph import StateGraph, END


MAX_RETRIES = 5

# Langgraph
# Build graph outside of main so its reusable for multiple invocations
workflow = StateGraph(State)

workflow.add_node("CoderAgent", coder_agent)
workflow.add_node("TestGeneratorAgent", test_generator_agent)
workflow.add_node("TesterAgent", tester_agent)
workflow.add_node("DocAgent", doc_agent)

workflow.set_entry_point("CoderAgent")

#Edges
workflow.add_edge("CoderAgent", "TestGeneratorAgent")
workflow.add_edge("TestGeneratorAgent", "TesterAgent")


# --- Conditional edge with retry limit ---
def tester_edge(state):
    # Initialize retry counter if not present
    retries = state.get("retries", 0)
    if state.get("tests_passed") is True:
        return "DocAgent"
    elif retries < MAX_RETRIES:
        state["retries"] = retries + 1
        return "CoderAgent"
    else:
        # Max retries reached → stop the workflow
        state["output"] = (state.get("output", "") + 
                           f" | Max retries ({MAX_RETRIES}) reached.")
        return END

workflow.add_conditional_edges("TesterAgent", tester_edge)
#use below instead of above, if no retry limit is required
# workflow.add_conditional_edges("TesterAgent", lambda state: "DocAgent" if  state.get("tests_passed") is True else "CoderAgent",)

graph = workflow.compile()




#main
if __name__=="__main__":   
    """Sample problems. More to come """
    """
    problem_state = {
        "problem": "Implement a recursive Fibonacci function that returns the nth Fibonacci number.",
        "func_name": "fibonacci"
    }
    problem_state = {
        "problem": "Implement a function calculate_auc(y_true, y_pred) that returns ROC AUC score.",
        "func_name": "calculate_auc"
    }
    problem_state = {
        "problem": "Implement a function gcd(a, b) that returns the greatest common divisor of two integers using Euclidean algorithm.",
        "func_name": "gcd"
    }

    """
    problem_state = {
        "problem": "Implement a function merge_sorted_arrays(arr1, arr2) that merges two sorted arrays into one sorted array.",
        "func_name": "merge_sorted_arrays"
    }    
    final_output = graph.invoke({"problem" : problem_state["problem"], "func_name": problem_state["func_name"]})
    print(final_output)




