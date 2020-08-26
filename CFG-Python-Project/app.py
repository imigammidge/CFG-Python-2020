from flask import Flask, render_template, request, make_response, redirect

def start_flask():

    app = Flask(__name__)

    # Get username from the request - should work for every page
    def get_username(req):
        return req.cookies.get('pokemon_username')


    @app.route('/', methods=['POST', 'GET'])
    def show_home():
        if 'pokemon_username' not in request.cookies:
            if 'username' not in request.form:
                return render_template('home.html', no_delay=request.args.get('no_delay'))
            else:
                user = request.form.get('username').strip()
                resp = make_response(render_template('home.html', user=user, no_delay=True))
                resp.set_cookie('pokemon_username', user) if user else resp.delete_cookie('pokemon_username')
                return resp
        else:
            return render_template('home.html', user=get_username(request))


    @app.route('/reset')
    def reset_username():
        resp = redirect('/{}'.format('' if not request.args.get('no_delay') else '?no_delay=True'))
        resp.delete_cookie('pokemon_username')
        return resp


    @app.errorhandler(Exception)
    def error_page(e):
        return render_template('error.html', error=e)


    @app.route('/start')
    def start_game():
        return render_template('start.html', user=get_username(request))


    @app.route('/accept')
    def accept_challenge():
        # Currently trying to customise this
        return render_template('battle.html', user=get_username(request))


    @app.route('/exit')
    def reject_challenge():
        # Currently returns a generic template! You can make a copy this template and personalize it for this option.
        return render_template('generic.html', user=get_username(request))

    
    app.run(host="0.0.0.0", port=8080, debug=True)
