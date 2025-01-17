from cffi import FFI

class Adder_DLL:
    def __init__(self, dll_path: str, header_path: str) -> None:
        self.ffi_instance = FFI()

            # Read the contents of the header file
        with open(header_path) as header_file:
            without_preprocessor = [line for line in header_file if not line.strip().startswith("#")]
            header_content = "".join(without_preprocessor)

        # Use the content of the header file for cdef
        self.ffi_instance.cdef(header_content)

        # Load the DLL
        self.lib_dll =  self.ffi_instance.dlopen(dll_path,flags=0)

    def execute_addition(self, summandA: int, summandB: int):

        # Call the function
        result = self.lib_dll.add_nums(summandA, summandB)

        return result
    
if __name__ == '__main__':

    dll_path = "build\\lib_adder.dll"
    header_path = "build\\lib_adder.h"

    adder_lib = Adder_DLL(dll_path, header_path)
    
    result = adder_lib.execute_addition(10, 4)

    print(result)