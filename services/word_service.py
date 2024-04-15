import logging
import modules.dictionary as dictionary
from quart import Quart, request, jsonify, Response

from modules.statistics import Statistics

BASE_URL = "/api/v1/"
SIMILAR_URL = BASE_URL + 'similar'
STATS_URL = BASE_URL + 'stats'
DOCS_URL = BASE_URL + 'docs'

app = Quart(__name__)
app.json.sort_keys = False

# Configure logging to send errors to stderr
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.ERROR)

statistics = Statistics()

# Initialize the dictionary during application startup
dictionary.init_dictionary()

@app.route(SIMILAR_URL, methods=['GET'])
async def get_similar_words() -> tuple[Response, int]:
    statistics.start_processing()

    word = request.args.get('word', '').lower()
    if not word:
        return jsonify(error="Word parameter is required"), 400

    # Find similar words
    try:
        similar_words = dictionary.get_similar_words(word)
    except dictionary.WordNotFound:
        return jsonify(error="Word not found in the dictionary"), 404

    statistics.end_processing()
    return jsonify(similar=similar_words), 200


@app.route(STATS_URL, methods=['GET'])
async def get_stats() -> tuple[Response, int]:

    total_words = dictionary.get_total_words()
    total_requests = statistics.total_requests
    avg_processing_time_ns = statistics.get_avg_processing_time_ns()

    return jsonify(
        totalWords=total_words,
        totalRequests=total_requests,
        avgProcessingTimeNs=avg_processing_time_ns,
    ), 200


@app.route(DOCS_URL, methods=['GET'])
def api_docs() -> Response:
    # API documentation endpoint to describe how to use the API.
    return jsonify({
        "endpoints": {
            SIMILAR_URL: "Find similar words in the dictionary",
            STATS_URL: "Get general statistics about the program",
            DOCS_URL: "View API documentation"
        }
    })
