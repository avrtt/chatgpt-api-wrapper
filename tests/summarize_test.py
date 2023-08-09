import asyncio
from chatgpt_api_wrapper.tools import summarize


def test_summarize():
    example = ""
    summary = asyncio.run(summarize(example))

    assert summary
    assert len(summary) > 10
    assert summary != example
    
    print(summary)
