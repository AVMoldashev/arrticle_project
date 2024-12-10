def article_validator(article):
    errors = {}
    if not article.title:
        errors['title'] = "title - является обяз. полем"
    elif len(article.title) > 50:
        errors['title'] = "длина title - не мб > 50"
    if not article.content:
        errors['content'] = "content - является обяз. полем"

    if not article.author:
        errors['author'] = "author - является обяз. полем"
    elif len(article.author) > 50:
        errors['author'] = "длина author - не мб > 50"

    return errors