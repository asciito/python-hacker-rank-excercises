import sys
import io

class PrintContext:

    def __init__(self) -> None:
        self.old_output, sys.stdout = sys.stdout, io.StringIO()

    def getValue(self) -> str:
        return sys.stdout.getvalue().strip('\n')  
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.stdout = self.old_output

