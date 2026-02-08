import random
import re
memory = {}
def chatwai(prompt):
    prompt_lower = prompt.lower()
    if any(word in prompt_lower for word in ["hi", "hello", "hey"]):
        return "Hello! Ask me something interesting."
    if "your name" in prompt_lower:
        return "I'm a Flask-based AI assistant built with logic and reasoning."
    if "how are you" in prompt_lower:
        return "I run on logic, so I'm always functioning optimally :)"
    math_match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', prompt_lower)
    if math_match:
        a, op, b = math_match.groups()
        a, b = int(a), int(b)
        result = eval(f"{a}{op}{b}")
        return f"The answer is {result}."
    if "better" in prompt_lower and " or " in prompt_lower:
        items = prompt_lower.split("better")[0].split(" or ")
        if len(items) >= 2:
            return f"It depends on context. {items[0].strip()} may be better for some situations, while {items[1].strip()} works better in others."
        
    if prompt_lower.startswith("why"):
        return "That's a great question. Usually the reason involves cause and effect. Can you be more specific?"
    if prompt_lower.startswith("what is") or prompt_lower.startswith("define"):
        topic = prompt.split(" ", 2)[-1]
        return f"{topic.capitalize()} generally refers to a concept or system related to knowledge, science, or daily life."
    if "advantage" in prompt_lower or "disadvantage" in prompt_lower:
        return "Advantages help achieve goals efficiently, while disadvantages create limitations. Both should be considered before decisions."
    if "do you think" in prompt_lower:
        return "I think both perspectives have value. It often depends on the situation and priorities."
    memory["last"] = prompt
    if "what did i say" in prompt_lower:
        return f"You last said: '{memory.get('last','I forgot')}'"
    smart_replies = [
        "Interesting. Let's analyze that logically.",
        "That depends on multiple factors.",
        "Can you clarify your question so I can reason better?",
        "From a reasoning perspective, context matters.",
        "That involves both benefits and trade-offs."
    ]
    return random.choice(smart_replies)


