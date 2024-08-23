"""
this is a small translation tool.
You can translate a Metaobject on shopify and register the translation
"""

from init_paths import add_all_to_path

add_all_to_path()


from class_shopify_admin_api import GraphQlAdminAPI
from class_translator import Translator
from pagination_shopify_api import pageInfo
from icecream import ic

shopify_admin_api = GraphQlAdminAPI()
translator = Translator()

deutsche_lizenz = "Soweit im jeweiligen Angebot nichts anderes angegeben ist, erhalten Sie eine zeitlich und räumlich unbeschränkte, nicht ausschließliche Nutzungslizenz, welche auf die private Verwendung beschränkt ist. Eine kommerzielle Nutzung ist, sowohl für den Inhalt als Ganzes als auch für Teile des Inhaltes, ausgeschlossen. Die private Verwendung der digitalen Inhalte ist unbegrenzt möglich, sie dürfen insbesondere verändert, vervielfältigt und mit anderen Produkten oder digitalen Inhalten verbunden werden."


def register_content(_translated_content, _gid):

    for item in _translated_content:

        ic(response)


def fetch_all_metaobjects_by_topic(_topic: str) -> list:
    """fetch all metaobjects of a topic (e.g. "product_content")
    :resp: list of metaobject GIDs
    """
    _output = []
    page = pageInfo()

    while page.hasNextPage:
        _resp = shopify_admin_api.get_all_metaobjects_by_type(_topic)
        page = pageInfo(**_resp.json()["data"]["metaobjects"]["pageInfo"])
        for item in _resp.json()["data"]["metaobjects"]["edges"]:
            _output.append(item["node"]["id"])

    return _output


def translate_all_metaobjects_by_topic(_topic: str):
    """fetch, translate and register all metaobjects of a topic (e.g. "product_content")"""

    mo_ids = fetch_all_metaobjects_by_topic(_topic)
    for mo_id in mo_ids:
        content = shopify_admin_api.get_translatable_content(mo_id)
        for item in content:
            _hash = item["digest"]
            _key = item["key"]
            _translated_content = translator.translate(item["value"])
            if (
                mo_id == "gid://shopify/Metaobject/88559944022"
                and _key == "multi_line_text"
            ):
                _translated_content["DE"] = deutsche_lizenz

            response = shopify_admin_api.register_translation(
                mo_id,
                _key,
                _hash,
                _translated_content,
            )

            ic(response)


def main():
    """
    main function of the small translation tool

    gets the translatable content of a Metaobject on shopify,
    translates it with the Translator class and registers the translation
    on the shopify server

    :return: None
    """
    translate_all_metaobjects_by_topic("product_content")
    ic("done")


if __name__ == "__main__":
    main()
