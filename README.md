# PaLM-powered Q&A System 🎓 
This project  implements a question-answering(QA) system designed to streamline student support for Codebasics. Built with LangChain, Hugging Face Streamlit, and Google PaLM, the system leverages cutting-edge AI to provide accurate and efficient answers to student inquiries directly on the Codebasics website.

The system reads from a CSV file containing frequently asked questions (FAQs) and their corresponding answers, embeds the data using Hugging Face's instructor model, and stores the embeddings in a Chromadb vector store. The QA system then uses a retrieval mechanism to fetch the relevant answers based on user queries. The interface is built using Streamlit for easy interaction.

### 🎯 Key Features
- **Google PaLM**: Employs Google PaLM for powerful language understanding and generation. It generates answers with controlled randomness.
- **LangChain**: Utilizes LangChain for natural language processing tasks.
- **Hugging Face Instruct Embeddings 🤗**: Uses the instructor model to embed the data for efficient retrieval.
- **Chroma Vector Store 🤗**:Stores the embeddings and retrieves them based on similarity scores.
- **Streamlit**: Provides an interactive user interface for easy access and interaction.

## Installation

1. Clone the repository:
  ```bash
   git clone https://github.com/Lakshmiec/palm-powered-qa-system.git
  ```
2. Navigate to the project repository :
    ```bash
  cd palm-powered-qa-system
  ```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a .env file in the root directory of your project.
   - Acquire an API key through makersuite.google.com and put it in .env file:
```toml
GOOGLE_API_KEY = "your-google-api-key"
```
## Usage

1. Run the Streamlit app by executing:

    ```
    streamlit run main.py
    ```
## File Structure
├── main.py # Streamlit app file
├── palm_langchain_qa_system.py # Main logic for the QA system
├── faqs_codebasics.csv # CSV file containing FAQs
├── .env # Environment variables file
├── requirements.txt # Python packages required
└── README.md # This readme file


## Detailed Explanation

### Google Palm LLM

- **Temperature Setting**: The temperature is set to 0.1, which makes the model's output more deterministic and conservative. This is suitable for generating accurate and reliable answers.

### Hugging Face Embeddings

- **Model**: The project uses `hkunlp/instructor-large` for generating embeddings of the FAQ data. These embeddings are then stored in the Chroma vector store.

### Chroma Vector Store

- **Initialization**: The `initialize_chroma_vector_store` function reads the CSV file and stores the embeddings.
- **Persistence**: The vector store is persisted to disk to avoid reloading and recomputing the embeddings.

### Streamlit Interface

- **Initialize Vector Store**: A button to initialize and persist the vector store.
- **Ask Questions**: A text input field for users to enter their questions. The system fetches the most relevant answer based on the user's query.

## How to Interact with the QA System

1. **Initialize Vector Store**:
    - Click on the "Initialize Vector Store" button. This step is required only once or whenever the CSV data is updated.

2. **Ask a Question**:
    - Enter your question in the text input field and click on the "Get Answer" button.
    - The system will display the answer fetched from the vector store based on the context.



### Ideal For:

-> Educational institutions seeking to automate student support.
-> Organizations aiming to leverage AI for efficient knowledge management.
-> Developers interested in exploring LangChain, Streamlit, and PaLM for building interactive applications.

### Get Started Today!

1. Clone the repository.
2. Install required libraries (refer to installation instructions).
3. Configure LangChain and PaLM access.
4. Run the application using Streamlit.
