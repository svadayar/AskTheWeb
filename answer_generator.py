def generate_answer(context, question):
    prompt = f"""Use the following context to answer the question:\n{context}\n\nQ: {question}\nA:"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
