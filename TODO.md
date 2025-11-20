# EcoScan - Multi-Agent Recycling Assistant - TODO

## Project Overview
Building **EcoScan**, a multi-agent system using Google's ADK framework that helps users determine if items are recyclable in their area. Many plastics are labeled as recyclable but aren't accepted by local programs.

**System Components:**
- 1 Main orchestrator agent
- 3 Specialized subagents for recycling analysis
- Web-based chat interface with user profiles
- Location-based recycling guidance

## Architecture Plan
**Orchestrator Agent**: Main coordinator for routing requests and managing subagent interactions

**Product Intelligence Agent**: Analyzes item descriptions/images and identifies material types and plastic codes

**Location Agent**: Looks up location-based recycling regulations and determines if materials are accepted locally

**Synthesis Agent**: Provides specific recycling instructions and tips on plastic codes to watch for

**Chat Interface**: Streamlit-based frontend with user profile system for location data

**User Profile System**: Stores user location and local recycling program information

## TODO List

### Phase 1: Setup & Architecture
- [x] Define the 3 subagent roles and capabilities
- [x] Create CLAUDE.md documentation for future development
- [x] Set up project structure (agents/, app.py, requirements.txt)
- [x] Create skeleton agent classes with method stubs
- [x] Set up Streamlit chat interface
- [x] Pivot to EcoScan concept and update documentation
- [ ] Install and configure Google ADK
- [ ] Design user profile system for location storage
- [ ] Define data models for materials, recycling rules, and locations
- [ ] Design API contracts between agents
- [ ] Research recycling databases and APIs for local regulations

### Phase 2: Core Implementation
- [ ] Implement user profile system in Streamlit
  - [ ] Location input on first use
  - [ ] Profile storage in session state
  - [ ] Profile management UI
- [ ] Implement the main orchestrator agent
- [ ] Implement Product Intelligence Agent
  - [ ] Text description parsing for material identification
  - [ ] Image processing for recycling symbols and codes
  - [ ] Plastic resin code recognition (PETE #1, HDPE #2, etc.)
  - [ ] Material type classification
- [ ] Implement Location Agent
  - [ ] Location-based recycling database integration
  - [ ] Material acceptability lookup by location
  - [ ] Special handling requirements identification
  - [ ] Recycling facility locator
- [ ] Implement Synthesis Agent
  - [ ] Instruction generation based on material and location
  - [ ] Educational tips on plastic codes
  - [ ] Eco-friendly alternative suggestions
  - [ ] "What to watch for" guidance formatting
- [ ] Set up inter-agent communication and coordination

### Phase 3: Interface & Integration
- [x] Create basic Streamlit chat interface
- [ ] Update Streamlit interface for EcoScan branding
  - [ ] Add image upload capability
  - [ ] Update example queries for recycling
  - [ ] Add user profile setup flow
  - [ ] Display recycling codes reference guide
- [ ] Add logging and monitoring for agent interactions
- [ ] Implement error handling and fallback mechanisms
- [ ] Add loading states and progress indicators in UI

### Phase 4: Data & Integration
- [ ] Identify recycling regulation data sources
  - [ ] Municipal recycling program databases
  - [ ] State/regional recycling guidelines
  - [ ] Material recovery facility capabilities
- [ ] Build or integrate material identification system
  - [ ] Plastic resin code database
  - [ ] Recycling symbol recognition
  - [ ] Common product material composition
- [ ] Create fallback responses for unknown materials/locations

### Phase 5: Testing & Deployment
- [ ] Test individual agents independently
- [ ] Test full multi-agent workflow integration
- [ ] Test with various plastic types and recycling symbols
- [ ] Validate location-based accuracy
- [ ] Set up deployment configuration (local/cloud)

## Key Technical Considerations
1. Use ADK's multi-agent orchestration capabilities
2. Accurate material identification from text and images is critical
3. Recycling rules vary significantly by location - location data is essential
4. Keep recycling regulation data current (rules change frequently)
5. Implement proper error handling and fallback mechanisms
6. Privacy considerations for storing user location data
7. Educational component - explain WHY items aren't recyclable

## Questions Answered
- ✓ What are the specific roles/capabilities for the 3 subagents?
  - Product Intelligence Agent, Location Agent, Synthesis Agent
- ✓ What frontend framework preference for the chat interface?
  - Streamlit (Python-native, fast setup, built-in chat components)
- ✓ How will users input items?
  - Text description or image upload
- ✓ How will location be handled?
  - User profile system with location stored on initialization
- ✓ What should the output include?
  - Specific recycling instructions with tips on plastic codes to watch for

## Open Questions
- Which recycling databases/APIs should we use for local regulations?
- What image recognition library/service for identifying recycling symbols?
- Should we support barcode scanning for product lookup?
- Local development vs cloud deployment preference?
- Authentication system needed or just session-based profiles?
- How to handle items with multiple materials (e.g., composite packaging)?
