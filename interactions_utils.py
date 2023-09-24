from docx import Document

def get_title_bypath(path1):
    name = path1.split('\\')[-1].split(".")[0]
    return name

def get_heading_text(paragraphs, heading_name):
    found = False
    text = ""
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 1') and (heading_name in paragraph.text):
            found = True
            continue
        if found and paragraph.style.name != "Heading 1":
            text += paragraph.text
            text += '\n\n'
        elif found and paragraph.style.name == "Heading 1":
            break
    return text