import tornado.ioloop
import tornado.options
import tornado.web

from tornado_swagger.const import API_OPENAPI_3
from tornado_swagger.model import register_swagger_model
from tornado_swagger.parameter import register_swagger_parameter
from tornado_swagger.setup import setup_swagger
from tornado_swagger.setup import export_swagger


class PostsHandler(tornado.web.RequestHandler):
    def get(self):
        """
        ---
        tags:
        - Posts
        summary: List posts
        description: List all posts in feed
        produces:
        - application/json
        responses:
            200:
              description: list of posts
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/PostModel'
        """
        data = {
            "test":"ffff"
        }
        self.write(data) 
    
    def post(self):
        """
        ---
        tags:
        - Posts
        summary: Add posts
        description: Add posts in feed
        produces:
        - application/json
        parameters:
        -   in: body
            name: body
            description: post data
            required: true
            schema:
              $ref: '#/components/schemas/PostModel'
        """


class PostsDetailsHandler(tornado.web.RequestHandler):
    def get(self, posts_id):
        """
        ---
        tags:
        - Posts
        summary: Get posts details
        description: posts full version
        produces:
        - application/json
        parameters:
        -   $ref: '#/components/parameters/PostId'
        responses:
            200:
              description: list of posts
              schema:
                $ref: '#/components/schemas/PostModel'
        """

    def patch(self, posts_id):
        """
        ---
        tags:
        - Posts
        summary: Edit posts
        description: Edit posts details
        produces:
        - application/json
        parameters:
        -   $ref: '#/components/parameters/PostId'
        -   in: body
            name: body
            description: post data
            required: true
            schema:
              $ref: '#/components/schemas/PostModel'
        """

    def delete(self, posts_id):
        """
        ---
        tags:
        - Posts
        summary: Delete posts
        description: Remove posts from feed
        produces:
        - application/json
        parameters:
        -   $ref: '#/components/parameters/PostId'
        """


@register_swagger_parameter
class PostId:
    """
    ---
    name: posts_id
    in: path
    description: ID of post
    required: true
    type: string
    """


# @register_swagger_model
class PostModel:
    """
    ---
    type: object
    description: Post model representation
    properties:
        id:
            type: integer
            format: int64
        title:
            type: string
        text:
            type: string
        is_visible:
            type: boolean
            default: true
    """
class MytestOldHandler(tornado.web.RequestHandler):

    def post(self):
        """
        ---
        tags:
        -   MytestOld
        summary: MytestOld desc
        description:  MytestOld desc
        produces:
        -   application/json
        parameters:
        -   in: body
            name: post json
            required: true
            description: post json
            schema:
                type: object
                required:
                    -   astask_recruiter_id
                    -   teammember_userid
                properties:
                    astask_recruiter_id:
                        type: string
                        example: team5ca64605696924.59748857
                    teammember_userid:
                        type: string
                        example: d74120ba-ca26-4654-909c-aad8863df9c6
                    astask_titles:
                        type: array
                        items:
                            type: string
                        example: 
                        -   emergency medicine physician
                    astask_mandatory_skills:
                        type: array
                        items:
                            type: string
                        example: 
                        -   road engineering
                        -   Autocad
                        -   work supervisio
        responses:
            200:
                description: object
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                astask_titles_relaxed:
                                    type: array
                                    description: astask_titles_relaxed.
                                    items:
                                        type: string
                                astask_mandatory_skills_relaxed:
                                    type: array
                                    description: astask_mandatory_skills_relaxed.
                                    items:
                                        type: array
                                        items:
                                            type: string
        """
        data = {
            "test":"ffff1222"
        }
        self.write(data) 
    

class MytestHandler(tornado.web.RequestHandler):
    
    def post(self):
        """
        ---
        tags:
        -   Mytest
        summary: mytest desc
        description:  mytest desc
        produces:
        -   application/json
        requestBody:
            description: Afuck
            required: true
            content:
                application/json:
                    schema:
                        type: object
                        required:
                            -   astask_recruiter_id
                            -   teammember_userid
                        properties:
                            astask_recruiter_id:
                                type: string
                                example: team5ca64605696924.59748857
                            teammember_userid:
                                type: string
                                example: d74120ba-ca26-4654-909c-aad8863df9c6
                            astask_titles:
                                type: array
                                items:
                                    type: string
                                example: 
                                -   emergency medicine physician
                            astask_mandatory_skills:
                                type: array
                                items:
                                    type: string
                                example: 
                                -   road engineering
                                -   Autocad
                                -   work supervisio
        responses:
            200:
                description: object
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                astask_titles_relaxed:
                                    type: array
                                    description: astask_titles_relaxed.
                                    items:
                                        type: string
                                astask_mandatory_skills_relaxed:
                                    type: array
                                    description: astask_mandatory_skills_relaxed.
                                    items:
                                        type: array
                                        items:
                                            type: string
        """
        data = {
            "test":"ffff1222"
        }
        self.write(data) 
    

class Application(tornado.web.Application):
    _routes = [
        tornado.web.url(r"/api/mytest", MytestHandler),
        # tornado.web.url(r"/api/posts", PostsHandler),
        # tornado.web.url(r"/api/posts/(\w+)", PostsDetailsHandler),
        # tornado.web.url(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/var/www"}),
    ]

    def __init__(self):
        settings = {"debug": False}
        setup_swagger(
            self._routes,
            swagger_url="/doc",
            api_base_url="/",
            description="",
            api_version="1.0.0",
            title="ML demo API",
            contact="name@domain",
            schemes=["https"],
            security_definitions={"ApiKeyAuth": {"type": "apiKey", "in": "header", "name": "X-API-Key"}},
            api_definition_version=API_OPENAPI_3,
        )
        super(Application, self).__init__(self._routes, **settings)


if __name__ == "__main__":
    tornado.options.define("port", default="8080", help="Port to listen on")
    tornado.options.parse_command_line()
    app = Application()
    app.listen(port=8080)

    tornado.ioloop.IOLoop.current().start()