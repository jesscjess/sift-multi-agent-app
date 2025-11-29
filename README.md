# Sift - Smart Recycling Assistant

AI-powered recycling guidance that helps you determine if items are actually recyclable in your area. Many plastics are labeled as recyclable but aren't accepted by local recycling programs - Sift provides location-specific guidance to help you make informed decisions.

## Overview

Sift uses Google's ADK (Agent Development Kit) to orchestrate multiple specialized agents that analyze items and provide accurate, location-based recycling information:

- **Orchestrator Agent**: Coordinates the workflow and manages agent interactions
- **Product Intelligence Agent**: Identifies material types and plastic codes from descriptions or images
- **Location Agent**: Looks up location-specific recycling regulations
- **Synthesis Agent**: Provides specific instructions and tips on which plastic codes to watch for

## The Problem

Not all "recyclable" plastics are actually recycled:
- Different municipalities accept different materials
- Plastic codes (PETE #1, HDPE #2, etc.) have varying acceptance rates
- Many items labeled with recycling symbols aren't accepted locally
- Composite materials and contaminated items often can't be recycled

**Sift solves this** by providing accurate, location-specific recycling guidance.

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

### First-Time Setup

On your first use, you'll be prompted to set up your profile:
1. Enter your location (zip code or city)
2. Your local recycling rules will be stored for future queries
3. Start scanning items!

## Project Structure

```
multi-agent-smart-shopper/
├── agents/                      # Agent implementations
│   ├── __init__.py
│   ├── orchestrator.py         # Main coordinator agent
│   ├── product_intelligence.py # Material analysis
│   ├── location.py             # Local rules lookup
│   └── synthesis.py            # Recommendations
├── app.py                       # Streamlit chat interface
├── requirements.txt             # Python dependencies
├── CLAUDE.md                    # Documentation for Claude Code
├── TODO.md                      # Project tasks and roadmap
└── README.md                    # This file
```

## Usage Examples

Once fully implemented, you can ask questions like:

**Text Queries:**
- "Is this plastic bottle recyclable in my area?"
- "Can I recycle HDPE #2 containers?"
- "What plastic codes should I avoid?"
- "Is styrofoam recyclable near me?"

**Image Upload:**
- Upload a photo of the recycling symbol
- Upload a picture of the product packaging
- Scan the resin identification code

**Example Response:**
```
♻️ Material Identified: PETE #1 (Polyethylene Terephthalate)

✅ Recyclable in your area (San Francisco, CA)

Instructions:
1. Rinse the container thoroughly
2. Remove the cap (HDPE #2 - also recyclable)
3. Place in your blue recycling bin
4. Do not flatten - recycling machines sort by shape

💡 Tips to Remember:
- PETE #1 and HDPE #2 are widely accepted
- Avoid PVC #3 and PS #6 (rarely recycled)
- Check for the "Recycle Ready" symbol
- When in doubt, check with your local facility
```

## Development Status

🚧 **In Development** - This project is being built for a hackathon.

**Completed:**
- ✅ Project structure and architecture
- ✅ Agent skeleton files
- ✅ Streamlit chat interface foundation
- ✅ Documentation and planning

**In Progress:**
- 🔄 Agent implementations with Google ADK
- 🔄 User profile system
- 🔄 Material identification system
- 🔄 Recycling database integration

## Architecture

The system follows a sequential multi-agent workflow:

1. User submits item (description or image) via chat interface
2. User profile provides location data
3. Orchestrator analyzes and routes the request
4. Product Intelligence Agent identifies the material type and codes
5. Location Agent checks recycling regulations for that location
6. Synthesis Agent generates specific instructions and tips
7. Results are returned to the user

See [CLAUDE.md](CLAUDE.md) for detailed architecture documentation.

## Why This Matters

- **Environmental Impact**: Proper recycling reduces waste and pollution
- **Contamination Prevention**: Placing non-recyclables in bins contaminates entire batches
- **Informed Decisions**: Knowledge helps consumers choose better products
- **Education**: Understanding plastic codes empowers better purchasing

## Contributing

This is a hackathon project. Contributions and suggestions are welcome!

## License

[Add license information]
