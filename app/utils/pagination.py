def paginate(query, page: int = 1, page_size: int = 20):
    offset = (page - 1) * page_size
    return query.offset(offset).limit(page_size)
