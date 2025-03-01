import re
import gradio as gr
import html

params = {
    "display_name": "Think Remover",
    "is_tab": False,
    "enabled": True,
    "scope": "both",  # possibles values: both/internal/visible
    "keep_x_messages": 5,
    "patterns": {
        "replace_by": "",
        "starting": "<think>",
        "ending": "</think>",
        "keep_tags": False,
    }
}

def replace_think_tags(text, pattern):
    """
    Replace text between <think> and </think> tags with "...".

    Parameters:
    text (str): The text to be processed.
    pattern (str): The regex pattern to search for.

    Returns:
    str: The processed text.
    """
    def replacer(match):
        replace_by = params['patterns']['replace_by']
        starting_pattern = params['patterns']['starting']
        ending_pattern = params['patterns']['ending']
        keep_tags = params['patterns']['keep_tags']
        if keep_tags:
            return f"{starting_pattern}{replace_by}{ending_pattern}"
        else:
            return f"{replace_by}"

    return re.sub(pattern, replacer, text, flags=re.DOTALL)

def modify_history_segment(segment, pattern):
    """
    Modify a segment of the history by replacing text between <think> and </think> tags.

    Parameters:
    segment (list): A list of tuples representing a segment of the history.
    pattern (str): The regex pattern to search for.

    Returns:
    list: The modified segment.
    """
    modified_segment = []
    for user_input, response in segment:
        decoded_response = html.unescape(response)
        modified_response = replace_think_tags(decoded_response, pattern)
        modified_segment.append((user_input, modified_response))
    return modified_segment

def history_modifier(history):
    """
    Modifies the chat history. Only used in chat mode.
    """
    pattern = f"{params['patterns']['starting']}(.*?){params['patterns']['ending']}"

    if params['enabled']:
        if params['scope'] in ['both', 'visible'] and 'visible' in history and history['visible']:
            keep_count = params['keep_x_messages']
            if len(history['visible']) > keep_count:
                history['visible'] = modify_history_segment(history['visible'][:-keep_count], pattern) + history['visible'][-keep_count:]

        if params['scope'] in ['both', 'internal'] and 'internal' in history and history['internal']:
            keep_count = params['keep_x_messages']
            if len(history['internal']) > keep_count:
                history['internal'] = modify_history_segment(history['internal'][:-keep_count], pattern) + history['internal'][-keep_count:]

    return history

def history_modifier0(history):
    return history

def setup():
    """
    Gets executed only once, when the extension is imported.
    """
    pass

def ui():
    with gr.Accordion("Think Remover", open=False, elem_classes="Think Remover"):
        with gr.Row():
            enabled = gr.Checkbox(value=params['enabled'], label='Enabled', info="Enable or disable the Think Remover extension.")
            scope = gr.Dropdown(choices=["both", "internal", "visible"], value=params['scope'], label='Scope', info="Choose the scope of the extension.")
            keep_x_messages = gr.Number(value=params['keep_x_messages'], label='Keep Last X Messages', info="Number of recent messages to keep unmodified.")

        with gr.Row():
            starting_tag = gr.Textbox(value=params['patterns']['starting'], label='Starting Tag', info="The starting tag for the pattern.")
            ending_tag = gr.Textbox(value=params['patterns']['ending'], label='Ending Tag', info="The ending tag for the pattern.")

        with gr.Row():
            keep_tags = gr.Checkbox(value=params['patterns']['keep_tags'], label='Keep Tags', info="Keep the <think> and </think> tags in the output.")
            replace_by = gr.Textbox(value=params['patterns']['replace_by'], label='Replace By', info="The text to replace the content between the tags with.")

        def update_params(enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by):
            params.update({
                'enabled': enabled,
                'scope': scope,
                'keep_x_messages': keep_x_messages,
                'patterns': {
                    'starting': starting_tag,
                    'ending': ending_tag,
                    'keep_tags': keep_tags,
                    'replace_by': replace_by
                }
            })

        enabled.change(update_params, [enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by], None)
        scope.change(update_params, [enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by], None)
        keep_x_messages.change(update_params, [enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by], None)
        starting_tag.change(update_params, [enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by], None)
        ending_tag.change(update_params, [enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by], None)
        keep_tags.change(update_params, [enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by], None)
        replace_by.change(update_params, [enabled, scope, keep_x_messages, starting_tag, ending_tag, keep_tags, replace_by], None)