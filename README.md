# InsightExtractor: AI-Powered Article Analyzer

InsightExtractor is an advanced tool that leverages AI to analyze and extract meaningful insights from articles. Built with Streamlit, OpenAI, and FAISS, this tool allows users to input URLs of articles, process and analyze the content, and retrieve detailed answers with sources to user queries.

## Features

- **User-Friendly Interface**: Built with Streamlit for an interactive and easy-to-use interface.
- **Automated Data Loading**: Input URLs of articles directly into the sidebar for seamless data loading and processing.
- **Text Splitting and Embedding**: Utilizes Recursive Character Text Splitter for efficient text chunking and OpenAI Embeddings for creating vector representations.
- **Robust Query Handling**: Implements RetrievalQAWithSourcesChain to handle user queries and provide precise answers along with sources.
- **Real-Time Processing**: Ensures timely updates and feedback during the data loading and processing stages.

## How It Works

1. **Input URLs**: Users provide URLs of articles through the sidebar.
2. **Data Loading**: Articles are loaded and processed in real-time.
3. **Text Splitting**: The content is split into manageable chunks for better analysis.
4. **Embeddings Creation**: Vector representations of the text chunks are created using OpenAI Embeddings and stored in FAISS.
5. **Query Processing**: Users input their questions, and the tool retrieves relevant answers with sources using the RetrievalQAWithSourcesChain.

## Technologies Used

- **Streamlit**: For building the interactive user interface.
- **OpenAI**: For language model-based text analysis and query handling.
- **FAISS**: For efficient similarity search and vector storage.
- **Python**: The core programming language used for developing the tool.
