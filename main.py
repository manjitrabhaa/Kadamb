from flask import Flask, render_template, request, flash
import json
import random
import os
import pyperclip

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load quotes from a JSON file
with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)


# Define a function to get a random quote with author
def get_random_quote():
    # Select a random quote from the list
    quote_obj = random.choice(quotes)
    # Extract the quote and author name
    quote = quote_obj['Quote']
    author = quote_obj['Author']
    return {'quote': quote, 'author': author}


# Define the root route to display a random quote with author
@app.route('/')
def display_quote():
    # Call the get_random_quote function to get a random quote with author
    quote = get_random_quote()
    return render_template('quote.html', quote=quote)


# Define the route to copy quote to clipboard
# Define the route to copy quote to clipboard
@app.route('/copy', methods=['POST'])
def copy_to_clipboard():
    quote = request.form['quote']
    author = request.form['author']
    quote_with_author = f'"{quote}" - {author}'
    pyperclip.copy(quote_with_author)
    flash('Copied')
    return '', 204



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
