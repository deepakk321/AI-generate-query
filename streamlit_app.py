import streamlit as st
from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env if present in project root so developers can put GOOGLE_API_KEY there locally
load_dotenv()

from generate_sql import generate_sql


def main():
    st.title("AI Generate SQL")

    st.markdown(
        "Upload a database schema (text file) or leave empty to use `schema.txt` in the project root, then enter a user query to generate an SQL query."
    )

    uploaded_file = st.file_uploader("Upload schema file", type=["txt", "sql"], help="A text file containing CREATE TABLE statements or similar")

    if uploaded_file is not None:
        try:
            schema_bytes = uploaded_file.read()
            schema = schema_bytes.decode("utf-8")
        except Exception:
            st.error("Could not read uploaded file. Make sure it's a UTF-8 encoded text file.")
            return
    else:
        # fallback to schema.txt in project root
        schema_path = Path(__file__).parent / "schema.txt"
        if schema_path.exists():
            schema = schema_path.read_text(encoding="utf-8")
            st.info(f"Using schema from `{schema_path.name}` in project root")
        else:
            schema = ""

    if schema:
        with st.expander("Preview schema", expanded=False):
            st.code(schema)

    user_query = st.text_input("Enter your query", placeholder="e.g. Find total order amount per user in last 30 days")

    if st.button("Generate SQL"):
        if not user_query:
            st.warning("Please enter a query to generate SQL for.")
        elif not schema:
            st.warning("No schema available. Upload a schema file or add `schema.txt` to the project root.")
        else:
            with st.spinner("Generating SQL..."):
                try:
                    sql = generate_sql(schema, user_query)
                except Exception as e:
                    st.error(f"Error generating SQL: {e}")
                else:
                    st.success("Generated SQL")
                    st.code(sql, language="sql")


if __name__ == "__main__":
    main()
