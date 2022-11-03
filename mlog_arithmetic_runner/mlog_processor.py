

class MlogProcessor:
    def __init__(self):
        self.ipt = 2
        self.tick = 0
        self.instructions_executed = 0
        self.current_line = 0
        self.code = []
        self.constants = {
            "true": 1,
            "false": 0,
            "null": None
        }
        self.lambda_variables = {
            "@tick": lambda : self.tick,
            "@time": lambda : self.tick / 60.0,
            "@counter": lambda : self.current_line + 1,
            "@ipt": lambda : self.ipt
        }
        self.variables = {}

    def assemble_code(self, mlog_code: str):
        self.code = mlog_code.splitlines()

    def reset(self):
        self.tick = 0
        self.current_line = 0
        self.instructions_executed = 0
        self.variables = {}

    def get_variable(self, name: str):
        if name.startswith("@"):
            return self.lambda_variables.get(name, lambda : None)()
        if name in self.constants:
            return self.constants[name]
        if name in self.variables:
            return self.variables[name]
        return None

    def set_variable(self, name: str, value):
        self.variables[name] = value