#!/usr/bin/env python3
"""Getting Started with MultiAgent-SSM-MetaRL

This example demonstrates how to use the multi-agent framework
for collaborative reinforcement learning tasks.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from multi_agent.workflows import CollaborativeLearning
from multi_agent.agents import (
    MetaLearningAgent,
    AdaptationAgent,
    StateModelingAgent,
    CoordinatorAgent
)

def main():
    """Demonstrate basic multi-agent collaboration."""
    
    print("\n🤖 MultiAgent-SSM-MetaRL - Getting Started Example")
    print("="*50)
    
    # Step 1: Initialize specialized agents
    print("\n1. Initializing specialized agents...")
    
    meta_agent = MetaLearningAgent()
    print("   ✅ Meta-Learning Agent ready")
    
    adapt_agent = AdaptationAgent()
    print("   ✅ Adaptation Agent ready")
    
    state_agent = StateModelingAgent()
    print("   ✅ State Modeling Agent ready")
    
    coordinator = CoordinatorAgent()
    print("   ✅ Coordinator Agent ready")
    
    # Step 2: Create collaborative workflow
    print("\n2. Creating collaborative workflow...")
    
    workflow = CollaborativeLearning(
        agents=[meta_agent, adapt_agent, state_agent],
        coordinator=coordinator
    )
    print("   ✅ Collaborative workflow established")
    
    # Step 3: Define a sample task
    print("\n3. Defining sample task...")
    
    task_name = "HalfCheetah-v4"
    task_config = {
        "current_performance": 0.65,
        "target_performance": 0.90,
        "prediction_horizon": 10,
        "support_data": "sample_support_data",
        "query_data": "sample_query_data",
        "sequence_data": "sample_sequence_data",
        "environment_data": "sample_env_data"
    }
    
    print(f"   📋 Task: {task_name}")
    print(f"   🎯 Target: {task_config['target_performance']:.1%} performance")
    
    # Step 4: Execute collaborative solution
    print("\n4. Executing collaborative solution...")
    print("   (This may take a moment as agents collaborate...)")
    
    try:
        results = workflow.solve_task(
            task=task_name,
            collaboration_mode="emergent",
            **task_config
        )
        
        # Step 5: Display results
        print("\n5. 📊 Results:")
        print("   " + "="*40)
        
        if results["status"] == "success":
            print(f"   ✅ Status: {results['status'].upper()}")
            print(f"   📈 Performance Improvement: {results['improvement']:.1f}%")
            print(f"   🧠 Emergent Strategies Discovered: {results['emergent_strategies']}")
            print(f"   🤝 Collaboration Effectiveness: {results['collaboration_effectiveness']:.1%}")
            
            print("\n   🎉 SUCCESS: Agents achieved emergent intelligence!")
            
        else:
            print(f"   ❌ Status: {results['status'].upper()}")
            print(f"   💬 Message: {results.get('error_message', 'Unknown error')}")
    
    except Exception as e:
        print(f"\n   ❌ Error during execution: {str(e)}")
        print("   💡 This is expected in the initial setup - implement core components!")
    
    # Step 6: Next steps
    print("\n6. 🚀 Next Steps:")
    print("   " + "-"*40)
    print("   • Implement core SSM-MetaRL components in core/ directory")
    print("   • Connect tools to actual model implementations")
    print("   • Add real environment data and tasks")
    print("   • Run advanced benchmarks with emergence_benchmark.py")
    print("   • Explore custom agent creation and collaboration patterns")
    
    print("\n✨ Welcome to the future of collaborative AI!")
    print("   Ready to experience 1+1=5 emergent intelligence? 🧠⚡")

if __name__ == "__main__":
    main()