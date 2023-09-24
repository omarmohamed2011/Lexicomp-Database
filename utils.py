import json
import webbrowser

from docx import Document

def get_exact_heading_text(paragraphs, heading_name):
    found = False
    text = ""
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 1') and (heading_name == paragraph.text):
            found = True
            continue
        if found and paragraph.style.name != "Heading 1":
            text += paragraph.text
            text += '\n\n'
        elif found and paragraph.style.name == "Heading 1":
            break
    return text

def read_doc(path):
    document = Document(path)
    return document

def get_title(document):
    return document.paragraphs[0].text

def get_disease_txt(paragraphs):
    list_paragraphs = []
    temp=None
    for p in paragraphs:
        text=p.text
        if len(text) >1:
            if text[-1] != '.':
                temp=text
            else:
                if temp is not None:
                    list_paragraphs.append(temp+text)
                    temp=None
                else:
                    list_paragraphs.append(text)

    return list_paragraphs

def get_paragraphs_lst(paragraphs, heading_name):
    found = False
    heading_paragraphs=[]
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 1') and (heading_name in paragraph.text):
            found = True
            continue
        if found and paragraph.style.name != "Heading 1":
            heading_paragraphs.append(paragraph)
        elif found and paragraph.style.name == "Heading 1":
            break
    return heading_paragraphs

INTRODUCTORY_MESSAGE  = "The given text contains information about drugs, medical conditions, " \
                                              "and the corresponding drug dosage for each medical condition. The task " \
                                              "is to extract this information and convert it into JSON format, " \
                                              "where the medical condition is the key and the value is a dictionary " \
                                              "containing the note (if found) and dosage_text (in raw format, " \
                                              "if found). If the note or dosage_text is not found, their respective " \
                                              "values should be set to None in the dictionary."


def load_json(file_path):
    data = None
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def get_html_from_catg(medscape_data, class_name, drug_name):
    # TODO make the method to srap from category add category in signature and description
    age_ranges = medscape_data[class_name][drug_name]['age_ranges']
    range_titles = age_ranges.keys()
    html = []
    html.append(f"<h1>{drug_name}</h1>")
    description = f"<b>class name:</b> {class_name} <b>drug name:</b> {drug_name}"
    html.append(f"<p>{description}<p>")
    for title in range_titles:
        html.append(f"<h2>{title}</h2>")
        html.append(age_ranges[title])
    html = "\n".join(html)

    return html


def open_html(html):
    with open("temp.html", 'w') as f:
        f.write(html)
    webbrowser.open("temp.html")

