"""
Views for the user profile app:
    - UserProfileListView
    - UserProfileDetailView
    - UserProfileCreateView
    - UserProfileUpdateView
"""
from django.views import generic

from .forms import UserProfileForm
from .models import UserProfile


class UserProfileListView(generic.ListView):
    """
    A view for displaying a list of user profiles.

    Attributes:
        model (Model): The model class representing the user profiles.
        template_name (str): The name of the template to use for rendering the view.

    Methods:
        get_queryset(): Retrieves the query set of user profiles to be displayed.
        get_context_data(): Adds additional context data to be passed to the template.

    """

    model = UserProfile
    template_name = "user_profile_list.html"


class UserProfileDetailView(generic.DetailView):
    """
    A view for displaying a single user profile.
    """

    model = UserProfile
    template_name = "user_profile_detail.html"


class UserProfileCreateView(generic.CreateView):
    """
    A view for creating a user profile.

    Attributes:
        model (class): The model class for the user profile.
        form_class (class): The form class for the user profile.
        template_name (str): The name of the template to be used for rendering the view.

    Methods:
        dispatch(request, *args, **kwargs):
            Handles the incoming HTTP request and returns the HTTP response or a redirect to another view,
            depending on the HTTP method.

        form_valid(form):
            Saves the form instance, sets the user profile user attribute to the current user, and redirects
            to the success URL.

        get_success_url():
            Returns the URL to redirect to after a successful form submission.

    """

    model = UserProfile
    form_class = UserProfileForm
    template_name = "user_profile_create.html"


class UserProfileUpdateView(generic.UpdateView):
    """
    A view for updating user profile.
    """

    model = UserProfile
    form_class = UserProfileForm
    template_name = "user_profile_update.html"
