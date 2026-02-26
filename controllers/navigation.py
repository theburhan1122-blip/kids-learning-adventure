"""
Navigation Controller — simple view routing for Flet.
"""


class NavigationController:
    """Maps route names to view-builder functions and handles page transitions."""

    def __init__(self, page):
        self.page = page
        self._routes = {}
        self._history = []

    def register(self, route_name: str, view_builder):
        """
        Register a route.

        Args:
            route_name: String identifier (e.g. 'home', 'english', 'quiz').
            view_builder: Callable(page) -> ft.Control that builds the view.
        """
        self._routes[route_name] = view_builder

    def navigate_to(self, route_name: str, **kwargs):
        """
        Navigate to a registered route.

        Args:
            route_name: The route to navigate to.
            **kwargs: Extra arguments passed to the view builder.
        """
        if route_name not in self._routes:
            print(f"[NAV] Unknown route: {route_name}")
            return

        self._history.append(route_name)
        builder = self._routes[route_name]

        # Build the new view
        view = builder(self.page, **kwargs)

        # Swap page content
        self.page.controls.clear()
        self.page.controls.append(view)
        self.page.update()

    def go_back(self):
        """Navigate to the previous route."""
        if len(self._history) > 1:
            self._history.pop()  # Remove current
            prev = self._history[-1]
            # Rebuild previous view
            builder = self._routes[prev]
            view = builder(self.page)
            self.page.controls.clear()
            self.page.controls.append(view)
            self.page.update()
        else:
            # Default to home
            self.navigate_to("home")

    def go_home(self):
        """Navigate to home."""
        self.navigate_to("home")
