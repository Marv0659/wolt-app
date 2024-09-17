from bottle import default_app, get, post, response, run, template, static_file, request, redirect
from icecream import ic
import os
import x

##############################
@get("/")
def _():
    return "x"


##############################
@get("/mixhtml.js")
def _():
    return static_file("mixhtml.js", ".")

##############################
@get("/mojocss.js")
def _():
    return static_file("mojocss.js", ".")

##############################
@get("/mixhtml.css")
def _():
    return static_file("mixhtml.css", ".")

##############################
@get("/login")
def _():
    try:
        return template("login.html")
    except Exception as ex:
        if len(ex.args) >= 2: # own created exception
            response.status = ex.args[1]
            return {"error":ex.args[0]}
        else: # python exception, not under our control
            error = "System under maintenance. Please try again"
            response.status = 500
            return {"error":f"{error}"}
    finally:
        pass


##############################

@post("/signup")
def _():
    try:
        user_name = x.validate_user_name()
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        user_last_name = x.validate_user_last_name()
    except Exception as ex:
        if len(ex.args) >= 2: # own created exception
            response.status = ex.args[1]
            toast = template("__toast.html", message=ex.args[0])
            return toast
        else: # python exception, not under our control
            error = "System under maintenance. Please try again"
            response.status = 500
            return {"error":f"{error}"}
    finally:
        pass



##############################


@get("/signup")
def _():
    try:
        return template("signup")
    except Exception as ex:
        if len(ex.args) >= 2: # own created exception
            response.status = ex.args[1]
            
            return {"error":ex.args[0]}
        else: # python exception, not under our control
            error = "System under maintenance. Please try again"
            response.status = 500
            return {"error":f"{error}"}
    finally:
        pass


##############################
@get("/profile")
def _():
    try:
        name = request.get_cookie("me", secret="my secret")

        if name is None: # not a valid cookie
           # return redirect("/login")
            response.status = 303
            response.set_header("location", "/login")
        return template("profile.html", name=name)
    except Exception as ex:
        if len(ex.args) >= 2: # own created exception
            response.status = ex.args[1]
            return {"error":ex.args[0]}
        else: # python exception, not under our control
            error = "System under maintenance. Please try again"
            response.status = 500
            return {"error":f"{error}"}
    finally:
        pass


##############################
@post("/login")
def _():
    try:
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        # TODO: check if email and password are correct
        name = "Marvin"
        response.set_cookie("me", name, secret="my secret")
        
        return "<template mix-redirect='/profile'></template>"


    except Exception as ex:
        if len(ex.args) >= 2: # own created exception
            response.status = ex.args[1]
            toast = template("__toast.html", message=ex.args[0])
            return toast
        else: # python exception, not under our control
            error = "System under maintenance. Please try again"
            response.status = 500
            return {"error":f"{error}"}
    finally:
        pass



##############################
@get("/logout")
def _():
    response.delete_cookie("me")
    return redirect("/login")


##############################
if "PYTHONANYWHERE_DOMAIN" in os.environ:
    application = default_app()
else:
    ic("Server listening...")
    run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0.1)

##############################

