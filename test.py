import openai
openai.api_key = "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"

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)

# create a completion
completion = openai.Completion.create(model="ada", prompt="Hello world")

# print the completion
print(completion.choices[0].text)
