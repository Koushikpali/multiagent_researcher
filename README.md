# 🔬 Multi-Agent Researcher

A sophisticated multi-agent research system that combines web search, content scraping, and AI-powered analysis to generate comprehensive research reports on any topic.

## 📋 Overview

This project implements an intelligent research pipeline that leverages multiple AI agents working in coordination:

1. **Search Agent** - Conducts web searches to find relevant information
2. **Reader Agent** - Scrapes and extracts detailed content from web pages
3. **Writer Agent** - Synthesizes research data into structured, professional reports
4. **Critic Agent** - Evaluates and provides constructive feedback on generated reports

The system uses LangChain for orchestrating the multi-agent workflow and provides a Flask-based web interface for easy interaction.

## 🚀 Features

- **Multi-Agent Architecture**: Specialized agents for different research tasks
- **Web Search Integration**: Uses Tavily API for reliable web searches
- **Content Scraping**: Beautiful Soup integration for extracting web content
- **Intelligent Report Generation**: Creates structured, professional research reports
- **Quality Assurance**: Built-in critic agent to review and score reports
- **Web Interface**: User-friendly Flask-based UI for submitting research topics
- **LLM Support**: Integration with both Google Generative AI and HuggingFace models

## 📁 Project Structure

```
multiagent_researcher/
├── agent.py              # Core agent definitions (search, reader, writer, critic)
├── app.py                # Flask web application
├── pipeline.py           # Research pipeline orchestration
├── tools/                # Utility modules
│   ├── exporter.py       # Toolkit for agent tools
│   ├── tavilyapi.py      # Web search integration
│   └── beautiful_soup.py # Web scraping functionality
├── templates/            # HTML templates for web UI
│   └── langchain_researcher.html
├── __pycache__/          # Python cache
└── .gitattributes        # Git attributes

```

## 🛠️ Technology Stack

- **Python 3.x** - Core language
- **LangChain** - AI agent orchestration and workflow
- **Flask** - Web framework
- **Beautiful Soup** - Web scraping
- **Tavily API** - Web search
- **HuggingFace** - LLM inference (DeepSeek-R1 model)
- **Google Generative AI** - Alternative LLM support (Gemini)
- **Rich** - Console output formatting
- **Python-dotenv** - Environment variable management

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Koushikpali/multiagent_researcher.git
   cd multiagent_researcher
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with:
   ```
   HUGGINGFACE_API_KEY=your_huggingface_key
   TAVILY_API_KEY=your_tavily_api_key
   GOOGLE_API_KEY=your_google_api_key (optional)
   ```

## 🎯 Usage

### Web Interface

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Enter a research topic** and click the research button

4. **View results** including search findings, scraped content, generated report, and critic feedback

### Command Line

Run research directly from the command line:
```bash
python pipeline.py
```

When prompted, enter your research topic and the system will output all stages of the research process.

## 🔄 How It Works

### Research Pipeline Flow

```
1. Search Agent → Web Search Results
   ↓
2. Reader Agent → Scraped Web Content
   ↓
3. Writer Agent → Structured Research Report
   ↓
4. Critic Agent → Quality Feedback & Score
```

### Agent Descriptions

**Search Agent**
- Uses Tavily API for web searches
- Finds recent, reliable, and detailed information
- Returns search results for the given topic

**Reader Agent**
- Analyzes search results
- Identifies and scrapes the most relevant URL
- Extracts detailed content using Beautiful Soup

**Writer Agent**
- Creates well-structured research reports
- Includes Introduction, Key Findings, Conclusion, and Sources
- Focuses on clarity, factuality, and professionalism

**Critic Agent**
- Reviews generated reports
- Provides scoring (0-10)
- Identifies strengths and areas for improvement
- Delivers honest and constructive feedback

## 📊 Report Structure

Generated reports include:

- **Introduction** - Context and overview of the topic
- **Key Findings** - Minimum 3 well-explained points
- **Conclusion** - Summary and takeaways
- **Sources** - All URLs referenced in the research
- **Critic Review** - Score and feedback

## 🌐 Language Composition

- **HTML** - 71.7%
- **Python** - 28.3%

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Add new features

## 📝 License

This project is open source and available for personal and educational use.

## 👤 Author

**Koushikpali** - [GitHub Profile](https://github.com/Koushikpali)

## 🔗 Repository

[https://github.com/Koushikpali/multiagent_researcher](https://github.com/Koushikpali/multiagent_researcher)

## 🚨 Troubleshooting

**API Key Issues**
- Ensure all API keys are correctly set in `.env` file
- Verify API keys are valid and have proper permissions

**Web Search Failures**
- Check Tavily API status and rate limits
- Verify internet connectivity

**Content Scraping Issues**
- Some websites may block scraping attempts
- Ensure Beautiful Soup is properly installed

## 📚 Dependencies

Key Python packages (see `requirements.txt` for complete list):
- langchain
- langchain-google-genai
- langchain-huggingface
- flask
- beautifulsoup4
- python-dotenv
- rich

---

**Last Updated**: June 2026

For questions or support, please open an issue on GitHub.
