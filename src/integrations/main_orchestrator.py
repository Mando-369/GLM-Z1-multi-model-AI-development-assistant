import ollama
from chromadb import Client
from .hrm_integration import HRMOrchestrator


class UnifiedCodingAssistant:
    def __init__(self):
        # HRM for hierarchical reasoning
        self.hrm = HRMOrchestrator()

        # Your existing models via Ollama
        self.glm_z1 = "JollyLlama/GLM-Z1-32B-0414-Q4_K_M:latest"
        self.codellama = "codellama:latest"
        self.deepseek = "deepseek-coder:latest"

        # Knowledge base
        self.chromadb = Client()
        self.faust_collection = self.chromadb.get_collection("faust_docs")
        self.juce_collection = self.chromadb.get_collection("juce_docs")

    async def process_request(self, user_request):
        # Step 1: Analyze with Claude Code agent
        analysis = await self.analyze_requirements(user_request)

        # Step 2: HRM hierarchical planning
        plan = self.hrm.decompose_task(analysis)

        # Step 3: Route to specialized models
        results = await self.execute_plan(plan)

        # Step 4: Validate and test
        validated = await self.validate_results(results)

        return validated

    async def execute_plan(self, plan):
        results = []
        for subtask in plan.subtasks:
            if subtask.requires_deep_reasoning:
                # Use GLM-Z1 for rumination
                result = ollama.generate(model=self.glm_z1, prompt=subtask.prompt)
            elif subtask.is_faust_code:
                # Use CodeLlama with FAUST context
                context = self.faust_collection.query(subtask.query)
                result = ollama.generate(
                    model=self.codellama, prompt=f"{context}\n{subtask.prompt}"
                )
            else:
                # Use DeepSeek for general coding
                result = ollama.generate(model=self.deepseek, prompt=subtask.prompt)
            results.append(result)
        return results
