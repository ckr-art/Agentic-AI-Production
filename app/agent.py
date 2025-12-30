from app.llm import get_llm
from app.memory import Memory
from app.tools import calculator

class Agent:
    def __init__(self):
        self.llm = get_llm()
        self.memory = Memory()

    def run(self, user_input: str):
        self.memory.add(user_input)

        if "calculate" in user_input.lower():
            expression = user_input.lower().replace("calculate", "")
            tool_result = calculator(expression)
            self.memory.add(tool_result)
            return tool_result

        response = self.llm.generate_content(user_input)
        answer = response.text
        self.memory.add(answer)
        return answer
