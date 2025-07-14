# Flask basics course
Following along and tracking it through this repo!
Currently understood :
1. Routing and decorators:
   example of routes: - @app.route("/") -> usually used for the homepage
   - @app.route("/<variable-name>) -> to create a route with a specific variable name
   - @app.route("/<converter:variable-name>) -> we can use converters to convert the variables. ex: ("/<int:number>)
   
