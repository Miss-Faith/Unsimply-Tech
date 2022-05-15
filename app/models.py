class Quote:
    '''
    Quote class to define quotes
    '''

    all_articles = []

    def __init__(self,author,id,quote):
        self.author = name
        self.id = id
        self.quote = quote

    def save_quote(self):
        Quote.all_quotes.append(self)