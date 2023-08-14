# gloo-starter

Gloo was designed to help you have a fully-typed task-based approach to making LLM apps. Each call to an LLM is a defined task with an input and an output, and all the results are logged and sent to the Gloo dashboard (if you have configured it to do this).

Using gloo is a two step process:

1. Define a yaml that contains your tasks with inputs and outputs
2. Generate a task.py file per task that you can edit and configure.

## Getting started

### Define your tasks.yaml

To generate your tasks, first declare a tasks.yaml under `gloo/tasks.yaml`. You may place this
anywhere you like.

The following file has two tasks -- one that is used in a semantic search pipeline, and the other one in a chatbot that labels movie quotes and tells you the genre name or responds with a generated friendlyResponse if it doesn't know the answer.

```yaml
tasks:
  SearchDocuments:
    input: SearchInput
    output: SearchOutput
  ClassifyMovieGenre:
    input: ClassifyMovieInput
    output: ClassifyMovieOutput

types:
  ClassifyMovieInput:
    message: string
  ClassifyMovieOutput:
    clues: list<string>
    reasoning: string
    # If you want multi-class classification, use a list like list<Category>
    classification: Category
    friendlyResponse: string
  Genre:
    enum:
      - scifi
      - fantasy
      - mystery
  ## Search
  SearchInput:
    query: string
    context: string
  SearchOutput:
    clues: list<string>
    reasoning: string
    isAnswerInContext: string
    answer: string
```

## Generate the client

`gloo-cli generate python --yaml app/gloo/tasks.yaml`

If you don't specify the --yaml flag, the tool will look for a `gloo` directory and a `tasks.yaml`
in that directory

Gloo will generate 2 relevant files with version 0:

```
YourProject/
  gloo/
    tasks.yaml
    your-task/
      v0/
        task.py
        test.py
```

## Modify your task.py file

Please take a look at each task.py file to see how to configure them. More detailed documentation is coming soon.
