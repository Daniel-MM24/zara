from symbol_table import SymbolTable

def run_test():
    st = SymbolTable()

    print("--- Simulating Zara Program ---")
    # integer x = 10;
    st.add("x", "integer")
    
    # float y = 3.14;
    st.add("y", "float")

    # stack my_stack;
    st.add("my_stack", "stack")

    # function calculate() {
    st.enter_scope()
    st.add("calculate", "function", kind="func")
    
    #   string msg = "hello";
    st.add("msg", "string")
    
    #   array numbers;
    st.add("numbers", "array")

    # Verify lookups
    st.log()
    print(f"Finding 'x' from inside function: {st.lookup('x')}")
    print(f"Finding 'msg' from inside function: {st.lookup('msg')}")

    st.exit_scope()
    # }

    # Verify scope safety
    print(f"Finding 'msg' after function ends: {st.lookup('msg')}")
    st.log()

if __name__ == "__main__":
    run_test()