
# This file is autogenerated by the gloo compiler
# Do not edit this file directly
# (skip unused imports)
# ruff: noqa: F401
# flake8: noqa
# pylint: skip-file
# isort: skip_file


from gloo_py import OpenAILLMClient, ENV

GPT35Client = OpenAILLMClient(provider='openai', __type='''completion''', max_tokens=200, api_key=ENV.OPENAI_API_KEY, temperature=0, model='''gpt-3.5-turbo-instruct''')
