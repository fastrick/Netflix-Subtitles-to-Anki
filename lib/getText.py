from bs4 import BeautifulSoup


def get_text_from_xml(xml_file):
    soup = BeautifulSoup(open(xml_file), "xml")

    result_dict = {}
    for p in soup.find_all('p'):
        attributes = {
            "begin": p["begin"],
            "end": p["end"],
            "region": p["region"],
            "style": p["style"],
            "xml:id": p["xml:id"]
        }

        text = ' '.join(p.stripped_strings)

        result_dict[attributes["begin"]] = text

    return result_dict

#get_text_from_xml("Subtitles/Better Call Saul/S02/E01-pt.xml")