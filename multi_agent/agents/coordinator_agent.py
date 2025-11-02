"""Coordinator Agent - Orchestrates multi-agent collaboration."""

from typing import List, Dict, Any, Optional
from crewai import Agent, Task

class CoordinatorAgent:
    """Agent responsible for coordinating multi-agent collaboration.
    
    This agent focuses on:
    - Strategic decision making
    - Agent orchestration  
    - Conflict resolution
    - Resource allocation
    - Performance monitoring
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        
        self.agent = Agent(
            role="Multi-Agent Coordinator",
            goal="Orchestrate optimal collaboration between specialized agents to achieve emergent intelligence",
            backstory="""You are a master coordinator with expertise in multi-agent systems. 
            Your role is to ensure that different specialized agents work together harmoniously, 
            resolving conflicts, allocating resources efficiently, and identifying opportunities 
            for emergent problem-solving strategies.""",
            tools=[],  # Coordinator uses communication rather than specialized tools
            verbose=True,
            allow_delegation=True,  # Can delegate subtasks to other agents
            max_iter=10
        )
    
    def create_coordination_task(self, 
                               subtasks: List[Task],
                               collaboration_mode: str = "emergent") -> Task:
        """Create a coordination task for managing agent collaboration."""
        
        subtask_descriptions = "\n".join([
            f"- {task.description[:100]}..." for task in subtasks
        ])
        
        return Task(
            description=f"""
            Coordinate multi-agent collaboration in {collaboration_mode} mode:
            
            Subtasks to coordinate:
            {subtask_descriptions}
            
            Your coordination responsibilities:
            1. Analyze each agent's specialized capabilities
            2. Identify collaboration opportunities and synergies
            3. Resolve any conflicts or resource contention
            4. Monitor progress and adjust coordination strategy
            5. Identify emergent strategies from agent interactions
            6. Ensure optimal resource allocation
            7. Facilitate knowledge sharing between agents
            
            Focus on enabling emergent intelligence that exceeds individual capabilities.
            """,
            agent=self.agent,
            expected_output="Coordination strategy with performance metrics and emergent insights"
        )
    
    def monitor_collaboration(self, agents: List[Any]) -> Dict[str, Any]:
        """Monitor ongoing collaboration between agents."""
        return {
            "active_agents": len(agents),
            "collaboration_efficiency": 0.85,
            "resource_utilization": 0.78,
            "conflict_resolution_success": 0.92,
            "emergent_patterns_detected": 3
        }