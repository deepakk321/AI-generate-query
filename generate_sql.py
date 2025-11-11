import os
import google.generativeai as genai

def read_schema(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_user_query():
    return input("Enter your query message: ")

def generate_sql(schema, user_query):
    api_key = "AIzaSyDa1jSnlXMUf9pXe4UPeo1nGIqeqkbJqvg" #os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise Exception("Set GOOGLE_API_KEY environment variable.")
    genai.configure(api_key=api_key)
    # print(genai.list_models())
    # for m in genai.list_models():
    #     if "generateContent" in m.supported_generation_methods:
    #         print("model name - ",m.name)
    model = genai.GenerativeModel('gemini-pro-latest')
    prompt = (
        f"Given the following database schema:\n{schema}\n"
        f"Generate an SQL query for: {user_query}\n"
        "Only output the SQL query."
    )
    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    schema_file = "schema.txt"  # Change path if needed
    schema = read_schema(schema_file)
    user_query = get_user_query()
    sql_query = generate_sql(schema, user_query)
    print("\nGenerated SQL Query:\n", sql_query)

if __name__ == "__main__":
    main()