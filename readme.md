
## Useful commands
```bash
poetry run jupyter notebook
```

```bash
poetry run ipython kernel install --user --name=dev && jupyter notebook
```

vscode doesn't recognize default path of installed venvs via poetry so configure
the venvs to be within the project
```bash
poetry config virtualenvs.in-project true
poetry install
```

## Containers
Multiple dev-container setup in case we need different builds / environments. 

#### test
reserved for any changes to builds

#### dev
reserved for app-level code changes


## Sample diffbot response
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 03 Feb 2024 05:49:01 GMT
Content-Type: text/event-stream; charset=utf-8
Transfer-Encoding: chunked
Connection: close
Expires: Sun, 02 Feb 2025 05:49:01 GMT
Cache-Control: max-age=31536000, no-cache
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: frame-ancestors 'self' diffbot.com *.diffbot.com;
X-Content-Type-Options: nosniff

data: [{"diffbot_request": {"name": "Twitter", "extra_fields": ["ceo"]}, "diffbot_response": {"status": 200, "message": null, "plugin_url": "https://llm.diffbot.com/api/v1/enhance_organization?name=Twitter&extra_fields=ceo", "method": "get", "content": {"status": 200, "message": null, "type": "Organization", "entity": {"twitterUri": "twitter.com/Twitter", "isAcquired": false, "revenue": {"currency": "USD", "value": 5077000000.0}, "logo": "https://llm.diffbot.com/img/J1Mo.jpg", "foundingDate": {"str": "d2006-01-01", "precision": 3, "timestamp": 1136073600000}, "image": "https://llm.diffbot.com/img/O6Z6.jpg", "wikipediaUri": "en.wikipedia.org/wiki/Twitter", "diffbotUri": "http://diffbot.com/entity/E1v2UkreyPXm7leKR5WspGw", "ipo": {"date": {"str": "d2013-11-07", "precision": 3, "timestamp": 1383782400000}, "stockExchange": "nyse"}, "capitalization": {"currency": "USD", "value": 25449001000.0}, "name": "Twitter", "totalInvestment": {"currency": "USD", "value": 12869191680.0}, "linkedInUri": "linkedin.com/company/twitter", "nbEmployees": 7500, "isDissolved": false, "description": "X, formerly and commonly referred to as Twitter, is a social media website based in the United States. With over 500 million users, it is one of the world's largest social networks. Users can share and post text messages, images, and videos known historically as \"tweets\". X also includes direct messaging, video and audio calling, bookmarks, lists and communities, and Spaces, a social audio feature. Users can vote on context added by approved users using the Community Notes feature. Although the service is now called X, the primary URL remains twitter.com , with the x.com domain name redirecting to that address.", "homepageUri": "twitter.com", "ceo": {"name": "Linda Yaccarino", "diffbotUri": "http://diffbot.com/entity/E2N5_3UXEPqiV0lSlA7JZNA"}, "isPublic": false, "remoteScore": 0.8633639, "crunchbaseUri": "crunchbase.com/organization/twitter", "location": {"country": {"name": "United States of America"}, "city": {"name": "San Francisco"}, "region": {"name": "California"}}}, "articles": null}}}]

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": "", "role": "assistant", "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": "The", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": " CEO", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": " of", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": " Twitter", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": " is", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": " Linda", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": " Y", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": "acc", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": "ar", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": "ino", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": ".", "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": null, "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

data: {"id": "chatcmpl-8o3BdrTnxoSuqUBhicJbCNkV9SLvz", "choices": [{"delta": {"content": null, "role": null, "tool_call_id": null, "tool_calls": null}, "finish_reason": "stop", "index": 0}], "created": 1706939341, "model": "gpt-3.5-turbo-0613", "system_fingerprint": null, "object": "chat.completion.chunk"}

