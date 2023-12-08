from typing import Any

"""
Handles renaming _id for a documents, also takes care of handling
the nested level documents
"""
def rename_document_id_dict(document: dict):
    if '_id' in document:
        document['id'] = str(document.pop('_id'))
    for field in document:
        # Handling nested level _id in a document.
        rename_document_id(document[field])
    return document

"""
Handles renaming _id for a list of documents
"""
def rename_document_id_list(documents: list):
    for document in documents:
        rename_document_id(document)
    return documents

"""
Handles renaming _id for a document of type Any
"""
def rename_document_id(document: Any):
    if isinstance(document, dict):
        return rename_document_id_dict(document)
    elif isinstance(document, list):
        return rename_document_id_list(document)
    return