from django import template


register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


@register.inclusion_tag("home/inclusion/top_menu.html", takes_context=True)
def top_menu(context, root, calling_page=None):
    menuitems = root.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.has_children = menuitem.get_children().live().in_menu().exists()

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "request": context['request']
    }


@register.inclusion_tag("home/inclusion/footer.html", takes_context=True)
def display_footer(context):
    return {
        "request": context['request']
    }