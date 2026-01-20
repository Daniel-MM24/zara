from semantic_analyzer import SemanticAnalyzer

def test_zara_semantics():
    # Scenario 1: Scope Violation
    print("\nScenario 1: Testing Scopes")
    sa = SemanticAnalyzer()
    sa.st.enter_scope()
    sa.check_declaration("integer", "local_var", "integer")
    sa.st.exit_scope()
    sa.check_assignment("local_var", "integer") # Should fail
    sa.validate()

    # Scenario 2: Array vs Stack Consistency
    print("\nScenario 2: Testing Collections")
    sa = SemanticAnalyzer()
    sa.check_declaration("array", "my_list")
    sa.check_collection_usage("my_list", "length") # Correct
    sa.check_collection_usage("my_list", "push")   # Should fail
    sa.validate()

if __name__ == "__main__":
    test_zara_semantics()