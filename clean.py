import re


def clean(text):
    message = clean_chat(text)
    cleaned = remove_non_message_text(message)
    return cleaned


def clean_chat(chat):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  
    dash_whitespace = r"\s-\s"
    username = r"([\w\s]+)"  
    metadata_end = r":\s"  
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat, "r") as file:
        content = file.read()
    cleaned = re.sub(pattern, " ", content)
    return tuple(cleaned.split("\n"))


def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))


