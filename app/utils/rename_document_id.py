from typing import Any


def __rename_document_id_helper(document, level=0):
    if level >= 10:
        return
    if isinstance(document, dict):
        if '_id' in document:
            document['id'] = document.pop('_id')
        for field in document:
            __rename_document_id_helper(document[field], level+1)
    elif isinstance(document, list):
        for element in document:
            __rename_document_id_helper(element, level+1)
    return


def rename_document_id(document: Any):
    __rename_document_id_helper(document)
    return document
