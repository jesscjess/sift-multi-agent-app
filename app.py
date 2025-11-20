"""Streamlit Chat Interface for Multi-Agent Smart Shopping System"""

import streamlit as st
from agents import (
    OrchestratorAgent,
    ProductNormalizerAgent,
    OptimizerAgent,
    EvaluatorAgent,
)

# Page configuration
st.set_page_config(
    page_title="Smart Shopping Assistant",
    page_icon="🛒",
    layout="centered"
)

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize agents (singleton pattern)
if "orchestrator" not in st.session_state:
    # Create subagents
    product_normalizer = ProductNormalizerAgent()
    optimizer = OptimizerAgent()
    evaluator = EvaluatorAgent()

    # Create and initialize orchestrator
    orchestrator = OrchestratorAgent()
    orchestrator.initialize_agents(product_normalizer, optimizer, evaluator)

    st.session_state.orchestrator = orchestrator

# App header
st.title("🛒 Smart Shopping Assistant")
st.caption("Find the best deals across stores with AI-powered comparison")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to buy?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing prices across stores..."):
            # Process request through orchestrator
            result = st.session_state.orchestrator.process_request(prompt)

            # Format response (temporary until agents are implemented)
            if result.get("status") == "not_implemented":
                response = f"""I'm ready to help you find the best deals! 🎯

**Your request:** {prompt}

The multi-agent system is being set up with:
- 🔍 **Product Normalizer**: Will find products across stores
- 💰 **Optimizer**: Will calculate price differences
- ⭐ **Evaluator**: Will recommend the best option

*Note: Agent implementation is in progress. Soon I'll be able to provide real price comparisons!*
"""
            else:
                response = result.get("message", "Something went wrong")

            st.markdown(response)

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.info(
        "This Smart Shopping Assistant uses a multi-agent system to:\n\n"
        "1. Find products across multiple stores\n"
        "2. Compare prices and calculate savings\n"
        "3. Recommend the best shopping strategy"
    )

    st.header("Example Queries")
    st.code("Find the cheapest place to buy milk and eggs")
    st.code("Compare prices for apples across stores")
    st.code("Where should I buy bread, butter, and jam?")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
