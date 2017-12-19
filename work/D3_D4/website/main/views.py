"""Widoki"""
from django.shortcuts import render

# Main View
def template(request, templatename):
    """ Main View """
    return render(request, templatename)

# TODO: Contexted View
def contextedteamplate(request, templatename):
    """ Contexted View """
    context = {
        # TODO: CONTEXT IMPLEMENT HERE
    }
    return render(request, templatename, context)
