from docx import Document

def get_drug_interactions(paragraphs):
    found = False
    text = ""
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 1') and paragraph.text == 'Drug Interactions':
            found = True
            continue
        if found and paragraph.style.name != "Heading 1":
            text += paragraph.text
            text += '\n\n'
        elif found and paragraph.style.name == "Heading 1":
            break
    return text

def get_paragraphs_lst(paragraphs):
    paragraph_list = []
    for paragraph in paragraphs:
        paragraph_list.append(paragraph.text)
    return paragraph_list

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

def get_title(document):
    return document.paragraphs[0].text

def get_maximum(dose):
    ##"(maximum: 60 mg/24 hours) g/L mg/l day mg/"
    regex1 = "(M|m)aximum: (\d)+?(.(\d)+?)? (.{2}|.|.{3})/(.|.{2}|.{3}|.{4}|.{5}) (.{5}|.{4}|.{3}|.{2}|.{1})?"
    regex2 = "(M|m)aximum dose: (\d)+?(.(\d)+?)? (.{2}|.|.{3})/(.|.{2}|.{3}|.{4}|.{5}) (.{5}|.{4}|.{3}|.{2}|.{1})?"
    regex3 = "(M|m)aximum daily dose: (\d)+?(.(\d)+?)? (.{2}|.|.{3})/(.|.{2}|.{3}|.{4}|.{5}) (.{5}|.{4}|.{3}|.{2}|.{1})?"
    regex4 = "(M|m)aximum single dose: (\d)+?(.(\d)+?)? (.{2}|.|.{3})"
    regex5 = "(M|m)aximum total dose: (\d)+?(.(\d)+?)? (.{2}|.|.{3})"
    regex6 = "(M|m)aximum: (\d)+?(.(\d)+?)? (.{2}|.|.{3})"

    if re.search(regex1,dose):
        return re.search(regex1,dose)
    if re.search(regex2,dose):
        return re.search(regex2,dose)
    if re.search(regex3,dose):
        return re.search(regex3,dose)
    if re.search(regex4,dose):
        return re.search(regex4,dose)
    if re.search(regex5,dose):
        return re.search(regex5,dose)
    if re.search(regex6,dose):
        return re.search(regex5,dose)

def return_maximum(dose):
    try:
        span_range = get_maximum(dose).span()
        return dose[span_range[0]:span_range[1]]
    except:
        return ''
