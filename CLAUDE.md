# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Sift** - A multi-agent system using Google's ADK (Agent Development Kit) framework that helps users determine if items are recyclable in their area. Many plastics are labeled as recyclable but aren't actually accepted by local recycling programs. Sift provides location-specific recycling guidance to help users make informed purchasing decisions.

## Architecture

### Agent Hierarchy

The system uses three specialized agents coordinated by an orchestrator:

**Orchestrator Agent** (Main Coordinator)
- Routes user requests to appropriate subagents
- Manages multi-agent workflows
- Aggregates results from subagents
- Returns final recommendations to the chat interface

**Product Intelligence Agent**
- Analyzes item descriptions or images
- Identifies material types and plastic codes
- Extracts relevant recycling information

**Location Agent**
- Looks up local recycling regulations based on user location
- Determines if specific materials are accepted in the user's area
- Provides location-specific guidelines

**Synthesis Agent**
- Generates specific recycling instructions
- Provides tips on plastic codes to watch for
- Suggests eco-friendly alternatives when items aren't recyclable

### Communication Flow

1. User submits item (description or image) via chat interface
2. User profile provides location data
3. Orchestrator agent analyzes request and routes to subagents
4. Product Intelligence Agent identifies material type and plastic codes
5. Location Agent checks local recycling rules for that material
6. Synthesis Agent generates instructions and educational tips
7. Orchestrator aggregates and returns results

## Technical Stack

- **Framework**: Google ADK for multi-agent orchestration
- **Frontend**: Streamlit (Python-native chat interface with built-in components)
- **Language**: Python (entire stack)
- **Image Processing**: PIL/Pillow for image handling (when users upload photos)

## User Profile System

Users create a profile on first use that stores:
- Location data (zip code, city, or region)
- Local recycling program information
- Preferences for recycling guidance

This allows the system to provide accurate, location-specific recycling information.

## Development Notes

### Multi-Agent Coordination

The orchestrator uses ADK's multi-agent capabilities to manage subagent interactions. Each subagent should be designed with:
- Clear input/output contracts
- Specific tools and functions for their domain
- Error handling for their specialized tasks

### Agent Communication Protocol

Subagents communicate through the orchestrator, not directly with each other. The typical flow is sequential:
Product Intelligence Agent → Location Agent → Synthesis Agent

However, the orchestrator should be flexible enough to parallelize or reorder steps when appropriate.

### Key Implementation Considerations

1. **Material Identification**: System must accurately identify plastic types (PETE #1, HDPE #2, etc.) from descriptions or images
2. **Location Data**: Recycling rules vary significantly by municipality - location data is critical for accuracy
3. **Database Accuracy**: Recycling regulations change frequently - need a strategy for keeping data current
4. **Image Processing**: When users upload photos, need robust symbol/code recognition (recycling symbols, resin codes)
5. **Educational Component**: Help users understand why certain plastics aren't recyclable, not just yes/no answers
6. **Privacy**: User location data should be handled securely and transparently
7. **Fallback Mechanisms**: Handle cases where material can't be identified or local rules aren't available
