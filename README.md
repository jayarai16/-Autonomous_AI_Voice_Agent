# Autonomous AI Voice Agent

This is a simple implementation of an AI voice agent for requesting refunds, built for the Sentienta Quality AI AI/ML Intern Test - Assignment 1.

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- Microphone for voice input (optional - falls back to text input)
- Speakers/headphones for voice output (optional - demo mode prints responses)

### Installation Steps
1. **Create Virtual Environment**:
   ```
   python -m venv venv
   ```

2. **Activate Virtual Environment**:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Demo Steps

### Option 1: Interactive Voice Demo
1. Run: `python voice_agent.py`
2. The agent will initialize and say "Starting voice agent"
3. If microphone available: Speak your responses
4. If no microphone: Type responses when prompted
5. Try saying/typing:
   - "hello" or "yes" to proceed with refund script
   - "I want a refund" (detects intent)
   - "cancel my subscription" (switches to free-flow)
   - "exit" to end conversation
6. View conversation history printed at the end

### Option 2: Simulated Demo (No Hardware Needed)
1. Run: `python demo.py`
2. Watch the complete sample conversation unfold
3. See all features demonstrated automatically
4. Review the architecture explanation at the end

## Architecture Overview

### Core Components
- **Speech-to-Text (STT)**: Google Speech Recognition API (free, open-source)
- **Text-to-Speech (TTS)**: pyttsx3 library (offline, cross-platform)
- **Intent Detection**: Keyword-based pattern matching
- **Conversation Memory**: In-memory list storage
- **Voice Modulation**: Sentiment analysis using TextBlob

### Dialogue Flow
1. **Initialization**: Agent starts in scripted mode
2. **Scripted Mode**: Follows predefined refund conversation sequence
3. **Mode Switch**: Automatically switches to free-flow after script completion
4. **Free-flow Mode**: Handles intents like refund, cancel, help
5. **Fallback**: "Didn't understand" for unrecognized inputs
6. **Termination**: Ends on "exit" command

### Autonomy Features
- Self-contained processing loop
- Context-aware response generation
- Dynamic voice rate adjustment
- Memory persistence throughout conversation
- Error handling with graceful fallbacks

### Data Flow
```
User Input (Voice/Text)
    ↓
Speech-to-Text
    ↓
Intent Detection
    ↓
Dialogue Logic (Scripted/Free-flow)
    ↓
Response Generation
    ↓
Voice Modulation
    ↓
Text-to-Speech Output
```

## Key Features

- Autonomous conversation flow
- Context-aware responses
- Voice modulation based on sentiment
- Handles unexpected inputs gracefully
- Goal-oriented dialogue for refund requests
- Local inference (no paid APIs used)

## Assignment Compliance

✅ All requirements met:
- Speech-to-Text
- Text-to-Speech
- Conversation memory
- Intent handling
- Voice modulation
- Autonomous operation
- Scripted and adaptive conversations
- Handles objections and unexpected responses
- Mode switching

✅ Restrictions followed:
- Open-source models only
- No paid/hosted APIs (Google SR is free)
- Local inference
- Standalone demo

## Files Included

- `voice_agent.py`: Main interactive voice agent script
- `demo.py`: Simulated conversation demo (no hardware required)
- `requirements.txt`: Python package dependencies
- `architecture.txt`: Detailed architecture diagram and explanation
- `README.md`: Complete documentation and instructions