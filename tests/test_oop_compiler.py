from zara_oop_table import OOPSymbolTable
from zara_oop_compiler import ZaraOOPCompiler

def test_zara_oop():
    table = OOPSymbolTable()
    
    # Define Class Hierarchy
    table.define_class("Robot")
    table.add_method("Robot", "move", ["dist"])
    
    table.define_class("Drone", parent="Robot")
    table.add_method("Drone", "fly", ["alt"])

    compiler = ZaraOOPCompiler(table)

    print("\n--- Compiling: Drone d = new Drone(); d.move(10); ---")
    # Simulation of Object Creation
    compiler.compile_constructor("d", "Drone")
    
    # Simulation of Inherited Method Call
    # 'move' is not in Drone, but is in Robot.
    compiler.compile_method_call("d", "Drone", "move", ["10"])
    
    # Simulation of Class-Specific Method Call
    compiler.compile_method_call("d", "Drone", "fly", ["50"])
    
    compiler.log_ir()

if __name__ == "__main__":
    test_zara_oop()