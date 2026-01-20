class ZaraErrorReporter:
    def __init__(self):
        self.errors = []

    def report(self, phase, message, line=None):
        error_msg = f"[{phase} ERROR] {message}"
        if line: error_msg += f" (Line {line})"
        self.errors.append(error_msg)
        print(f"❌ {error_msg}")

    def has_errors(self):
        return len(self.errors) > 0

    def summary(self):
        print(f"\n--- Compilation Finished: {len(self.errors)} errors found ---")