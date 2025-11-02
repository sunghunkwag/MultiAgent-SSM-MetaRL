# MultiAgent-SSM-MetaRL

Multi-Agent Framework for State Space Models with Meta-Reinforcement Learning

## Overview
This repository provides a modular multi-agent framework that integrates:
- State Space Models (SSM) for sequence modeling
- Model-Agnostic Meta-Learning (MAML) for rapid adaptation
- Test-Time Adaptation for online optimization

The system composes specialized agents (Meta-Learning, Adaptation, State Modeling, Environment, Coordinator) to coordinate training, adaptation, and evaluation across reinforcement learning tasks.

## Key Features
- Role-specific agents with clear responsibilities
- Orchestrated collaboration via an agent coordinator
- Pluggable tools interfacing with SSM, MAML, and adaptation modules
- Workflow layer for repeatable multi-agent experiments
- Extensible structure for additional agents and tasks

## Architecture
- Collaboration layer: Coordinator, Meta-Learning, Adaptation, State Modeling, Environment agents
- Core layer: SSM, MAML, Test-Time Adaptation, Environment runner
- Workflow layer: Task composition and execution

## Project Structure
```
MultiAgent-SSM-MetaRL/
├── multi_agent/
│   ├── agents/
│   │   ├── meta_learning_agent.py
│   │   ├── adaptation_agent.py
│   │   ├── state_modeling_agent.py
│   │   ├── environment_agent.py
│   │   └── coordinator_agent.py
│   ├── tools/
│   │   ├── ssm_tool.py
│   │   ├── maml_tool.py
│   │   └── adaptation_tool.py
│   ├── workflows/
│   │   ├── collaborative_learning.py
│   │   └── emergent_optimization.py
│   └── communication/
│       ├── message_broker.py
│       └── shared_memory.py
├── experiments/
│   ├── multi_agent_benchmarks/
│   ├── emergence_analysis/
│   └── performance_comparison/
├── examples/
│   └── getting_started.py
└── docs/
    ├── agent_design_patterns.md
    ├── collaboration_protocols.md
    └── performance_analysis.md
```

## Installation
- Python >= 3.8

```bash
git clone https://github.com/sunghunkwag/MultiAgent-SSM-MetaRL.git
cd MultiAgent-SSM-MetaRL
pip install -e .
pip install crewai langchain torch gymnasium
```

## Quick Start
```python
from multi_agent.workflows import CollaborativeLearning
from multi_agent.agents import (
    MetaLearningAgent,
    AdaptationAgent,
    StateModelingAgent,
    CoordinatorAgent
)

meta = MetaLearningAgent()
adapt = AdaptationAgent()
state = StateModelingAgent()
coord = CoordinatorAgent()

wf = CollaborativeLearning(
    agents=[meta, adapt, state],
    coordinator=coord
)

results = wf.solve_task(
    task="HalfCheetah-v4",
    collaboration_mode="emergent",
    current_performance=0.65,
    target_performance=0.90,
    prediction_horizon=10,
    support_data="sample_support_data",
    query_data="sample_query_data",
    sequence_data="sample_sequence_data",
    environment_data="sample_env_data"
)

print(results)
```

## Agents and Responsibilities
- Meta-Learning Agent: Optimizes initialization and adaptation speed (MAML)
- Adaptation Agent: Performs online updates and test-time optimization
- State Modeling Agent: Models temporal dynamics using SSMs
- Environment Agent: Manages task/environment setup and distribution
- Coordinator Agent: Orchestrates agents, resolves conflicts, allocates resources

## Workflows
- CollaborativeLearning: Creates agent tasks, delegates via CrewAI, aggregates outputs; returns performance metrics and collaboration diagnostics

## Benchmarks and Evaluation
- experiments/multi_agent_benchmarks: multi-agent benchmarks
- experiments/emergence_analysis: analysis utilities
- Metrics: improvement relative to single-agent baselines, stability, sample efficiency
- Note: Any improvement figures in examples are placeholders; run benchmarks to obtain empirical results on target hardware and datasets.

## Development
```bash
pip install -e .[dev]
pytest -q
```

## Roadmap
- Phase 1: Core multi-agent framework (current)
- Phase 2: Collaboration protocols and evaluation suite
- Phase 3: Emergence analysis utilities
- Phase 4: Distributed execution
- Phase 5: Integration with larger AGI research pipelines

## License
MIT License. See LICENSE.

## References
- SSM-MetaRL-TestCompute (base research implementation)
- SSMs for sequence modeling
- Model-Agnostic Meta-Learning (MAML)
- Multi-agent RL
