# Think Remover Extension

The Think Remover extension is designed to remove or replace specific patterns of text within the conversation history of a chatbot. It provides a user-friendly interface to configure the extension's behavior.

## Key Features

- **Enabled/Disabled**: Toggle the extension on or off.
- **Scope**: Choose the scope of the extension's operation, either for both internal and visible messages, or for internal or visible messages separately.
- **Keep Last X Messages**: Specify the number of recent messages to keep unmodified.
- **Pattern Tags**: Define the starting and ending tags for the pattern to be removed or replaced.
- **Keep Tags**: Option to keep the starting and ending tags in the output.
- **Replace By**: Specify the text to replace the content between the tags with.

## Installation

1. Clone the [text-generation-webui](https://github.com/oobabooga/text-generation-webui) repository.
2. Navigate to the `extensions` directory.
3. Clone or download the `think_remover` extension into the `extensions` directory.
4. Restart the text-generation-webui interface.

## Usage

1. Enable or disable the extension using the checkbox.
2. Select the scope of the extension's operation using the dropdown menu.
3. Set the number of recent messages to keep unmodified using the number input field.
4. Enter the starting and ending tags for the pattern using the text input fields.
5. Choose whether to keep the tags in the output using the checkbox.
6. Enter the text to replace the content between the tags with using the text input field.

The Think Remover extension will then apply the configured settings to the conversation history, removing or replacing the specified patterns as desired. The parameters can be modified at any time during the conversation, and the changes will be automatically applied to the conversation history.

## Limitations

- The extension currently supports only a single pattern definition.
- The pattern tags must be unique within the conversation history.
- The extension does not handle nested patterns or complex regular expressions.
- The extension is designed to be used with the [text-generation-webui](https://github.com/oobabooga/text-generation-webui) interface.

## Examples of Use

- To remove or replace thoughts and ideas that are not relevant to the conversation, use `<think>` and `</think>` as the starting and ending tags.
- To remove or replace sensitive or inappropriate content, use unique tags that are not likely to appear in the conversation naturally.

## License

This extension is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.