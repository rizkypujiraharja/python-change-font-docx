# Python Font Changer Docx
this is my first python code, this code is created to change the font of a docx document

## How to use
Install [python-docx](https://python-docx.readthedocs.io/)

    pip install python-docx

Change font on document

    python3 change.py -i=Test.docx
    
# Available arguments    
| Argument | Short | Required | Default | Info |
| - | - | - | - | - |
| --input | -i | `true` | | Input path file |
| --output | -o | `false` | result_{filename}.docx | Output path file |
| --font | -f | `false` | Arial | Font name |
