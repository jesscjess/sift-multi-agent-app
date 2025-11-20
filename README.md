# Multi-Agent Smart Shopping System

AI-powered shopping assistant that compares prices across stores and recommends optimal purchasing strategies using a multi-agent architecture.

## Overview

This system uses Google's ADK (Agent Development Kit) to orchestrate multiple specialized agents:

- **Orchestrator Agent**: Coordinates the workflow and manages agent interactions
- **Product Normalizer Agent**: Finds and normalizes product data across stores
- **Optimizer Agent**: Calculates price differences and identifies savings opportunities
- **Evaluator Agent**: Recommends the best shopping strategy based on multiple factors

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd multi-agent-smart-shopper
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Streamlit chat interface:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Project Structure

```
multi-agent-smart-shopper/
├── agents/                      # Agent implementations
│   ├── __init__.py
│   ├── orchestrator.py         # Main coordinator agent
│   ├── product_normalizer.py   # Product search and normalization
│   ├── optimizer.py            # Price comparison and optimization
│   └── evaluator.py            # Recommendation engine
├── app.py                       # Streamlit chat interface
├── requirements.txt             # Python dependencies
├── CLAUDE.md                    # Documentation for Claude Code
├── TODO.md                      # Project tasks and roadmap
└── README.md                    # This file
```

## Usage Examples

Once the agents are fully implemented, you can ask questions like:

- "Find the cheapest place to buy milk and eggs"
- "Compare prices for apples across all stores"
- "Where should I buy bread, butter, and jam to save the most?"
- "Is it worth shopping at multiple stores for my grocery list?"

## Development Status

🚧 **In Development** - This project is currently being built for a hackathon.

**Completed:**
- ✅ Project structure and architecture
- ✅ Agent skeleton files
- ✅ Streamlit chat interface

**In Progress:**
- 🔄 Agent implementations with Google ADK
- 🔄 Store integrations
- 🔄 Price comparison logic

## Architecture

The system follows a sequential multi-agent workflow:

1. User submits query via chat interface
2. Orchestrator analyzes and routes the request
3. Product Normalizer finds products across stores
4. Optimizer calculates price differences and savings
5. Evaluator recommends optimal purchasing strategy
6. Results are returned to the user

See [CLAUDE.md](CLAUDE.md) for detailed architecture documentation.

## Contributing

This is a hackathon project. Contributions and suggestions are welcome!

## License

[Add license information]
