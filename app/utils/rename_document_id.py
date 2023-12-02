from typing import Any


def __renameDocumentIdHelper(document, level=0):
    if level >= 10:
        return
    if isinstance(document, dict):
        if '_id' in document:
            document['id'] = document.pop('_id')
        for field in document:
            __renameDocumentIdHelper(document[field], level+1)
    elif isinstance(document, list):
        for element in document:
            __renameDocumentIdHelper(element, level+1)
    return


def renameDocumentId(document: Any):
    __renameDocumentIdHelper(document)
    return document
