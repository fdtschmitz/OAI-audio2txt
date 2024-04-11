from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Você é um assistente poeta, especializado em criar 'Hello World' em várias linguagens diferentes."},
    {"role": "user", "content": "Componha uma poema que possui exemplos de Hello World nas linguagens mais populares do mercado."}
  ]
)

print(completion.choices[0].message)