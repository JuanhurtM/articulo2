from flask import Flask, render_template
from data import Articles
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask,jsonify,send_from_directory
from marshmallow import Schema, fields

app = Flask(__name__)

spec = APISpec( 
    title='Flask-api-swagger-doc',
    version='1.0.0.',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(),MarshmallowPlugin()]
)

@app.route('/api/swagger.json')
def create_swagger_spec():
        return jsonify(spec.to_dict())



class ArticleResponseSchema(Schema):
        id = fields.Int()
        title = fields.Str()
        body = fields.Str()
        author = fields.Str()
        create_date = fields.Str()

class ArticleListResponseSchema(Schema):
        article_list = fields.List(fields.Nested(ArticleResponseSchema))

@app.route('/articles')
def article():
    """Get List of Articles
        ---
        get:
            description: Get List of Articles
            responses:
                200:
                    description: Return an article list
                    content:
                        application/json:
                            schema: ArticleListResponseSchema
    """

    resultado = data.Articles()

    return ArticleListResponseSchema().dump({'article_list':resultado})

with app.test_request_context():
    spec.path(view=article)


@app.route('/')
def index():
    datos = Articles()
    return render_template('index.html', data=datos)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/article0')
def article0():
    datos = Articles()
    return render_template('article0.html', data=datos)


@app.route('/article1')
def article1():
    datos = Articles()
    return render_template('article1.html', data=datos)


@app.route('/article2')
def article2():
    datos = Articles()
    return render_template('article2.html', data=datos)


@app.route('/docs')
@app.route('/docs/<path:path>')
def swagger_docs(path=None):
    if not path or path == 'docs.html':
        return render_template('docs.html',base_url='/docs')
    else:
        return send_from_directory('static',path)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
